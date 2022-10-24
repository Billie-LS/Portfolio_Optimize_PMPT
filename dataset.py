import os
import numpy as np
import pandas as pd
import yfinance as yf

from pandas_datareader import data as pdr
from sqlalchemy import (
    create_engine as ce,
    inspect
)

from datetime import date
from datetime import timedelta

class DataCollection:
    """
    Fetch stock data
    
    ...
    
    Attributes:
    ----------
    Basket of market index and assets
    
    Methods:
    --------
    get_raw_data(basket_list, start, end)
    sqlite_data(stock_data)
    save_data(raw_data)

    """

    # Specify portfolio sectors - basket of market index and assets
    blend_list = ['IBM', 'TSLA','TSM', 'NVDA', 'DVN', 'OXY','CNI', 'NOC','BHF', 'AIG']
    tech_list = ['AAPL', 'IBM', 'TSLA', 'GOOGL', 'MSFT','CSCO', 'TSM', 'NVDA']
    energy_list = ['DVN', 'OXY', 'NEE', 'MRO', 'APA', 'CTRA']
    industrials_list = ['BA', 'GE', 'CNI', 'NOC', 'LPX', 'BLDR', 'AAL', 'CPA']
    financials_list = ['BHF', 'AIG', 'EQH', 'PFG', 'WBS']
    market = ['^GSPC']   # adding S&P 500 Index (^GSPC) for use in beta weighting 

    # 'PDC',
    
    def get_raw_data(basket_list, start, end):
        """
        Fetch raw data from Yahoo Finance API
        Arguments:        
            basket_list: 
            start: 
            end: 
        Returns:
            stock_data
            raw_data
        """       
        stocks = basket_list
        raw_data = pdr.get_data_yahoo(stocks, start, end)

        # Save raw_data locally for reference
        DataCollection.save_data(raw_data)
        stock_data = raw_data['Close']
        return stock_data, raw_data

    
    def save_data(raw_data):
        """
        Save raw data into a local csv copy
        Arguments:        
            raw_data
        Returns:
            Nothing
        """
        
        # Check to see if data directory has raw data csv, else download from Yahoo Finance API
        if os.path.exists('data/raw_frame_close.csv') == True:
                os.remove('data/raw_frame_close.csv')
                raw_data.to_csv('data/raw_frame_close.csv')
        else:
                raw_data.to_csv('data/raw_frame_close.csv')
    

    def sqlite_data(stock_data):
        """
        Fetch SQLite data out of raw stock_data
        Arguments:        
            stock_data
        Returns:
            sql_basket_df
            sql_basket_indexed_df
        """
        # Generate temporary 'sqlite database' for online work
        db_connect_string = 'sqlite:///'

        # Create an engine to interact with the database
        engine = ce(db_connect_string)
        
        # display(sql.inspect(engine).get_table_names())          # confirm temporary database and engine function

        # write the imported (market + assets) dataframe into temporary sql database
        stock_data.to_sql('basket', con = engine, index=False, if_exists='replace')
        
        # display(sql.inspect(engine).get_table_names())          # confirm dataframe written to table in temporary sql database

        # Output dataframe name is sql_basket_df
        sql_basket_df = pd.read_sql_table('basket', con=engine) # extract sample of dataframe from table in temporary sql database
        
        # display(sql_basket_df.shape) 
        # display(sql_basket_df.sample())  # display sample row of database extracted

        sql_basket_indexed_df = (sql_basket_df.copy()).set_index('Date')

        return sql_basket_indexed_df, sql_basket_df


    """
    TESTING BELOW
    """

    # Basket
    # asset_list = ['AAPL', 'IBM', 'TSLA', 'GOOGL']
    # market = ['^GSPC']     

   
    # Set start and end dates of 3 years back from your current date
    # end_date = pd.to_datetime('today')
    # start_date = end_date - np.timedelta64(5, 'Y')     #  5 years
    # start, end = start_date, end_date
    # start, end                                         # verify our date range

    # stock_data=mpt_precanned_asset_selection(stocks, start, end)
    # print(stock_data)

    # stock_data = get_raw_data(asset_list, market, start, end)
    # print(stock_data)