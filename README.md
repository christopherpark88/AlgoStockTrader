# AlgoStockTrader
Temporarily storing CSV files on repo

ON FIRST SETUP:
1) run "py -3 -m venv .venv"
2) run ".venv\scripts\activate"
3) Select new python environment (venv)
4) Install pip and then
5) Run "pip install -r requirements.txt" on first setup 


After installing new package, run "pip freeze > requirements.txt"

How to use:

save_sp500_tickers() to get list of s&p500 companies and pickle
get_yahoo_data to get stock ticker data from yahoo api
compile_data to compile data into one dataframe

