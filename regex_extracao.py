import re


# Regex de extração de dados, independente de serem válidos ou não.

regex = {
    # Qualquer coisa + @ + qualquer coisa
    "email" : (
        r"\S+@\S+"   #(\S) Pega qualquer coisa que não seja espaço, (@) arroba, ()\Squalquer coisa que não seja espaço.
    ),

    # Captura todos os números de telefone, estejam ou não com DDD. Logo, busca números com 8, 9 e 11 dígitos.
    "telefone": (
        r"(?:\(?\d{2}\)?\s?)?9?\d{4}-?\d{4}" #(\(?) Parênteses opcional, a ideia é pegar todos os números, estejam com parenteses ou não.
                                             #(\d{2}) DDD: Qualquer número, duas vezes.
                                             #(\s?) Espaço opcional.
                                             #(9?) Opcional
                                             #(\d{4}) Quatro números. Ocorre duas vezes pra formar os 8 números.
                                             #(-?) Hífen opcional

    ),

    # CPF (11 dígitos) com ponto, hífen ou espaços opcionais.
    "cpf": (
        r"\d{3}[.\s-]?\d{3}[.\s-]?\d{3}[-\s]?\d{2}" #(\d{3}) Três números.
                                                    #([.\s-]?) Ponto ou espaço ou hífen opcionais.
    ),

    # Captura todas as datas possíveis.
    "data": (
        r"\d{1,2}/\d{1,2}/\d{2,4}" #(\d{1,2}) O dia podendo ser qualquer número de um ou dois dígitos.
                                   #/ barra
                                   #(\d{2,4}) O ano podendo ser qualquer ano de dois ou quatro dígitos.
    ),

    # Captura os horários, contandos os segundos (se tiver)
    "horario": (
        r"\d{1,2}:\d{2}(?::\d{2})?"
    ),
    
    # Captura data e horário juntos
    "data_e_horario": (
        r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\s\d{1,2}:\d{2}(?::\d{2})?" #(\d{1,2}) Qualquer número, de 1 ou 2 digitos.
                                                                   #([/-]) Barra ou traço, então pode aceitar datas como 01/01/2121 ou 01-01-2121.
                                                                   #(\d{2,4}) Ano com dois ou quatro dígitos.
                                                                   #\d{1,2}:\d{2}(?::\d{2})? Hora obrigatória, segundos opcionais.
    ),

    # Captura URL
    "url" :(
        r"(?:https?://)?(?:www\.)?\S+\.\S+(?:/\S*)?" #((?:https?://)?) Protocolo opcional.
                                                     #((?:www\.)?) www opcional.
                                                     #(\.) Ponto literal
                                                     #(\S+) Qualquer coisa que não seja espaço.
                                                     #(\S+\.\S+) Domínio.
                                                     #((?:/\S*)?) Path.
    ),

    # Captura dinheiro
    "dinheiro" :(
        r"(?:R\$\s?)?\d+(?:[\.,]\d+)*" #((?:R\$\s?)?) Talvez tenha R$ e espaço.
                                       # (\d+) Um ou mais números.
                                       #((?:[\.,]\d+)*) Pode ter ".", "," com números após, quantas vezes quiser.
    ),

    # Nome 
    "nome" :(
        r"[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+(?:\s[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+)+"
    ),
}