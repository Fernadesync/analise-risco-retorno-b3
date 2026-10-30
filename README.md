# analise-risco-retorno-b3

Análise de Risco e Retorno de Ações da B3

Estudo analítico, feito em Python, sobre o comportamento de risco e retorno de ações brasileiras de setores diferentes, comparadas ao Ibovespa.

Status: em desenvolvimento. Etapa concluída: coleta de dados. Próximas: retornos e risco, beta e Sharpe, dashboard no Power BI.

Pergunta central

Como ações de setores diferentes da B3 se comportam em termos de risco e retorno, e a diversificação reduz o risco de uma carteira em relação a cada ativo isolado?

Dados
Fonte: Yahoo Finance, via biblioteca yfinance.
Período: 29/10/2021 a 28/10/2026 (cerca de 5 anos de pregões).
Preços: fechamento ajustado por dividendos e desdobramentos (auto_adjust=True).
Benchmark: Ibovespa (^BVSP).
Ticker	Setor
ITUB4	Banco
BBDC4	Banco
PETR4	Petróleo
VALE3	Mineração
WEGE3	Indústria
EGIE3	Energia
LREN3	Varejo
ABEV3	Consumo

Metodologia :
Coleta e limpeza: download dos preços ajustados, checagem de valores faltantes e alinhamento das datas com o Ibovespa.
Retornos diários: cálculo do retorno simples (e log-retorno, quando útil).
Estatística descritiva do risco: retorno médio, volatilidade (anualizada), assimetria, curtose, distribuição dos retornos e testes de normalidade.
Correlação entre os ativos e drawdown máximo.
Comparação com o Ibovespa: retorno acumulado, beta (regressão linear) e índice de Sharpe.
Carteira diversificada: comparação entre o risco da carteira com pesos iguais e o risco dos ativos individuais.
Dashboard no Power BI com as principais conclusões.

Resultados :
Em construção. Esta seção será preenchida com gráficos e conclusões ao final de cada etapa.

Limitações :
Período de cerca de 5 anos, que não cobre todos os ciclos de mercado.
Desempenho passado não garante desempenho futuro.
Retornos financeiros costumam ter caudas pesadas e não seguir a distribuição normal.
Custos de transação, impostos e taxas não foram considerados.
Amostra pequena de ações (8), com viés de escolha.

Estrutura do projeto:
analise-risco-retorno-b3/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── raw/            # CSVs baixados (não versionados)
├── notebooks/          # análises, numeradas na ordem de leitura
└── src/
    └── coleta.py       # download dos preços com yfinance

Como reproduzir
Clone o repositório:
bash
   git clone https://github.com/Fernadesync/analise-risco-retorno-b3.git
   cd analise-risco-retorno-b3
(Recomendado) Crie e ative um ambiente virtual:
bash
   python -m venv .venv
   source .venv/bin/activate   # no Windows: .venv\Scripts\activate
Instale as dependências:
bash
   pip install -r requirements.txt
Baixe os dados (a pasta data/raw/ é criada automaticamente):
bash
   python src/coleta.py
Tecnologias

Python, pandas, numpy, yfinance, matplotlib/seaborn, statsmodels, Power BI.

Aviso

Este projeto é um estudo analítico e educacional. Nada aqui constitui recomendação de investimento.

Autor

Feito por [José Fernandes Da Silva Filho] como parte da minha trajetória em Estatística e Ciência de Dados.

LinkedIn : https://www.linkedin.com/in/jos%C3%A9-fernandes-da-silva-filho-5052232a6/
 
GitHub : https://github.com/Fernadesync 