### primeiro passo: leitura e inspeção dos arquivos 
### em tese, fazer nesse arquivo só pra leitura dos 4 que o reginaldo mandou

def ler_arquivo_atendimentos():   #função pra ler o arquivo
    with open ("automatos-trabalho1/assets/01_atendimentos_bagunçados.txt", "r", encoding= "utf-8") as arq :   #lê o arquivo. já tá definido pro modo leitura apenas e deixei o caminho salvo pra ler da pasta do repositorio e da pasta que tá salvo os assets
        conteudo = arq.readlines()   #o readlines cria uma lista de strings com base no /n invisivel que tem entre um chamado e outro, e com isso, separa chamado a chamado            
        contador = len(conteudo)   #se baseia na variavel acima pra decretar o numero de linhas, já que a função de cima lê todo o arquivo antes de "arrumar"  
        print (f"linhas: {contador}")  #mostra o numero de linhas do arquivo de atendimentos
        for linha in conteudo [0:100]: #mostra os 100 primeiros chamados 
            print(linha.strip())   #essa função tira o /n invisivel do final de cada chamado, pra na hora de vizualizar, não ter um espaço extra separando cada chamado
        return contador, conteudo   #retorna os valores de linhas e o texto como um todo pra serem usados depois


def ler_arquivo_logs ():
    with open ("automatos-trabalho1/assets/02_logs_mistos.log", "r", encoding= "utf-8") as arq:
        conteudo = arq.readlines()   #o readlines cria uma lista de strings com base no /n invisivel que tem entre um chamado e outro, e com isso, separa chamado a chamado            
        contador = len(conteudo)   #se baseia na variavel acima pra decretar o numero de linhas, já que a função de cima lê todo o arquivo antes de "arrumar"  
        print (f"linhas: {contador}")  #mostra o numero de linhas do arquivo de atendimentos
        for linha in conteudo [0:100]: #mostra os 100 primeiros chamados 
            print(linha.strip())   #essa função tira o /n invisivel do final de cada chamado, pra na hora de vizualizar, não ter um espaço extra separando cada chamado
        return contador, conteudo   #retorna os valores de linhas e o texto como um todo pra serem usados depois
            
    
def ler_arquivo_mensagem_chat ():
     with open ("automatos-trabalho1/assets/03_mensagens_chat.txt", "r", encoding= "utf-8") as arq:
        conteudo = arq.readlines()   #o readlines cria uma lista de strings com base no /n invisivel que tem entre um chamado e outro, e com isso, separa chamado a chamado            
        contador = len(conteudo)   #se baseia na variavel acima pra decretar o numero de linhas, já que a função de cima lê todo o arquivo antes de "arrumar"  
        print (f"linhas: {contador}")  #mostra o numero de linhas do arquivo de atendimentos
        for linha in conteudo [0:100]: #mostra os 100 primeiros chamados 
            print(linha.strip())   #essa função tira o /n invisivel do final de cada chamado, pra na hora de vizualizar, não ter um espaço extra separando cada chamado
        return contador, conteudo   #retorna os valores de linhas e o texto como um todo pra serem usados depois


def ler_arquivo_exportacao_suja ():
    with open ("automatos-trabalho1/assets/04_exportacao_suja.csv", "r", encoding= "utf-8") as arq:
        conteudo = arq.readlines()   #o readlines cria uma lista de strings com base no /n invisivel que tem entre um chamado e outro, e com isso, separa chamado a chamado            
        contador = len(conteudo)   #se baseia na variavel acima pra decretar o numero de linhas, já que a função de cima lê todo o arquivo antes de "arrumar"  
        print (f"linhas: {contador}")  #mostra o numero de linhas do arquivo de atendimentos
        for linha in conteudo [0:100]: #mostra os 100 primeiros chamados 
            print(linha.strip())   #essa função tira o /n invisivel do final de cada chamado, pra na hora de vizualizar, não ter um espaço extra separando cada chamado
        return contador, conteudo

