'''
a) Leitura e inspeção dos arquivos:
Implemente um módulo capaz de: ler todos os arquivos fornecidos; contabilizar o 
número de linhas de cada arquivo; identificar o tipo geral de conteúdo de cada 
arquivo (texto livre, log, chat ou CSV); apresentar uma pequena amostra de 
conteúdo de cada arquivo.
'''


arquivos_do_reginaldo = {
    "atendimentos": "01_atendimentos_bagunçados.txt",
    "logs":         "02_logs_mistos.log",
    "chat":         "03_mensagens_chat.txt",
    "exportacao":   "04_exportacao_suja.csv",
}


def ler_arquivo(identificador_do_arquivo: str, CSV: bool = False) -> None | tuple[str, list[str]]:
    """
    Abre o arquivo e retorna a lista de linhas.
    
    params:
        identificador_do_arquivo (str): Nome legível do arquivo.
        CSV (bool): Flag para .csv, ignora o cabeçalho.
        
    returns:
         arquivo (None | tuple[str, list[str]]): Tupla contendo o caminho e o conteúdo do arquivo.
         Retorna nada se o identificador do arquivo não for reconhecido.
    """
    caminho = arquivos_do_reginaldo.get(identificador_do_arquivo)
    
    if not caminho:
        print(f"Erro: O identificador '{identificador_do_arquivo}' não existe.")
        arquivo = None

    with open(f"assets/{caminho}", "r", encoding="utf-8") as arq:
        arquivo = (caminho, arq.readlines()[1:] if CSV else arq.readlines())
        
    return arquivo


def tamanho_arquivo(lista_linhas: list[str]) -> int:
    """
    Recebe a lista de linhas e diz quantas são.
    
    params:
        lista_linhas (list): Lista de conteúdo do arquivo.
        
    returns:
        tamanho (int): Quantidade de linhas do arquivo.
    """
    tamanho = len(lista_linhas)
    return tamanho


def visualizar_amostra(lista_linhas: list[str], quantidade=10) -> list[str]:
    """
    Recebe as linhas e mostra na tela a quantidade pedida (padrão 10).
    
    params:
        lista_linhas (list[str]): Lista de conteúdo do arquivo.
        quantidade (int): Quantidade de `n` primeiras linhas a serem amostradas
    return:
        amostra (str): Amostra das `n` primeiras linhas do arquivo.
    """
    
    amostra = "".join(lista_linhas[0:quantidade])
    return amostra