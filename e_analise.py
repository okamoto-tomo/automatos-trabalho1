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


SEP = "=" * 72


# carregamento dps arquivos
def carregar_df(json_path=None):
    if json_path and os.path.isfile(json_path):
        with open(json_path, 'r', encoding="utf-8") as f:
            raw = json.load(f)
            
        dados = raw if isinstance(raw, list) else next(
            (v for v in raw.values() if isinstance(v, list)), None)
        
        if dados:
            print(f" JSON carregado: {json_path} ({len(dados)} registros)")
            return pd.DataFrame(dados)

    print("[ERRO] Arquivo não informado ou não encontrado.")
    return None


def analisar(json_path=None):
    df = carregar_df(json_path)
    if df is None:
        return 
    
    df["classificacao"] = df["classificacao"].str.lower().str.strip()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    blocos = []

    def secao(titulo):
        blocos.append(f"\n{SEP}\n  {titulo}\n{SEP}")

    # e.1 – tipo
    secao("e.1  Quantidade total de ocorrências por tipo de padrão")
    e1 = df.groupby("tipo").size().reset_index(name="total").sort_values("tipo")
    blocos.append(e1.to_string(index=False))

    # e.2 – validados e invalidos 
    secao("e.2  Ocorrências válidas e inválidas por tipo")
    e2 = (df.groupby(["tipo", "classificacao"])
            .size()
            .unstack(fill_value=0)
            .reindex(columns=["valido", "invalido"], fill_value=0))
    e2["total"] = e2.sum(axis=1)
    e2["% válido"]   = (e2["valido"]   / e2["total"] * 100).round(1).astype(str) + "%"
    e2["% inválido"] = (e2["invalido"] / e2["total"] * 100).round(1).astype(str) + "%"
    blocos.append(e2[["valido", "% válido", "invalido", "% inválido", "total"]].to_string())

    # e.3 distribuicao dos arquivos
    secao("e.3  Distribuição das ocorrências entre os arquivos")
    e3 = (df.groupby(["arquivo_origem", "tipo"])
            .size()
            .unstack(fill_value=0))
    e3["TOTAL"] = e3.sum(axis=1)
    blocos.append(e3.to_string())

    # e.4  classificacao por arquivo
    secao("e.4  Classificação (válido / inválido) por arquivo")
    e4 = (df.groupby(["arquivo_origem", "classificacao"])
            .size()
            .unstack(fill_value=0)
            .reindex(columns=["valido", "invalido"], fill_value=0))
    e4["total"] = e4.sum(axis=1)
    e4["% válido"]   = (e4["valido"]   / e4["total"] * 100).round(1).astype(str) + "%"
    e4["% inválido"] = (e4["invalido"] / e4["total"] * 100).round(1).astype(str) + "%"
    blocos.append(e4[["valido", "% válido", "invalido", "% inválido", "total"]].to_string())

    # e.5 resumo executivo
    secao("e.5  Resumo executivo")
    total_geral  = len(df)
    total_valido = (df["classificacao"] == "valido").sum()
    total_inv    = total_geral - total_valido
    tipo_top     = e1.loc[e1["total"].idxmax(), "tipo"]
    arq_top      = e3["TOTAL"].idxmax()

    resumo = (
        f"\n  Total de ocorrências processadas : {total_geral}"
        f"\n  Total válidas                    : {total_valido}  ({round(total_valido/total_geral*100,1)}%)"
        f"\n  Total inválidas                  : {total_inv}  ({round(total_inv/total_geral*100,1)}%)"
        f"\n\n  Tipo mais frequente              : {tipo_top} ({e1.set_index('tipo').loc[tipo_top,'total']} ocorrências)"
        f"\n  Arquivo com mais ocorrências     : {arq_top} ({int(e3.loc[arq_top,'TOTAL'])} ocorrências)"
        f"\n  Tipos analisados                 : {df['tipo'].nunique()}"
        f"\n  Arquivos analisados              : {df["arquivo_origem"].nunique()}\n"
    )
    blocos.append(resumo)
    blocos.append(SEP)

    relatorio = f"{SEP}\n  ANÁLISE QUANTITATIVA\n" \
                f"  Gerado em: {ts}\n" + "\n".join(blocos)

    print(relatorio)

    # exportacoes
    stats = {
        "metadados":                 {"gerado_em": ts, "total_registros": total_geral},
        "total_por_tipo":            e1.set_index("tipo")["total"].to_dict(),
        "validos_invalidos_por_tipo": e2.to_dict(orient="index"),
        "distribuicao_por_arquivo":  e3.to_dict(orient="index"),
        "classificacao_por_arquivo": e4.to_dict(orient="index"),
        "resumo": {
            "total_geral": total_geral, "total_valido": int(total_valido),
            "total_invalido": int(total_inv),
            "pct_valido":   round(total_valido / total_geral * 100, 1),
            "pct_invalido": round(total_inv    / total_geral * 100, 1),
            "tipo_mais_frequente":        tipo_top,
            "arquivo_mais_ocorrencias":   arq_top,
        },
    }

    with open("resultados_quantitativos.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2, default=str)
    print("Exportado resultados_quantitativos.json")

    with open("relatorio_quantitativo.txt", "w", encoding="utf-8") as f:
        f.write(relatorio)
    print("Exportado relatorio_quantitativo.txt")

    return stats


if __name__ == "__main__":
    analisar(sys.argv[1] if len(sys.argv) > 1 else None)
