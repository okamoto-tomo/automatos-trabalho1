import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.regex_classificacao_padroes import *
from lib.regex_exemplos import *
import re

RED     = "\033[31m"
GREEN   = "\033[32m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

for exemplo, tipo in zip(exemplos, regex_classificacao.keys()):
    pattern = regex_classificacao[tipo]
    
    print(f"Expressão regular de {tipo}: {pattern}")

    for string in exemplo:
        if re.fullmatch(pattern, string):
            print(f"{string:<40} {BOLD}{GREEN}✅{RESET}")
        else:
            print(f"{string:<40} {BOLD}{RED}❌{RESET}")
            
    print("\n")