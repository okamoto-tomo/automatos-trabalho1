import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from a_leitura import *
from b_extracao import *
from lib.regex_extracao_padroes import *


for arquivo in list(arquivos_do_reginaldo.keys())[:3]:
    print(*extrair_valores(ler_arquivo(arquivo), regex_extracao), sep="\n")