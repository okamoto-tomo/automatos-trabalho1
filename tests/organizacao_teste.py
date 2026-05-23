import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import d_organizacao

# ==========================================
# EXEMPLO DE USO PRÁTICO (SIMULAÇÃO)
# ==========================================
if __name__ == "__main__":
    # Inicializa o organizador
    organizador = d_organizacao.OrganizadorDados()

    # Simulando dados que seriam extraídos pelas Regex nos arquivos do trabalho
    # Arquivo: 01_atendimentos_bagunçados.txt
    organizador.adicionar_ocorrencia(
        tipo="CPF", 
        valor="123.456.789-00", 
        origem="01_atendimentos_bagunçados.txt", 
        valido=True
    )
    organizador.adicionar_ocorrencia(
        tipo="CPF", 
        valor="111222333-44", 
        origem="01_atendimentos_bagunçados.txt", 
        valido=False  # Mal formatado estruturalmente
    )

    # Arquivo: 03_mensagens_chat.txt
    organizador.adicionar_ocorrencia(
        tipo="E-mail", 
        valor="aluno@ufpa.br", 
        origem="03_mensagens_chat.txt", 
        valido=True
    )
    organizador.adicionar_ocorrencia(
        tipo="URL", 
        valor="http://site-invalido..com", 
        origem="03_mensagens_chat.txt", 
        valido=False
    )

    # Exportando a estrutura para o arquivo JSON exigido
    organizador.exportar_para_json("ocorrencias_estruturadas.json")