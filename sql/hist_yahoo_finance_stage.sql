-- staging table for the latest copy of historical finance data
CREATE TABLE market_data.hist_yahoo_finance_stage (LIKE market_data.hist_yahoo_finance);
