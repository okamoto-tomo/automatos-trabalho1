'''
 Implemente expressões regulares para identificar e extrair, no mínimo, os seguintes padrões: () 
   1. e-mails, 
   2. telefones, 
   3. CPFs, 
   4. datas,
   5. horários
   6. datas e horários combinados, 
   7. URLs, 
   8. valores monetários em reais, 
   9. nomes próprios 
   (definir critérios e justificar)'''

import re

regex = {
    email: (
        r"[a-z0-9_]"                        # Começa com letra minúscula + número + underline, mínimo 1 caractere
        r"( [a-z0-9_] | (\.[a-z0-9_]) )*"   # Evita pontos seguidos (ex: joao..1@gmail.com é inválido)
        r"@"                                # Arroba
        r"([a-z0-9]{2,}\.)+"                # Mínimo de 2 caracteres alfanuméricos seguido de um ponto, no mínimo uma ocorrência disso
        r"[a-z]{2,}"                        # Top-level domain, no mínimo duas letras minúsculas no final do email
    ),
    
    telefone: (
        r"( (\d{2}) | (\(\d{2}\)) )"        # DDD: XX ou (XX)
        r"\s?"                              # Espaço opcional entre DDD e telefone
        r"\d{5}"                            # Primeiros 5 dígitos do número
        r"-?"                               # Hífen opcional
        r"\d{4}"                            # Últimos 4 dígitos do número
    ),
    
    cpf: (
        r"((\d{3}\.){2}\d{3}-\d{2}"         # CPF com ponto e hífen
        r"|"                                # OU
        r"(\d{11}))"                        # CPF sem ponto e hífen
    ),
    
    data: (
        r"\d{2}/\d{2}/"                     # Dia/mês/
        r"((\d{2})|(\d}{4}))"               # Dois ou quatro dígitos do ano (DD/MM/AA ou DD/MM/AAAA)
    ),
    
    horario: (
        r"\d{2}:\d{2}:\d{2}"                # Hora:minuto:segundo (HH:MM:SS)
    ),
    
    data_e_horario: (
        r"\d{2}/\d{2}/"                     # Dia/mês/
        r"((\d{2})|(\d}{4}))"               # Dois ou quatro dígitos do ano (DD/MM/AA ou DD/MM/AAAA)
        r"\d{2}:\d{2}:\d{2}"                # Hora:minuto:segundo (HH:MM:SS)
    ),
    
    url: (
        r"(https?://)?"                     # Protocolo HTTP ou HTTPS opcional
        r"(www\.)?"                         # World Wide Web opcional
        r"([a-z0-9]{2,}\.)+"                # Mínimo de 2 caracteres alfanuméricos seguido de um ponto, no mínimo uma ocorrência disso
        r"[a-z]{2,}"                        # Top-level domain, no mínimo duas letras minúsculas no final do URL
        r"(/.*)?"                           # Barra seguido de qualquer coisa de qualquer tamanho, opcional
    ),
    
    dinheiro: (
        r"R$(\s)?"                          # Real cifrão com espaço opcional
        r"( \d{1,3}(\.\d{3})*)"             # 1 a 3 dígitos seguido de zero ou mais ponto com 3 dígitos
        r"|"                                # OU
        r"(\d+) )"                          # 1 ou mais dígitos
        r"(,\d{2})?"                        # Vírgula com 2 dígitos, opcional
    ),
    
    nome: (
        r"([A-Z ÁÉÍÓÚ ÂÊÎÔÛ ÃÕ][a-z áéíóú âêîôû ãõ ç]+)+"    # Um ou mais palavras capitalizadas, inclui diacríticos da língua portuguesa
    ),
}