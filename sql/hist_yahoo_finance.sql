-- current table for historical yahoo finance data
CREATE TABLE market_data.hist_yahoo_finance (
    ticker text, 
    date timestamp,
    open numeric, 
    high numeric, 
    low numeric, 
    close numeric, 
    adj_close numeric, 
    volume numeric
);
