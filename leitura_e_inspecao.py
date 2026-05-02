### primeiro passo: leitura e inspeção dos arquivos 
### em tese, fazer nesse arquivo só pra leitura dos 4 que o reginaldo mandou

def ler_arquivo_atendimentos():   #função pra ler o arquivo
    contador = 0   #contaodor pra saber o numero de linhas do arquivo de atendimentos
    conteudo = ""  #guarda o texto de cada linha do arquivo como uma string e vai interando pelo loop for          
    with open ("automatos-trabalho1/assets/01_atendimentos_bagunçados.txt", "r") as arq :   #lê o arquivo. já tá definido pro modo leitura apenas e deixei o caminho salvo pra ler da pasta do repositorio e da pasta que tá salvo os assets
        for linha in arq:   #pra interar linha a linha do arquivo
            contador += 1   #vai somando o numero de linhas
            conteudo += linha   #vai colocando o texto de cada linha na variavel conteudo    
        print (contador)   #mostra o numero de linhas do arquivo de atendimentos
        return contador, conteudo   #retorna os valores de linhas e o texto como um todo pra serem usados depois


ler_arquivo_atendimentos()       
        


