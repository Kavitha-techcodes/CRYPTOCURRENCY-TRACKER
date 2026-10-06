from scraper import get_crypto_data
from filters import filter_by_price, highest_gainer

import pandas as pd
from datetime import datetime
import os
import time


FILE_PATH = "data/crypto_data.csv"


def save_data(data):

    df = pd.DataFrame(data)

    df["Timestamp"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    os.makedirs("data", exist_ok=True)

    if os.path.exists(FILE_PATH):

        df.to_csv(
            FILE_PATH,
            mode="a",
            header=False,
            index=False
        )

    else:

        df.to_csv(
            FILE_PATH,
            index=False
        )

    print("Data saved successfully!")


while True:

    print("\n==============================")
    print("Fetching cryptocurrency data...")
    print("==============================")

    data = get_crypto_data(headless=True)

    if data:

        print("\n===== TOP 10 CRYPTOCURRENCIES =====")

        for coin in data:
            print(coin)

        save_data(data)

        # Price filter
        filtered_coins = filter_by_price(
            data,
            1000
        )

        print("\n===== COINS ABOVE $1000 =====")

        for coin in filtered_coins:
            print(coin)

        # Highest gainer
        gainer = highest_gainer(data)

        print("\n===== HIGHEST 24H GAINER =====")

        if gainer:
            print(gainer)

    else:

        print("No cryptocurrency data found.")

    print("\nWaiting 60 seconds for next update...")

    time.sleep(60)