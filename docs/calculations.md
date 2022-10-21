### class MPTCalculations
---
* Methods
    * mpt_pe_compute_portfolio_returns(asset_prices_returns_df, portfolio_volatility) - Compute the returns of a portfolio given the portfolio weights and returns of the individual assets
    * mpt_pe_get_portfolio_weights_df(portfolio_volatility) - Extract the weigths into a new dataframe from a sequence of portfolio meta-data (returns, volatility, Sharpe Ratio, weights)
    * mpt_pe_get_mc_porfolio_df(asset_prices_df) - Arrange Monte-Carlo dataframe to have tuples for column names as required by the MCForecastTools
    * mpt_pe_get_mc_weights(portfolio_weights) - Arrange Monte-Carlo dataframe weights list as required by the MCForecastTools
    * mpt_pe_compute_investment_pnl(initial_test_investment, asset_prices_test_beg_df, asset_prices_test_end_df, portfolio_weights_df) - Compute PNL on an initial investment of a portfolio

* References
    * [Modern Portfolio Theory](https://www.investopedia.com/terms/m/modernportfoliotheory.asp) - To understand risks and returns characterics of a possibly healthy portfolio