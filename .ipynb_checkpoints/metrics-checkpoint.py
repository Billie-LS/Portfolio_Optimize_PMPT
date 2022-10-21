import pandas as pd
import numpy as np

from pathlib import Path

class QuantMetrics:
    """
    Calculates performance stats of assets

    ...
    
    Attributes:
    ----------
    num_trading_days = 252
    risk_free_rate = 0.0275
    num_random_portfolio_run = 10000
    rolling_window_days = 20
    
    Methods:
    --------
    mpt_qa_compute_freq_stats(sql_basket_indexed_df)
    mpt_qa_get_efficient_frontier(asset_prices_df, asset_prices_ann_returns_mean, asset_prices_ann_cov_mtrx_df)
    mpt_qa_return_portfolio_allocations(efficient_frontier_df)

    """

    # Constants being used for this module
    # No of trading days ina year
    num_trading_days = 252
    # Risk free rate of ??
    risk_free_rate = 0.0275
    # No of simulations in Monte Carlo
    num_random_portfolio_run = 10000
    # Rolling windos period of ??
    rolling_window_days = 20

    """
    Get asset prices from .csv files
    """
    """
    def mpt_qa_get_asset_prices_csv(filename):
        asset_prices_df = pd.read_csv(
            Path(filename), 
            index_col="Date", 
            parse_dates=True, 
            infer_datetime_format=True
        )

        #TEMP CODE UNTIL GET REAL MAKRKET DATA - USE CISOO AS MARKET
        asset_prices_df.insert(loc = 0, column = 'market', value = asset_prices_df['cisco'])
        asset_prices_df.drop(['cisco'], axis=1, inplace=True)
        
        return asset_prices_df
    """

    def mpt_qa_compute_freq_stats(sql_basket_indexed_df):
        """
        Compute the frequency components on asset prices
        Arguments:
            sql_basket_indexed_df: ??            
        Returns:
            asset_prices_returns_df
            asset_prices_ann_returns_mean
            asset_prices_std_df
            asset_prices_ann_std_df
            asset_prices_std_rolling_df
            asset_prices_ann_cov_mtrx_df
            asset_prices_ann_corr_mtrx_df
            asset_prices_cum_returns_df
            asset_prices_sharpe_ratio_df
            log_returns
        """

        # Compute the asset returns
        asset_prices_returns_df = sql_basket_indexed_df.pct_change().dropna()
        # Compute the annual average asset returns
        asset_prices_ann_returns_mean = asset_prices_returns_df.mean() * QuantMetrics.num_trading_days
        
        # 'Close' prices dataframe Log returns for ALL portfolio assets and <market/index>
        log_returns = np.log(sql_basket_indexed_df / sql_basket_indexed_df.shift(1)).dropna()
        
        # Compute the standard deviation of the assets   
        asset_prices_std_df = asset_prices_returns_df.std()
        # Compute the annualized standard deviation of the assets   
        asset_prices_ann_std_df = asset_prices_std_df * np.sqrt(QuantMetrics.num_trading_days)
        # Compute the rolling_window standard deviation of the assets   
        asset_prices_std_rolling_df = asset_prices_returns_df.rolling(window = QuantMetrics.rolling_window_days).std()
        # Compute the asset annual covariance matrix
        asset_prices_ann_cov_mtrx_df = asset_prices_returns_df.cov() * QuantMetrics.num_trading_days
        # Compute the asset correlation matrix
        asset_prices_ann_corr_mtrx_df = asset_prices_returns_df.corr()
        # Compute the cumulative returns
        asset_prices_cum_returns_df = (1 + asset_prices_returns_df).cumprod() - 1
        # Compute the share ratio 
        asset_prices_sharpe_ratio_df = asset_prices_ann_returns_mean / asset_prices_ann_std_df

        return asset_prices_returns_df,     \
            asset_prices_ann_returns_mean,  \
            asset_prices_std_df,            \
            asset_prices_ann_std_df,        \
            asset_prices_std_rolling_df,    \
            asset_prices_ann_cov_mtrx_df,   \
            asset_prices_ann_corr_mtrx_df,  \
            asset_prices_cum_returns_df,    \
            asset_prices_sharpe_ratio_df,   \
            log_returns

    def mpt_qa_get_efficient_frontier(asset_prices_df, asset_prices_ann_returns_mean, asset_prices_ann_cov_mtrx_df):
        """
        Determines the efficient frontier components:
        (1) Portfolio Returns
        (2) Porfolio Volatility (Risk)
        (3) Sharpe Ratio 
        Arguments:
            asset_prices_df
            asset_prices_ann_returns_mean
            asset_prices_ann_cov_mtrx_df      
        Returns:
            efficient_frontier_df
        """

        # Initialize an empty list for storing the portfolio returns
        portfolio_returns = []
        # Initialize an empty list for storing the portfolio volatility
        portfolio_volatility = []
        # Initialize an empty list for storing the portfolio weights
        portfolio_weights = []
        # Initialize an empty list for storing the shapre ratio
        portfolio_sharpe_ratio = []

        # Get the number of assets in the asset datafrme
        num_assets = asset_prices_df.shape[1]    

        for portfolio_idx in range(QuantMetrics.num_random_portfolio_run):
        
            # Normalize weight    
            # Generate random wieghts
            weights = np.random.random(num_assets)
            # Normalize the weights so that the sum of all the wieghts are = 1
            weights = weights / np.sum(weights)    
            # Add teh portfolio weights to the list of portfolio weights
            portfolio_weights.append(weights)
        
            # Compute the portfolio return (weights of each asset * the return of each asset)
            returns = np.dot(weights, asset_prices_ann_returns_mean)    
            # Add the portfolio return to the list of portfolio returns
            portfolio_returns.append(returns)
        
            # Compute the portfolio variance
            variance = asset_prices_ann_cov_mtrx_df.mul(weights, axis=0).mul(weights, axis=1).sum().sum()
            # Compute the portfolio starndard deviation
            std_dev = np.sqrt(variance);
            # Annualize the standard deviation will give the volatility
            volatility = std_dev * np.sqrt(QuantMetrics.num_trading_days)
            # Append the porfolio volatility to the list of portfolio volatilities
            portfolio_volatility.append(volatility)
        
            # Compute the ssharpe ratio
            sharpe_ratio = (returns - QuantMetrics.risk_free_rate) / volatility;
            # Append the sharpe ratio to the list of protfolio sharpe ratios
            portfolio_sharpe_ratio.append(sharpe_ratio)        

        # Create a list of the asset from the input asset df
        asset_lst = list(asset_prices_df.columns);

        # Create an empty dataframe
        efficient_frontier_df = pd.DataFrame()

        # Add the return and volitilty to each portfolio/row
        efficient_frontier_df['Returns'] = pd.DataFrame(portfolio_returns)
        efficient_frontier_df['Volatility'] = pd.DataFrame(portfolio_volatility)
        efficient_frontier_df['SharpeRatio'] = pd.DataFrame(portfolio_sharpe_ratio)

        # Create a dataframe of number of portfolios by the wieght of easch asset/symbol
        for portfolio_idx, asset in enumerate(asset_prices_df.columns.tolist()):
            efficient_frontier_df[asset + '_W'] = pd.DataFrame([w[portfolio_idx] for w in  portfolio_weights])

        return efficient_frontier_df

    def mpt_qa_return_portfolio_allocations(efficient_frontier_df):
        """
        Select portfolio allocations based on the:
        (1) "minimum" risk
        (2) "maximum" risk
        (3) "optimum sharpe ratio"
        Arguments:
            efficient_frontier_df   
        Returns:
            portfolio_min_volatility
            portfolio_max_volatility
            portfolio_opt_sharpe_ratio
        """

        portfolio_min_volatility = efficient_frontier_df.iloc[efficient_frontier_df.loc[:,'Volatility'].idxmin()]
        portfolio_max_volatility = efficient_frontier_df.iloc[efficient_frontier_df.loc[:,'Volatility'].idxmax()]
        portfolio_opt_sharpe_ratio = efficient_frontier_df.iloc[efficient_frontier_df.loc[:,'SharpeRatio'].idxmax()]
        
        return portfolio_min_volatility, portfolio_max_volatility, portfolio_opt_sharpe_ratio