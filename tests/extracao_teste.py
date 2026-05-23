import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import a_leitura
import b_extracao
import lib.regex_classificacao_padroes


for arquivo in a_leitura.arquivos_do_reginaldo.keys():
    print(*b_extracao.extrair_valores(arquivo, lib.regex_classificacao_padroes.regex), sep="\n")