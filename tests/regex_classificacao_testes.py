import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lib.regex_classificacao_padroes
import lib.regex_classificacao_exemplos
import re

RED     = "\033[31m"
GREEN   = "\033[32m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

for exemplo, tipo in zip(lib.regex_classificacao_exemplos.exemplos, lib.regex_classificacao_padroes.regex.keys()):
    pattern = lib.regex_classificacao_padroes.regex[tipo]
    
    print(f"Expressão regular de {tipo}: {pattern}")

    for string in exemplo:
        if re.fullmatch(pattern, string):
            print(f"{string:<40} {BOLD}{GREEN}✅{RESET}")
        else:
            print(f"{string:<40} {BOLD}{RED}❌{RESET}")
            
    print("\n")