# automatos-trabalho1

Usa regex para extrair e classificar dados de arquivos bagunçados e/ou sujos, gerando relatórios e estatísticas quantitativas sobre as ocorrências encontradas.

## Requisitos

- Python 3.x
- pip
- Pandas 3.0.3

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/automatos-trabalho1.git
cd automatos-trabalho1
pip install -r requirements.txt
```

## Como usar

```bash
python main.py
```

O programa vai processar os arquivos automaticamente e gerar os seguintes arquivos de saída:

```
arquivos_json/
├── dados_csv.json
└── dados_gerais.json

lib/
├── relatorio_quantitativo_dados_csv.txt
├── relatorio_quantitativo_dados_gerais.txt
├── resultados_quantitativos_dados_csv.json
└── resultados_quantitativos_dados_gerais.json
```