import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import fundamentus
from datetime import datetime, timedelta
import holidays
import matplotlib.dates as mdates

def obter_dados(ticker):
    # Define a data de término como hoje
    end_date = datetime.today().strftime('%Y-%m-%d')

    # Cria um calendário de feriados no Brasil
    br_holidays = holidays.Brazil()

    # Calcula a data de início considerando 6 dias úteis 
    data_hoje = datetime.today()
    dias_uteis = 0
    while dias_uteis < 6:
        data_hoje -= timedelta(days=1)
        if data_hoje.weekday() < 5 and data_hoje not in br_holidays:
            dias_uteis += 1

    start_date = data_hoje.strftime('%Y-%m-%d')

    # Obter os dados históricos no período especificado
    dados = yf.download(ticker, start=start_date, end=end_date)

    return dados

def risco_retorno(df):
    retorno = df['Adj Close'].pct_change()
    retorno_medio = retorno.mean()*100
    risco = retorno.std()*100
    return risco, retorno_medio

def dados_fundamentalistas(ticker):
    df = fundamentus.get_papel(ticker)
    pl = df['PL'].values[0]
    roe = df['ROE'].values[0]
    roe = roe[:roe.find('%')]
    ultimo_balanco = df['Ult_balanco_processado'].values[0]
    bf = pd.to_datetime(ultimo_balanco).strftime('%d/%m/%Y')
    return df, pl, roe, bf

def gerar_grafico(data, ticker):
    # Gerar gráfico do preço de fechamento
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Adj Close'], marker='o')
    plt.title(f"Preço de Fechamento da {ticker[:ticker.find('.')]}")
    plt.ylabel("Preço (BRL)")
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))  #
    plt.savefig(f'{ticker}.png')

    return
