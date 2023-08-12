import logging
import os
import sys
from typing import Tuple

import yfinance
import pandas


def get_trading_volume(symbol: str, logger: logging.Logger, hours: int = 48) -> Tuple[pandas.Series, pandas.Series]:
    """Get assumed trading volume of a particular stock.

    Args:
        symbol: Stock ticker.
        logger: Logger object.
        hours: Number of hours to fetch the historical data.

    Returns:
        Tuple[pandas.Series, pandas.Series]:
        Returns a tuple of the Series of information for buy and sell.
    """
    # Fetch historical stock data using yfinance
    sys.stdout = open(os.devnull, 'w')  # block print
    stock_data = yfinance.download(symbol, period=f"{hours}h", interval="1h")
    sys.stdout = sys.__stdout__  # release print

    # Filter rows with non-zero buy and sell volumes
    filtered_data = stock_data[(stock_data['Volume'] > 0)]

    # Separate buy and sell volume data
    assumed_buy_volume = filtered_data[filtered_data['Close'] > filtered_data['Close'].shift(-1)]['Volume']
    assumed_sell_volume = filtered_data[filtered_data['Close'] < filtered_data['Close'].shift(-1)]['Volume']

    logger.info("Predicted buy: %s", '{:,}'.format(assumed_buy_volume.sum()))
    logger.info("Predicted sell: %s", '{:,}'.format(assumed_sell_volume.sum()))

    assumed_buy_volume = pandas.Series(assumed_buy_volume, name="Predicted buying volume")
    assumed_sell_volume = pandas.Series(assumed_sell_volume, name="Predicted selling volume")

    return assumed_buy_volume, assumed_sell_volume
