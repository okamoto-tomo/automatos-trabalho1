import lib.regex_patterns
import lib.regex_examples
import re

RED     = "\033[31m"
GREEN   = "\033[32m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

for exemplo, campo in zip(lib.regex_examples.exemplos, lib.regex_patterns.regex.keys()):
    pattern = lib.regex_patterns.regex[campo]
    
    print(f"Expressão regular de {campo}: {pattern}")

    for string in exemplo:
        if re.fullmatch(pattern, string):
            print(f"{string:<40} {BOLD}{GREEN}✅{RESET}")
        else:
            print(f"{string:<40} {BOLD}{RED}❌{RESET}")
            
    print("\n")