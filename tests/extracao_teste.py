import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import a_leitura
import b_extracao
import lib.regex_classificacao_padroes


for arquivo in list(a_leitura.arquivos_do_reginaldo.keys())[:3]:
    print(*b_extracao.extrair_valores(a_leitura.ler_arquivo(arquivo), lib.regex_classificacao_padroes.regex), sep="\n")