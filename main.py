from a_leitura import *
from b_extracao import *
from lib.regex_extracao_padroes import *
from c_classificacao import *
from lib.regex_classificacao_padroes import *
from d_organizacao import *
from e_analise import *


PATH_JSON_GERAL = "dados_gerais.json"
PATH_JSON_CSV = "dados_csv.json"

if __name__ == "__main__":
    
    # GERAL
    lista_geral = []
    organizacao = OrganizadorTextual()
    
    for nome_amigavel in arquivos_do_reginaldo.keys():        
        arquivo = ler_arquivo(nome_amigavel)
        caminho, conteudo = arquivo[:2]
        
        if input(f"Mostrar tamanho do arquivo {caminho}? [Y/n] > ") in "Yy":
            print(f"Tamanho do arquivo {caminho}: {tamanho_arquivo(conteudo)}")
            
        if input(f"Mostrar amostra do arquivo {caminho}? [Y/n] > ") in "Yy":
            print(f"Amostra do arquivo {caminho}: \n{visualizar_amostra(conteudo)}")
            
        extracao = extrair_valores(arquivo, regex_extracao)
        classificacao = classificar_valores(extracao, regex_classificacao)
        organizacao.adicionar_lote(classificacao)
    
    if not organizacao.exportar_json(PATH_JSON_GERAL):
        print("ERRO")
    
    analise = analisar(f"arquivos_json/{PATH_JSON_GERAL}")

    with open("relatorio/relatorio_quantitativo_dados_gerais.txt", mode="r", encoding="utf-8") as f:
        print("".join(f.readlines()))
 
    # CSV
    lista_csv = []
    organizacao_csv = OrganizadorCSV()
    
    arquivo_csv = ler_arquivo("exportacao", CSV=True)
    caminho_csv, conteudo_csv = arquivo_csv[:2]
    
    validacao_csv = validar_csv(arquivo_csv, regex_classificacao)
    organizacao_csv.adicionar_lote(validacao_csv)
    
    if not organizacao_csv.exportar_json(PATH_JSON_CSV):
        print("ERRO")
        
    analise_csv = analisar(f"arquivos_json/{PATH_JSON_CSV}")
    
    with open("relatorio/relatorio_quantitativo_dados_csv.txt", mode="r", encoding="utf-8") as f:
        print("".join(f.readlines()))
 


    
    
    
        