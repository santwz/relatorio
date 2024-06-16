import subprocess
import os
from analise import obter_dados, risco_retorno, dados_fundamentalistas, gerar_grafico



ticker = "ITUB4.SA" #Basta colocar o código da ação esperada
data = obter_dados(ticker)
risco, retorno_medio = risco_retorno(data)
dtf, pl, roe, bf = dados_fundamentalistas(f'{ticker[:ticker.find('.')]}')
gerar_grafico(data,ticker)


# Conteúdo do documento LaTeX
latex = rf"""
\documentclass{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage{{graphicx}}
\usepackage{{amsmath}}
\usepackage[top=1.55cm, bottom=1.5cm, left=5cm, right=5cm]{{geometry}}


\title{{Relatório de Análise - {ticker[:ticker.find('.')]}}}
\author{{Wallace Santo}}
\date{{\today}}

\begin{{document}}

\maketitle

\section{{Introdução}}
Este relatório apresenta uma análise do papel \textbf{{{ticker[:ticker.find('.')]}}}, incluindo uma avaliação do risco e retorno, além de alguns dados fundamentalistas.

\section{{Gráfico de Preço de Fechamento}}
\begin{{figure}}[h]
    \centering
    \includegraphics[width=\linewidth]{{{ticker}.png}}
    \caption{{Preço de Fechamento da {ticker[:ticker.find('.')]}}}
\end{{figure}}

\section{{Análise de Risco e Retorno}}
O retorno médio da ação nos últimos 5 dias úteis foi de {retorno_medio:.2f}\%, enquanto o risco foi de {risco:.2f}\%.

\section{{Análise fundamentalista}}\

O último balanço registrado foi na data: {bf}\

\begin{{itemize}}
    \item \textbf{{P/L:}} {float(pl)/100}
    \item \textbf{{ROE:}} {roe}\%
\end{{itemize}}



\end{{document}}
"""

latex_file = "relatorio.tex"

with open(latex_file, "w", encoding="utf-8") as file:
    file.write(latex)

subprocess.run(["pdflatex", latex_file])

aux_files = ["relatorio.aux", "relatorio.log", "relatorio.out", f"{ticker}.png"]
for aux_file in aux_files:
    if os.path.exists(aux_file):
        os.remove(aux_file)