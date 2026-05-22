'''
 Implemente expressões regulares para identificar e extrair, no mínimo, os seguintes padrões:
   1. e-mail                        (https://support.google.com/mail/answer/9211434)
   2. telefone                      (https://teleco.com.br/num_cel.asp)                          
   3. CPF                           (https://en.wikipedia.org/wiki/CPF_number)
   4. data                          (https://funesa.se.gov.br/wp-content/uploads/2022/10/ABNT-NBR-5892-Representacao-e-formato-de-tempo-Datas-e-Horas.pdf)
   5. horário                       (https://funesa.se.gov.br/wp-content/uploads/2022/10/ABNT-NBR-5892-Representacao-e-formato-de-tempo-Datas-e-Horas.pdf)
   6. data e horário combinado      (https://funesa.se.gov.br/wp-content/uploads/2022/10/ABNT-NBR-5892-Representacao-e-formato-de-tempo-Datas-e-Horas.pdf)
   7. URL                           (https://datatracker.ietf.org/doc/html/rfc1738)
   8. valor monetário em reais      (https://www.planalto.gov.br/ccivil_03/mpv/1990-1995/542.htm)
   9. nome próprio                  (https://funag.gov.br/manual/index.php?title=Mai%C3%BAsculas_e_min%C3%BAsculas)
   (definir critérios e justificar)'''

regex = {
    "email": (
        r"(?=[a-z0-9\.]{6,30}@)"            # Lookahead necessário para contar o tamanho do local (mínimo 6, máximo 30 char).
        r"[a-z0-9]"                         # Começa com letra minúscula ou número
        r"([a-z0-9]|\.[a-z0-9])*"           # Evita pontos seguidos (ex: joao..1@gmail.com é inválido)
        r"@"                                # Arroba
        r"([a-z0-9]{2,}\.)+"                # Mínimo de 2 caracteres alfanuméricos seguido de um ponto, no mínimo uma ocorrência disso
        r"[a-z]{2,}"                        # Top-level domain, no mínimo duas letras minúsculas no final do email
    ),
    
    "telefone": (
        r"(\d{2}|\(\d{2}\)|\d{2}\s|\(\d{2}\)\s)?"   # DDD: XX ou (XX) opcional, separado opcionalmente por espaço
        r"9\d{4}"                                   # 9 + primeiros 4 dígitos do número
        r"-?"                                       # Hífen opcional
        r"\d{4}"                                    # Últimos 4 dígitos do número
    ),
    
    "cpf": (
        r"\d{3}\.\d{3}\.\d{3}-\d{2}"        # CPF com ponto e hífen
    ),
    
    "data": (
        r"(0[1-9]|[1-2]\d|3[0-1])"          # Dia
        r"/"                                # Barra
        r"(0[1-9]|1[0-2])"                  # Mês
        r"/"                                # Barra
        r"([1-9]\d{3})"                     # Ano
    ),
    
    "horario": (
        r"([0-1]\d|2[0-3])"                 # Hora
        r":"                                # Dois pontos
        r"[0-5]\d"                          # Minuto
        r":"                                # Dois pontos
        r"[0-5]\d"                          # Segundo
    ),
    
    "data_e_horario": (
        r"(0[1-9]|[1-2]\d|3[0-1])"          # Dia
        r"/"                                # Barra
        r"(0[1-9]|1[0-2])"                  # Mês
        r"/"                                # Barra
        r"([1-9]\d{3})"                     # Ano
        r"\s"                               # Espaço
        r"([0-1]\d|2[0-3])"                 # Hora
        r":"                                # Dois pontos
        r"[0-5]\d"                          # Minuto
        r":"                                # Dois pontos
        r"[0-5]\d"                          # Segundo
    ),
    
    "url": (
        r"(https?://)?"                     # Protocolo HTTP ou HTTPS opcional
        r"(www\.)?"                         # World Wide Web opcional
        r"([a-z0-9]{2,}\.)+"                # Mínimo de 2 caracteres alfanuméricos seguido de um ponto, no mínimo uma ocorrência disso
        r"[a-z]{2,}"                        # Top-level domain, no mínimo duas letras minúsculas no final do URL
        r"(/.*)?"                           # Barra seguido de qualquer coisa de qualquer tamanho, opcional
    ),
    
    "dinheiro": (
        r"R\$"                              # Real cifrão com espaço opcional
        r"\s?"                              # Espaço opcional
        r"((\d{1,3}(\.\d{3})*)"             # 1 a 3 dígitos seguido de zero ou mais ponto com 3 dígitos
        r"|"                                # OU
        r"(\d+))"                           # 1 ou mais dígitos
        r"(,\d{2})?"                        # Vírgula com 2 dígitos, opcional
    ),
    
    "nome": (
        r"[A-ZÁÉÍÓÚÂÊÎÔÛ]"                              # Inicial maiúscula
        r"[a-záéíóúâêîôûãõç]+"                          # Um ou mais letras, inclui diacríticos da língua portuguesa
        r"(?:\s[A-ZÁÉÍÓÚÂÊÎÔÛ][a-záéíóúâêîôûãõç]+)*"    # Outros nomes
    ),
}

'''
Observação 1:
O uso de lookahead no padrão do email foge de Linguagem Tipo 3 pelo uso de memória.
Em específico, o regex ([a-z0-9]|\.[a-z0-9]) alterna entre uma string de tamanho 1
e outra string de tamanho 2. A notação {m,n} faz contagem de grupos de símbolos e
não de símbolos em si. Sem o uso de lookahead, seria necessário fazer um caso para
cada posição de ponto possível, o que explodiria pela natureza combinacional do 
problema e não seria prático aplicar o regex.

Exemplo:
([a-z0-9]|\.[a-z0-9]){5,} não aceita j.oao
(?=[a-z0-9\.]{5,})([a-z0-9]|\.[a-z0-9])* aceita j.oao



Observação 2:
Sem formatação, é ambíguo extrair telefone e CPF por ambos poderem possuir 11 dígitos.
Dessa forma, decidiu-se que o CPF deve obrigatoriamente estar formatado, enquanto que
a formatação do telefone é opcional.
'''