### primeiro passo: leitura e inspeção dos arquivos 

# 1. Dicionário de caminhos 
arquivos_do_reginaldo = {
    "atendimentos": "assets/01_atendimentos_bagunçados.txt",
    "logs": "assets/02_logs_mistos.log",
    "chat": "assets/03_mensagens_chat.txt",
    "exportacao": "assets/04_exportacao_suja.csv"
}

# APENAS LER O ARQUIVO
def ler_arquivo(identificador_do_arquivo):
    """Apenas abre o arquivo e retorna a lista de linhas."""
    caminho = arquivos_do_reginaldo.get(identificador_do_arquivo)
    
    if not caminho:
        print(f"Erro: O identificador '{identificador_do_arquivo}' não existe.")
        return []

    with open(caminho, "r", encoding="utf-8") as arq:
        return arq.readlines()


# APENAS RETORNAR O TAMANHO
def tamanho_arquivo(lista_linhas):
    """Recebe a lista de linhas e diz quantas são."""
    return len(lista_linhas)


# APENAS EXIBIR A AMOSTRA NA TELA
def visualizar_amostra(lista_linhas, quantidade=100):
    """Recebe as linhas e mostra na tela a quantidade pedida (padrão 100)."""
    print(f"\n--- Amostra das {quantidade} primeiras linhas ---")
    for linha in lista_linhas[0:quantidade]:
        print(linha.strip())
    print("-------------------------------------------\n")