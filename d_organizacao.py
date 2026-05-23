'''
d) Organização dos dados extraídos.
Os dados extraídos devem ser estruturados, como: dicionários, listas ou objetos;
arquivos JSON ou CSV. Cada ocorrência deve conter, sempre que possível: tipo do
dado; valor extraído; arquivo de origem; classificação (válido ou inválido).
'''

import json
import os
from typing import List, Dict, Any, Tuple


# Diretório padrão de saída para todos os JSONs gerados
DIRETORIO_JSON = "arquivos_json"


def _garantir_diretorio(caminho_dir: str) -> None:
    """Cria o diretório de saída caso ainda não exista."""
    os.makedirs(caminho_dir, exist_ok=True)


def _caminho_saida(nome_arquivo: str) -> str:
    """Monta o caminho completo dentro de arquivos_json/."""
    return os.path.join(DIRETORIO_JSON, nome_arquivo)


# ---------------------------------------------------------------------------
# Tipos auxiliares
# ---------------------------------------------------------------------------

# Saída de classificar_valores  →  (tipo, valor, origem, valido)
OcorrenciaClassificada = Tuple[str, str, str, bool]

# Saída de validar_csv          →  (id, [(campo, valido), ...], valido_geral, caminho)
RegistroCSV = Tuple[int, List[Tuple[str, bool]], bool, str]


# ---------------------------------------------------------------------------
# Organização dos arquivos 01–03  (texto livre / log / chat)
# ---------------------------------------------------------------------------

class OrganizadorTextual:
    """
    Recebe as ocorrências classificadas provenientes dos arquivos 01, 02 e 03
    e as estrutura em uma lista de dicionários uniforme.

    Cada entrada da lista segue o esquema:
        {
            "tipo"            : str,   # e-mail, telefone, cpf, url, ...
            "valor"           : str,   # string extraída do texto
            "arquivo_origem"  : str,   # nome do arquivo de onde veio
            "classificacao"   : str    # "valido" | "invalido"
        }
    """

    def __init__(self):
        self.dados: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------ #
    # Ingestão                                                             #
    # ------------------------------------------------------------------ #

    def adicionar_ocorrencia(self, tipo: str, valor: str, origem: str, valido: bool) -> None:
        """Adiciona uma única ocorrência já classificada."""
        self.dados.append({
            "tipo"           : tipo,
            "valor"          : valor,
            "arquivo_origem" : origem,
            "classificacao"  : "valido" if valido else "invalido",
        })

    def adicionar_lote(self, ocorrencias: List[OcorrenciaClassificada]) -> None:
        """
        Ingere em bloco a saída de classificar_valores().

        Parâmetros
        ----------
        ocorrencias : lista de tuplas (tipo, valor, origem, valido)
        """
        for tipo, valor, origem, valido in ocorrencias:
            self.adicionar_ocorrencia(tipo, valor, origem, valido)

    # ------------------------------------------------------------------ #
    # Exportação                                                           #
    # ------------------------------------------------------------------ #

    def exportar_json(self, nome_arquivo: str = "dados_textuais.json") -> bool:
        """
        Salva todos os dados em arquivos_json/<nome_arquivo>.

        Parâmetros
        ----------
        nome_arquivo : nome do arquivo de saída (sem caminho)

        Retorna
        -------
        True em caso de sucesso, False em caso de falha.
        """
        _garantir_diretorio(DIRETORIO_JSON)
        caminho = _caminho_saida(nome_arquivo)
        try:
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(self.dados, f, indent=4, ensure_ascii=False)
            print(f"[SUCESSO] Dados textuais exportados para: {caminho}")
            return True
        except Exception as e:
            print(f"[ERRO] Falha ao exportar dados textuais: {e}")
            return False


# ---------------------------------------------------------------------------
# Organização do arquivo 04  (CSV com registros estruturados)
# ---------------------------------------------------------------------------

# Nomes de coluna na ordem em que validar_csv() as devolve
_COLUNAS_CSV = ["nome", "email", "telefone", "cpf", "data_e_horario", "dinheiro"]


class OrganizadorCSV:
    """
    Recebe os registros validados provenientes do arquivo 04 e os estrutura
    em uma lista de dicionários.

    Cada entrada da lista segue o esquema:
        {
            "id"             : int,
            "arquivo_origem" : str,
            "classificacao"  : str,    # "valido" | "invalido"
            "campos"         : {
                "<nome_coluna>" : {
                    "valor"         : str,
                    "classificacao" : str   # "valido" | "invalido"
                },
                ...
            }
        }

    A separação dos campos preserva a granularidade por coluna, o que
    permite análises de quais campos específicos causaram a invalidação
    do registro — informação perdida caso apenas o booleano geral fosse
    armazenado.
    """

    def __init__(self):
        self.dados: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------ #
    # Ingestão                                                             #
    # ------------------------------------------------------------------ #

    def adicionar_registro(self, registro: RegistroCSV) -> None:
        """Adiciona um único registro validado."""
        id_reg, matches, valido_geral, caminho = registro

        campos: Dict[str, Dict[str, str]] = {}
        for nome_col, (valor, valido_campo) in zip(_COLUNAS_CSV, matches):
            campos[nome_col] = {
                "valor"        : valor,
                "classificacao": "valido" if valido_campo else "invalido",
            }

        self.dados.append({
            "id"            : id_reg,
            "arquivo_origem": caminho,
            "classificacao" : "valido" if valido_geral else "invalido",
            "campos"        : campos,
        })

    def adicionar_lote(self, registros: List[RegistroCSV]) -> None:
        """
        Ingere em bloco a saída de validar_csv().

        Parâmetros
        ----------
        registros : lista de tuplas (id, [(valor, valido), ...], valido_geral, caminho)
        """
        for registro in registros:
            self.adicionar_registro(registro)

    # ------------------------------------------------------------------ #
    # Exportação                                                           #
    # ------------------------------------------------------------------ #

    def exportar_json(self, nome_arquivo: str = "dados_csv.json") -> bool:
        """
        Salva todos os registros em arquivos_json/<nome_arquivo>.

        Parâmetros
        ----------
        nome_arquivo : nome do arquivo de saída (sem caminho)

        Retorna
        -------
        True em caso de sucesso, False em caso de falha.
        """
        _garantir_diretorio(DIRETORIO_JSON)
        caminho = _caminho_saida(nome_arquivo)
        try:
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(self.dados, f, indent=4, ensure_ascii=False)
            print(f"[SUCESSO] Dados CSV exportados para: {caminho}")
            return True
        except Exception as e:
            print(f"[ERRO] Falha ao exportar dados CSV: {e}")
            return False