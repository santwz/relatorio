# Análise de Ações com Python

Este projeto, que ainda está em desenvolvimento, visa gerar um relatório automatizado de ações da B3. Algumas das motivações para usar o ambiente LaTeX foi:

1. Estética e formatação consistente
2. Flexibilidade e personalização
3. Facilidade na manutenção do código

## Funcionalidades

1. **Obtenção de Dados Históricos**: Utiliza a biblioteca `yfinance` para baixar os dados históricos de uma ação especificada.
2. **Cálculo de Risco e Retorno**: Calcula o risco (desvio padrão dos retornos) e o retorno médio da ação nos últimos 5 dias úteis.
3. **Dados Fundamentalistas**: Obtém dados fundamentalistas como P/L (Preço sobre Lucro) e ROE (Retorno sobre Patrimônio Líquido) da empresa utilizando a biblioteca `fundamentus`.
4. **Geração de Gráfico**: Cria um gráfico do preço de fechamento ajustado da ação nos últimos 5 dias úteis.
5. **Geração de Relatório LaTeX**: Gera um relatório em formato LaTeX contendo todas as análises realizadas, incluindo o gráfico gerado.

## Pré-requisitos

- Python 3.7+
- Bibliotecas Python: `yfinance`, `matplotlib`, `pandas`, `fundamentus`, `holidays`
- Distribuição LaTeX para geração do relatório PDF

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/santwz/relatorio_acao.git
    cd relatorio_acao
    ```

2. Instale as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```

3. Certifique-se de ter uma distribuição LaTeX instalada em seu sistema para gerar o relatório PDF.
    ``` bash
    https://miktex.org/
    ```

## Uso

1. Edite o arquivo `analise.py` para especificar o ticker da ação desejada:
    ```python
    ticker = "ITUB4.SA"  # Código da ação a ser analisada
    ```

2. Execute o script:
    ```bash
    python analise.py
    ```

3. O relatório em formato PDF será gerado no diretório atual com o nome `relatorio.pdf`.

## Funções

### obter_dados(ticker)

Obtém os dados históricos de preços da ação especificada nos últimos 5 dias úteis.

**Parâmetros:**
- `ticker`: Código da ação (ex: "ITUB4.SA")

**Retorno:**
- DataFrame com os dados históricos de preços.

### risco_retorno(df)

Calcula o risco (desvio padrão dos retornos) e o retorno médio da ação.

**Parâmetros:**
- `df`: DataFrame com os dados históricos de preços.

**Retorno:**
- `risco`: Risco da ação em porcentagem.
- `retorno_medio`: Retorno médio da ação em porcentagem.

### dados_fundamentalistas(ticker)

Obtém dados fundamentalistas da empresa, como P/L e ROE.

**Parâmetros:**
- `ticker`: Código da ação (ex: "ITUB4")

**Retorno:**
- `df`: DataFrame com os dados fundamentalistas.
- `pl`: P/L da empresa.
- `roe`: ROE da empresa.
- `bf`: Data do último balanço processado.

### gerar_grafico(data, ticker)

Gera um gráfico do preço de fechamento ajustado da ação e salva como PNG.

**Parâmetros:**
- `data`: DataFrame com os dados históricos de preços.
- `ticker`: Código da ação.

## Considerações futuras

Refinar as análises, adicionar matriz de correlação, ver como a ação se comporta em relação ao IBOV.

Sinta-se à vontade para contribuir ou abrir issues para melhorias e correções.
