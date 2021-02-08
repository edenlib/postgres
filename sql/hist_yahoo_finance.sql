-- current table for historical yahoo finance data
DROP TABLE IF EXISTS market_data.hist_yahoo_finance;
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
