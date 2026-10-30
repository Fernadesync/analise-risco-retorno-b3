"""Coleta de preços ajustados da B3 via yfinance."""
from pathlib import Path
import pandas as pd
import yfinance as yf

# Ações escolhidas por setor (sufixo .SA = B3)
ACOES = {
    "ITUB4.SA": "Banco",
    "BBDC4.SA": "Banco",
    "PETR4.SA": "Petróleo",
    "VALE3.SA": "Mineração",
    "WEGE3.SA": "Indústria",
    "EGIE3.SA": "Energia",
    "LREN3.SA": "Varejo",
    "ABEV3.SA": "Consumo",
}
BENCHMARK = "^BVSP"  # Ibovespa

RAIZ = Path(__file__).resolve().parent.parent
PASTA_RAW = RAIZ / "data" / "raw"

def baixar_precos(tickers, inicio, fim, salvar_em=None):
    """Baixa preços de fechamento ajustados (dividendos e desdobramentos).

    Retorna um DataFrame com data no índice e um ticker por coluna.
    """
    dados = yf.download(
        list(tickers), start=inicio, end=fim, auto_adjust=True, progress=False
    )
    precos = dados["Close"].copy()
    precos.index = pd.to_datetime(precos.index)
    precos = precos.sort_index()

    if salvar_em is not None:
        salvar_em = Path(salvar_em)
        salvar_em.parent.mkdir(parents=True, exist_ok=True)
        precos.to_csv(salvar_em)
    return precos

def baixar_tudo(inicio, fim):
    """Baixa as ações e o Ibovespa e salva em data/raw/."""
    acoes = baixar_precos(ACOES.keys(), inicio, fim, PASTA_RAW / "acoes.csv")
    ibov = baixar_precos([BENCHMARK], inicio, fim, PASTA_RAW / "ibovespa.csv")
    return acoes, ibov


if __name__ == "__main__":
    acoes, ibov = baixar_tudo("2021-10-29", "2026-10-28")
    print(acoes.tail())
