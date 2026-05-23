# EMAIL
email = [
    "joaodasilva@gmail.com",
    "maria.silva@hotmail.com",
    "usuario123@yahoo.com.br",
    "teste.email@dominio.org",
    "a1b2c3@bb.cc",
    "nome.sobrenome@empresa.com",
    "usuario.1@provedor.net",
    "contato@sub.dominio1.com",
    "email123@servico2.io",
    "fulano@exemplo.edu",
    "x1y2z3@ab.co",
    "nome.2023@mail.org",
    "a.b.c.d@dominio.com",
    "test.user@empresa.com.br",
    "superadmin@site.info",
    "usuario.teste@dominio3.co",
    "abc123@exemplo.io",
    "nome999@provedor.br",
    "email.ok1@teste.net",
    "z9a9210sxcjas1@aa.bb",
    "@gmail.com",               # sem parte local
    "joao@.com",                # domínio começa com ponto
    "joao..silva@gmail.com",    # dois pontos consecutivos
    "joao@gmail",               # sem TLD
    "JOAO@gmail.com",           # maiúscula na parte local
    "joao@gmail.c",             # TLD com 1 letra
    "joao @gmail.com",          # espaço na parte local
    ".joao@gmail.com",          # parte local começa com ponto
    "joao.@gmail.com",          # parte local termina com ponto
    "joao@gmail..com",          # dois pontos no domínio
    "",                         # string vazia
    "joao#silva@gmail.com",     # caractere especial inválido
    "joao@gmail.COM",           # TLD com maiúscula
    "apenas_texto",             # sem @ nem domínio
    "joao@@gmail.com",          # dois arrobas
    "_joao@gmail.com",          # começa com underscore (exige [a-z0-9])
    "joao@my-domain.com",       # hífen no domínio (não está em [a-z0-9])
    "joao@g.com",               # domínio com 1 char (exige {2,})
    "joao@",                    # sem domínio
    "joao@a.c",                 # TLD com 1 letra e domínio com 1 char
]

# TELEFONE
telefone = [
    "85 99999-1234",
    "98765-4321",
    "11912345678",
    "(21)987654321",
    "31 987654321",
    "47912345678",
    "(85)99999-0000",
    "91234-5678",
    "(48) 98765-1234",
    "62987654321",
    "(11) 912345678",
    "21 912345678",
    "(85)912345678",
    "79 98765-4321",
    "(41) 987654321",
    "912345678",
    "(71) 912345678",
    "81 98765-4321",
    "987654321",
    "51 91234-5678",
    "5 99999-1234",             # DDD com 1 dígito
    "(8) 98765-4321",           # DDD com 1 dígito entre parênteses
    "99999-12345",              # 10 dígitos
    "(85) 9999-1234",           # 4 dígitos antes do hífen (precisa de 5)
    "(85) 99999-12345",         # 5 dígitos após hífen (precisa de 4)
    "85 abc12-3456",            # letras no número
    "+55 85 99999-1234",        # código de país não suportado
    "(853) 99999-1234",         # DDD com 3 dígitos
    "()91234-5678",             # DDD vazio entre parênteses
    "85 9999-1234",             # só 4 dígitos na primeira parte
    "(85)9123456789",           # dígitos em excesso
    "ab 91234-5678",            # DDD com letras
    "85/91234-5678",            # barra no lugar de espaço/hífen
    "(85 91234-5678",           # parêntese sem fechar
    "85) 91234-5678",           # parêntese sem abrir
    "8591234",                  # número muito curto
    "  91234-5678",             # sem DDD, só espaço
    "85  91234-5678",           # dois espaços (só um é aceito)
    "(8 5) 91234-5678",         # espaço dentro do DDD
    "85 912345-678",            # split errado: 6+3 em vez de 5+4
]

# CPF
cpf = [
    "123.456.789-09",
    "000.000.000-00",
    "987.654.321-00",
    "111.222.333-44",
    "555.666.777-88",
    "123.456.789-09",
    "000.000.000-00",
    "987.654.321-00",
    "111.222.333-44",
    "555.666.777-88",
    "321.654.987-00",
    "321.654.987-00",
    "741.852.963-00",
    "741.852.963-00",
    "159.357.486-20",
    "159.357.486-20",
    "753.951.486-30",
    "753.951.486-30",
    "246.813.579-10",
    "246.813.579-10",
    "12.345.678-90",            # formato inválido: só 2 dígitos no 1º grupo
    "1234567890",               # 10 dígitos (falta 1)
    "123.456.78-90",            # 2 dígitos no 3º grupo
    "123.456.789-9",            # 1 dígito no verificador
    "123.456.789",              # sem dígitos verificadores
    "123456789-09",             # falta pontos
    "123.456.789-094",          # 3 dígitos verificadores
    "abc.def.ghi-jk",           # letras no lugar de dígitos
    "123.456.789-0",            # verificador incompleto
    "",                         # string vazia
    "123 456 789 09",           # espaços em vez de pontos/hífen
    "123.456.7890-9",           # dígitos mal distribuídos
    "1234.567.890-0",           # 4 dígitos no 1º grupo
    "123.4567.890-09",          # 4 dígitos no 2º grupo
    "123.456.789--09",          # hífen duplicado
    "123.456.789-",             # hífen sem verificador
    ".456.789-09",              # começa com ponto
    "123.456.-09",              # falta o 3º grupo
    "123456789",                # 9 dígitos (sem verificador)
    "12345678901234",           # 14 dígitos
]

# DATA
data = [
    "01/01/2024",
    "31/12/1999",
    "15/06/2023",
    "28/02/2000",
    "07/07/1977",
    "20/11/2025",
    "01/05/2024",
    "25/12/2023",
    "14/03/1999",
    "30/09/2010",
    "11/11/2011",
    "29/02/2000",
    "31/01/1985",
    "10/10/2010",
    "05/05/2005",
    "22/08/2019",
    "01/01/2000",
    "31/07/2030",
    "18/04/1972",
    "09/09/2009",
    "1/01/2024",                # dia com 1 dígito
    "01/1/2024",                # mês com 1 dígito
    "01/01/202",                # ano com 3 dígitos
    "01-01-2024",               # hífens em vez de barras
    "2024/01/01",               # formato americano
    "01.01.2024",               # pontos em vez de barras
    "01/01",                    # sem ano
    "/01/2024",                 # sem dia
    "01//2024",                 # mês ausente
    "",                         # string vazia
    "ab/cd/efgh",               # letras no lugar de dígitos
    "01/01/2",                  # ano com 1 dígito
    "01/01/20245",              # ano com 5 dígitos
    "00/01/2024",               # dia 00 
    "01/00/2024",               # mês 00
    "32/01/2024",               # dia 32
    "01/13/2024",               # mês 13
    "01 01 2024",               # espaços em vez de barras
    "01/01/",                   # ano ausente após a barra
    "01/01/2 24",               # espaço no meio do ano
]

# HORÁRIO
horario = [
    "00:00:00",
    "23:59:59",
    "12:30:45",
    "08:05:01",
    "15:00:00",
    "07:07:07",
    "18:45:30",
    "01:01:01",
    "10:20:30",
    "22:11:00",
    "06:00:00",
    "13:13:13",
    "09:59:59",
    "17:30:15",
    "21:00:01",
    "03:45:22",
    "16:08:55",
    "11:11:11",
    "04:30:00",
    "19:00:00",
    "0:00:00",                  # hora com 1 dígito
    "00:0:00",                  # minuto com 1 dígito
    "00:00:0",                  # segundo com 1 dígito
    "00:00",                    # sem segundos
    "12:30",                    # sem segundos
    "123:00:00",                # hora com 3 dígitos
    "00:000:00",                # minuto com 3 dígitos
    "00:00:000",                # segundo com 3 dígitos
    "ab:cd:ef",                 # letras
    "",                         # string vazia
    "25:00:00",                 # hora inválida (estruturalmente aceita pelo regex)
    "00-00-00",                 # hífens em vez de dois-pontos
    "00.00.00",                 # pontos em vez de dois-pontos
    "00:60:00",                 # minutos inválidos
    "00:00:60",                 # segundos inválidos
    " 0:00:00",                 # espaço à esquerda
    "0 0:00:00",                # espaço no meio da hora
    "00: 0:00",                 # espaço após dois-pontos
    "00:00:0 ",                 # espaço ao final
    "1:2:3",                    # todos com 1 dígito
]

# DATA E HORÁRIO
data_e_horario = [
    "01/01/2024 00:00:00",
    "31/12/1999 23:59:59",
    "15/06/2023 12:30:45",
    "28/02/2000 08:05:01",
    "07/07/1977 15:00:00",
    "20/11/2025 07:07:07",
    "01/05/2024 18:45:30",
    "25/12/2023 01:01:01",
    "14/03/1999 10:20:30",
    "30/09/2010 22:11:00",
    "11/11/2011 06:00:00",
    "29/02/2000 13:13:13",
    "31/01/2085 09:59:59",
    "10/10/2010 17:30:15",
    "05/05/2005 21:00:01",
    "22/08/2019 03:45:22",
    "01/01/2000 16:08:55",
    "31/07/2030 11:11:11",
    "18/04/1972 04:30:00",
    "09/09/2009 19:00:00",
    "01/01/2024",               # só data, sem horário
    "00:00:00",                 # só horário, sem data
    "1/01/2024 00:00:00",       # dia com 1 dígito
    "01/01/202 00:00:00",       # ano com 3 dígitos
    "01/01/2024 0:00:00",       # hora com 1 dígito
    "01/01/2024 00:00",         # sem segundos
    "01-01-2024 00:00:00",      # hífens na data
    "01/01/2024T00:00:00",      # separador ISO em vez de espaço
    "2024/01/01 00:00:00",      # formato americano
    "01/01/2024 ab:cd:ef",      # letras no horário
    "",                         # string vazia
    "01/01/202400:00:00",       # sem separador entre data e horário
    "01.01.2024 00:00:00",      # pontos na data
    "01/01/24 00-00-00",        # hífens no horário
    "01/01/2024  00:00:00",     # dois espaços como separador
    "ab/cd/2024 00:00:00",      # letras na data
    "01/01/2024 25:00:00",      # hora inválida
    "32/01/2024 00:00:00",      # dia inválido
    "01/13/2024 00:00:00",      # mês inválido
    "01/01/20 245 00:00:00",    # ano com espaço
]

# URL
url = [
    "https://www.google.com",
    "http://site.com.br",
    "www.exemplo.org",
    "dominio.net",
    "https://sub.dominio.com/pagina",
    "http://www.loja.com.br/produto/123",
    "www.portal.gov.br/noticias",
    "servico.io/api/v1",
    "https://blog.empresa.com/post/titulo",
    "http://app.sistema.net",
    "empresa.com.br",
    "https://www.site.info/sobre",
    "docs.plataforma.io",
    "www.ab.co",
    "https://portal.edu.br",
    "http://cdn.imagens.net/foto.jpg",
    "www.noticias.org/artigo",
    "https://loja.com/carrinho",
    "api.servico.com/dados",
    "http://www.sistema.com.br/login",
    "htt://site.com",           # protocolo incompleto
    "http://",                  # sem domínio
    "https://a.c",              # TLD com 1 letra
    "https://.com",             # sem domínio antes do ponto
    "ftp://site.com",           # protocolo não suportado (só http/https)
    "http://site .com",         # espaço no domínio
    "http://site..com",         # dois pontos no domínio
    "https://SITE.COM",         # maiúsculas no domínio
    "https://site.c",           # TLD com 1 letra
    "",                         # string vazia
    "https://s.com",            # domínio com 1 char
    "://site.com",              # protocolo vazio
    "https//site.com",          # falta : no protocolo
    "www..site.com",            # dois pontos após www
    "http://site",              # sem TLD
    "www.a.co",                 # domínio www.a com 1 char antes do TLD
    "http:/site.com",           # falta / no protocolo
    "https://site.com:8080",    # porta (não suportada pelo regex)
    "http://site-.com",         # hífen no domínio
    "https://?site.com",        # caractere inválido no início
]

# DINHEIRO
dinheiro = [
    "R$ 1.000,00",
    "R$50,00",
    "R$ 999,99",
    "R$ 1.000.000,00",
    "R$0,01",
    "R$ 100",
    "R$1.500",
    "R$ 49,90",
    "R$ 10.000,00",
    "R$250,00",
    "R$ 1.234.567,89",
    "R$9,99",
    "R$ 300,00",
    "R$ 75",
    "R$1.000.000",
    "R$ 0,50",
    "R$12.500,00",
    "R$ 99,00",
    "R$500",
    "R$ 3.750,25",
    "R 100,00",                 # falta o símbolo $
    "100,00",                   # sem prefixo R$
    "R$1.00,00",                # agrupamento incorreto (4 dígitos no grupo)
    "R$1.0,00",                 # agrupamento incorreto (1 dígito no grupo)
    "R$ 1,000.00",              # formato americano (ponto como decimal)
    "R$-100,00",                # valor negativo
    "R$ abc,00",                # letras no valor
    "R$1.000,000",              # 3 casas decimais
    "R$1.000,0",                # 1 casa decimal
    "r$ 100,00",                # prefixo minúsculo
    "$100,00",                  # sem o R
    "R$ ,00",                   # sem parte inteira
    "R$ 1.00.000,00",           # agrupamento misto inconsistente
    "R$1_000,00",               # underline
    "R$ 1.000.00,00",           # ponto duplo consecutivo
    "",                         # string vazia
    "R$ 100.00",                # ponto decimal americano sem vírgula
    "R$ 100,",                  # vírgula sem casas decimais
    "R$ .000,00",               # começa com ponto
    "RS 100,00",                # RS em vez de R$
]

# NOME
nome = [
    "João Silva",
    "Maria Aparecida",
    "Pedro",
    "Ana Luíza Ferreira",
    "José Carlos",
    "Fernanda",
    "Antônio Souza",
    "Beatriz Oliveira",
    "Francisco Lima",
    "Cláudia",
    "Sebastião Alves",
    "Mariana",
    "Raimundo Costa",
    "Lúcia Helena",
    "Ângelo",
    "Conceição Pereira",
    "André",
    "Débora Santos",
    "Thiago",
    "Camila Rodrigues",
    "joao silva",               # iniciais minúsculas
    "JOAO SILVA",               # tudo maiúsculo sem letras minúsculas
    "123 Silva",                # começa com número
    "João123",                  # número no meio do nome
    "joão",                     # inicial minúscula
    "@Maria",                   # caractere especial no início
    "Silva-Santos",             # hífen (não suportado)
    "O",                        # inicial maiúscula mas sem sequência de minúsculas (requer 2 ou mais)
    "João_Silva",               # underscore
    "",                         # string vazia
    "  ",                       # só espaços
    "maria",                    # tudo minúsculo
    "MARIA",                    # tudo maiúsculo
    "João2Silva",               # dígito no meio
    "José#Carlos",              # hashtag (não suportado)
    "Ana.Luiza",                # ponto (não suportado)
    "42",                       # só números
    "!Pedro",                   # começa com !
    "SÃo PauLo",                # capitalização inconsistente
    "d'Almeida",                # apóstrofo (não suportado)
]

# EXEMPLO
exemplos = [email, telefone, cpf, data, horario, data_e_horario, url, dinheiro, nome]