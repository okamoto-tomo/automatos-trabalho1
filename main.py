from a_leitura import *
from b_extracao import *
from lib.regex_extracao_padroes import *
from c_classificacao import *
from lib.regex_classificacao_padroes import *
from d_organizacao import *
from e_analise import *


PATH_JSON_GERAL = "dados_gerais.json"

if __name__ == "__main__":
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
        print("\n")
    
    print(analisar(f"arquivos_json/{PATH_JSON_GERAL}"))
    
    
    
        