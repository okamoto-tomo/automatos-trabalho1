### extrair os dados pra um arquivo json utilizando dicionarios 
import json
from typing import List, Dict, Any

class OrganizadorDados:
    def __init__(self):
        # Lista que armazenará todas as ocorrências estruturadas
        self.dados_estruturados: List[Dict[str, Any]] = []

    def adicionar_ocorrencia(self, tipo: str, valor: str, origem: str, valido: bool):
        """
        Adiciona uma nova ocorrência estruturada à lista, atendendo aos requisitos
        especificados no item d) do trabalho.
        """
        registro = {
            "tipo": tipo,
            "valor": valor,
            "arquivo_origem": origem,
            "classificacao": "valido" if valido else "invalido"
        }
        self.dados_estruturados.append(registro)

    def exportar_para_json(self, caminho_arquivo: str = "dados_extraidos.json") -> bool:
        """
        Exporta todos os dados organizados para um arquivo no formato JSON.
        """
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                # O parâmetro indent=4 garante a legibilidade e o ensure_ascii=False preserva acentos
                json.dump(self.dados_estruturados, f, indent=4, ensure_ascii=False)
            print(f"[SUCESSO] Dados exportados com sucesso para: {caminho_arquivo}")
            return True
        except Exception as e:
            print(f"[ERRO] Falha ao exportar arquivo JSON: {e}")
            return False




'''
# ==========================================
# EXEMPLO DE USO PRÁTICO (SIMULAÇÃO)
# ==========================================
if __name__ == "__main__":
    # Inicializa o organizador
    organizador = OrganizadorDados()

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
'''