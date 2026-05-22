### implementação com expressão regular pra identificar e extrair os dados 

# falta expressoes_regulares
import leitura_e_inspecao
import re

def extrair_valores(caminho: str, expressoes_regulares: dict) -> list[tuple[str, str, str]]:
    lista = []
    
    arquivo_origem = caminho.replace("assets/", "")
    arquivo = leitura_e_inspecao.ler_arquivo(caminho)[1][:10]
    
    for chave in expressoes_regulares.keys():
        tipo = chave
        
        for linha in arquivo:
            expressao_regular = expressoes_regulares[tipo]
            matches = re.findall(expressao_regular, linha)
            
            if matches:
                for valor in matches:
                    lista.append((tipo, valor, arquivo_origem))
                    
    return lista