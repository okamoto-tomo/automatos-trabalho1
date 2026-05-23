import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import leitura_e_inspecao
import extracao_de_padroes
import lib.regex_classificacao_padroes


for arquivo in leitura_e_inspecao.arquivos_do_reginaldo.keys():
    print(*extracao_de_padroes.extrair_valores(arquivo, lib.regex_classificacao_padroes.regex), sep="\n")