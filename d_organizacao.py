'''
d) Organização dos dados extraídos. 
Os dados extraídos devem ser estruturados, como: dicionários, listas ou objetos; 
arquivos JSON ou CSV. Cada ocorrência deve conter, sempre que possível: tipo do 
dado; valor extraído; arquivo de origem; classificação (válido ou inválido).
'''

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