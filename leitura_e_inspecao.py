### primeiro passo: leitura e inspeção dos arquivos 

# 1. Criamos o dicionário mapeando um "nome amigável" ao caminho real do arquivo
arquivos_do_reginaldo = {
    "atendimentos": "assets/01_atendimentos_bagunçados.txt",
    "logs": "assets/02_logs_mistos.log",
    "chat": "assets/03_mensagens_chat.txt",
    "exportacao": "assets/04_exportacao_suja.csv"
}

# 2. Uma única função genérica que faz todo o trabalho duro
def ler_arquivo(identificador_do_arquivo):
    """
    Busca o caminho do arquivo no dicionário, faz a leitura,
    mostra uma amostra das 100 primeiras linhas e retorna os dados.
    """
    # Busca o caminho correspondente no dicionário
    caminho = arquivos_do_reginaldo.get(identificador_do_arquivo)
    
    # Se o usuário digitar uma chave que não existe no dicionário, avisa e para
    if not caminho:
        print(f"Erro: O identificador '{identificador_do_arquivo}' não foi encontrado no dicionário.")
        return 0, []

    # Faz a leitura do arquivo encontrado
    with open(caminho, "r", encoding="utf-8") as arq:
        conteudo = arq.readlines()   # Cria a lista de strings com base nas quebras de linha
        contador = len(conteudo)     # Conta quantas linhas/chamados existem no total
        
        print(f"\n=== Lendo: {identificador_do_arquivo.upper()} ===")
        print(f"Total de linhas: {contador}")
        print("--- Amostra das 100 primeiras linhas ---")
        
        for linha in conteudo[0:100]:
            print(linha.strip())     # Remove o \n invisível para exibir sem linhas em branco extras
            
        print("=======================================\n")
        return contador, conteudo