# Regex de extração de dados, independente de serem válidos ou não.

regex_extracao = {
    # Captura e-mails com caracteres comuns antes do @, domínio e TLD.
    "email" : (
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"  #([a-zA-Z0-9._%+-]+) O que vem antes do @, com qualquer um desses caracteres.
                                                        #@ literal.
                                                        #([a-zA-Z0-9.-]+) Domínio do e-mail.
                                                        #([a-zA-Z]+) TLD.
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
        r"\d{1,2}[\/._-]\d{1,2}[\/._-]\d{2,4}" #(\d{1,2}) O dia podendo ser qualquer número de um ou dois dígitos.
                                               #/, ., - ou _.
                                               #(\d{2,4}) O ano podendo ser qualquer ano de dois ou quatro dígitos.
    ),

    # Captura os horários, contando os segundos (se tiver).
    "horario": (
        r"\d{1,2}:\d{2}(?::\d{2})?"         #(\d{1,2}) Hora com 1 ou 2 dígitos.
                                            #:, dois pontos.
                                            #(\d{2}) Minuto com dois dígitos.
                                            #((?::\d{2})?) Segundos opcionais.
    ),
    
    # Captura data e horário juntos
    "data_e_horario": (
        r"\d{1,2}[/._-]\d{1,2}[/._-]\d{2,4}\s\d{1,2}:\d{2}(?::\d{2})?"   #(\d{1,2}) Dia, qualquer número, de 1 ou 2 digitos.
                                                                         #(\/._-) Barra literal, ponto, underline ou hífen para separar os números da data.
                                                                         #(\d{1,2}) Mês com 1 ou 2 dígitos
                                                                         #(\d{2,4}) Ano com dois ou quatro dígitos, então captura tanto '24' quanto '2024'
                                                                         #\d{1,2}:\d{2}(?::\d{2})? Hora obrigatória, segundos opcionais.
    ),

    # Captura URL
    "url" :(
        r"(?:https?://)?(?:www\.)?(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/\S*)?" #((?:https?://)?) Protocolo opcional.
                                                                             #((?:www\.)?) www opcional.
                                                                             #((?:[a-zA-Z0-9-]+\.)+) Captura domínio e subdomínio, com letras ou números ou hífens.
                                                                             #([a-zA-Z]{2,}) Captura TLD (Top Level Domain), com duas ou mais letras.
                                                                             #((?:/\S*)?) Path opcional.
    ),

    # Captura dinheiro
    "dinheiro" :(
        r"R\$\s?\d+(?:\.\d{3})*(?:[\.,]\d{2})?" #R$ Obrigatório.
                                                #(\s?) Espaço opcional.
                                                # (\d+) Um ou mais números.
                                                #((?:\.\d{3})*) Para pegar milhares formatados, o * permite isso mais vezes, então abrange tanto 10.000 quanto 1.000.000.
    ),                                          #((?:[\.,]\d{2})?) Centavos opcionais, com ponto ou vírgula.

    # Nome 
    "nome" :(
        r"[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+(?:\s[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+)*"
    ),
}