# AlgoStockTrader
Temporarily storing CSV files on repo

# ON FIRST SETUP WINDOWS (cmd shell):
1) run "py -3 -m venv .venv"
2) run ".venv\scripts\activate"
3) Select new python environment (venv)
4) Install pip if missing and then
5) Run "pip install -r requirements.txt" on first setup 
6) After installing new package, run "pip freeze > requirements.txt"

# ON FIRST SETUP MAC (bash/zsh shell):
1) You may need to run sudo apt-get install python3-venv first
    run "python3 -m venv .venv"
2) source .venv/bin/activate
3) Select new python environment (venv)
4) Install pip if missing and then
5) Run "pip install -r requirements.txt" on first setup 
6) After installing new package, run "pip freeze > requirements.txt"

# How to use:

save_sp500_tickers() to get list of s&p500 companies and pickle
get_yahoo_data to get stock ticker data from yahoo api
compile_data to compile data into one dataframe

