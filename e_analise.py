'''
e) Análise quantitativa. 
O sistema deve produzir estatísticas sobre os dados extraídos, incluindo, no mínimo: 
quantidade total de ocorrências por tipo; quantidade de ocorrências válidas e 
inválidas por tipo; distribuição das ocorrências entre os arquivos.
'''

import json
import os
import sys
from datetime import datetime
import pandas as pd


LINHA = "=" * 72


def carregar_df(json_path=None):
    if not json_path or not os.path.isfile(json_path):
        print("[ERRO] Arquivo não informado ou não encontrado.")
        return None

    with open(json_path, 'r', encoding="utf-8") as f:
        raw = json.load(f)

    if isinstance(raw, list):
        dados = raw
    else:
        dados = None
        for v in raw.values():
            if isinstance(v, list):
                dados = v
                break

    if not dados:
        print("[ERRO] Nenhuma lista encontrada no JSON.")
        return None

    primeiro = dados[0]

    linhas = []

    # estrutura do CSV (tem 'matches')
    if "matches" in primeiro:
        for registro in dados:
            for tipo, conteudo in registro["matches"].items():
                linha = {
                    "id":            registro["id"],
                    "tipo":          tipo,
                    "valor":         conteudo["valor"],
                    "classificacao": conteudo["classificacao"],
                    "validade":      registro["validade"],
                    "arquivo_origem": registro["arquivo_origem"],
                }
                linhas.append(linha)

    # estrutura geral (tem 'tipo' e 'classificacao' direto)
    elif "tipo" in primeiro and "classificacao" in primeiro:
        linhas = dados

    else:
        print(f"[ERRO] Estrutura do JSON não reconhecida. Chaves: {list(primeiro.keys())}")
        return None

    print(f"JSON carregado: {json_path} ({len(dados)} registros, {len(linhas)} ocorrências)")
    return pd.DataFrame(linhas)


def analisar(json_path=None):
    df = carregar_df(json_path)
    if df is None:
        return

    df["classificacao"] = df["classificacao"].str.lower().str.strip()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    relatorio = LINHA + "\n"
    relatorio += "  ANÁLISE QUANTITATIVA\n"
    relatorio += f"  Gerado em: {ts}\n"

    # e.1 - total por tipo
    relatorio += f"\n{LINHA}\n  e.1  Quantidade total de ocorrências por tipo de padrão\n{LINHA}\n"
    e1 = df.groupby("tipo").size().reset_index(name="total").sort_values("tipo")
    relatorio += e1.to_string(index=False)

    # e.2 - validos e invalidos por tipo
    relatorio += f"\n{LINHA}\n  e.2  Ocorrências válidas e inválidas por tipo\n{LINHA}\n"
    e2 = df.groupby(["tipo", "classificacao"]).size().unstack(fill_value=0)
    e2 = e2.reindex(columns=["valido", "invalido"], fill_value=0)
    e2["total"] = e2["valido"] + e2["invalido"]
    e2["% válido"]   = (e2["valido"]   / e2["total"] * 100).round(1).astype(str) + "%"
    e2["% inválido"] = (e2["invalido"] / e2["total"] * 100).round(1).astype(str) + "%"
    relatorio += e2[["valido", "% válido", "invalido", "% inválido", "total"]].to_string()

    # e.3 - distribuicao por arquivo
    relatorio += f"\n{LINHA}\n  e.3  Distribuição das ocorrências entre os arquivos\n{LINHA}\n"
    e3 = df.groupby(["arquivo_origem", "tipo"]).size().unstack(fill_value=0)
    e3["TOTAL"] = e3.sum(axis=1)
    relatorio += e3.to_string()

    # e.4 - classificacao por arquivo
    relatorio += f"\n{LINHA}\n  e.4  Classificação (válido / inválido) por arquivo\n{LINHA}\n"
    e4 = df.groupby(["arquivo_origem", "classificacao"]).size().unstack(fill_value=0)
    e4 = e4.reindex(columns=["valido", "invalido"], fill_value=0)
    e4["total"] = e4["valido"] + e4["invalido"]
    e4["% válido"]   = (e4["valido"]   / e4["total"] * 100).round(1).astype(str) + "%"
    e4["% inválido"] = (e4["invalido"] / e4["total"] * 100).round(1).astype(str) + "%"
    relatorio += e4[["valido", "% válido", "invalido", "% inválido", "total"]].to_string()

    # e.5 - resumo
    relatorio += f"\n{LINHA}\n  e.5  Resumo executivo\n{LINHA}\n"

    total_geral  = len(df)
    total_valido = (df["classificacao"] == "valido").sum()
    total_inv    = total_geral - total_valido
    tipo_top     = e1.loc[e1["total"].idxmax(), "tipo"]
    arq_top      = e3["TOTAL"].idxmax()

    relatorio += f"\n  Total de ocorrências processadas : {total_geral}"
    relatorio += f"\n  Total válidas                    : {total_valido}  ({round(total_valido/total_geral*100,1)}%)"
    relatorio += f"\n  Total inválidas                  : {total_inv}  ({round(total_inv/total_geral*100,1)}%)"
    relatorio += f"\n\n  Tipo mais frequente              : {tipo_top} ({e1.set_index('tipo').loc[tipo_top,'total']} ocorrências)"
    relatorio += f"\n  Arquivo com mais ocorrências     : {arq_top} ({int(e3.loc[arq_top,'TOTAL'])} ocorrências)"
    relatorio += f"\n  Tipos analisados                 : {df['tipo'].nunique()}"
    relatorio += f"\n  Arquivos analisados              : {df['arquivo_origem'].nunique()}\n"
    relatorio += LINHA

    print(relatorio)

    # exporta json com as estatísticas
    stats = {
        "metadados":                  {"gerado_em": ts, "total_registros": total_geral},
        "total_por_tipo":             e1.set_index("tipo")["total"].to_dict(),
        "validos_invalidos_por_tipo": e2.to_dict(orient="index"),
        "distribuicao_por_arquivo":   e3.to_dict(orient="index"),
        "classificacao_por_arquivo":  e4.to_dict(orient="index"),
        "resumo": {
            "total_geral":              total_geral,
            "total_valido":             int(total_valido),
            "total_invalido":           int(total_inv),
            "pct_valido":               round(total_valido / total_geral * 100, 1),
            "pct_invalido":             round(total_inv    / total_geral * 100, 1),
            "tipo_mais_frequente":      tipo_top,
            "arquivo_mais_ocorrencias": arq_top,
        },
    }

    with open(f"relatorio/resultados_quantitativos_{json_path.replace(".json", "")}.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2, default=str)
    print("Exportado resultados_quantitativos.json")

    with open(f"relatorio/relatorio_quantitativo_{json_path.replace(".json", "")}.txt", "w", encoding="utf-8") as f:
        f.write(relatorio)
    print("Exportado relatorio_quantitativo.txt")

    return stats


if __name__ == "__main__":
    if len(sys.argv) > 1:
        analisar(sys.argv[1])
    else:
        analisar(None)