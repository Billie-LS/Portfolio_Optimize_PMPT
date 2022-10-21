### class DataCollection
---
* Methods
    * get_raw_data(basket_list, start, end) - Fetches raw data from Yahoo! Finance Web API endpoint
    * sqlite_data(stock_data) - Saves raw data into SQLite temp database
    * save_data(raw_data) - Saves raw data of Yahoo! Finance API endpoint into a csv file inside ***data/*** folder

* Installations
    Install package yfinance
    ```python
    > pip install yfinance
    ```
    Install package SQLAlchemy
    ```python
    > pip install SQLAlchemy
    ```

* References
    * [yfinance](https://pypi.org/project/yfinance/) - Download market data from Yahoo! Finance's API
    * [SQLAlchemy](https://www.sqlalchemy.org/) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

    

