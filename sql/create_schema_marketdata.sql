CREATE SCHEMA market_data
    CREATE TABLE hist_alpaca (
        ticker text
    )
    CREATE TABLE hist_yahoo_finance (
        ticker text, 
        date timestamp, 
        open numeric, 
        high numeric, 
        low numeric, 
        close numeric, 
        adj_close numeric, 
        volume numeric
    )
    CREATE TABLE real_alpaca (
        ticker text
    )
    CREATE TABLE real_tdameritrade (
        ticker text
    )
;
