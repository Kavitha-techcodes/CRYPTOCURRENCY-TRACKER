import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title="Cryptocurrency Price Tracker",
    page_icon="₿",
    layout="wide"
)


st.title("₿ Cryptocurrency Price Tracker")
st.write(
    "Real-Time Cryptocurrency Monitoring Dashboard"
)


FILE_PATH = "data/crypto_data.csv"


if not os.path.exists(FILE_PATH):

    st.error(
        "CSV file not found. Please run main.py first."
    )

    st.stop()


df = pd.read_csv(FILE_PATH)

df = df.dropna()


# =====================================
# LATEST DATA
# =====================================

latest_time = df["Timestamp"].max()

latest_data = df[
    df["Timestamp"] == latest_time
].copy()


# =====================================
# STATISTICS
# =====================================

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Coins Tracked",
        len(latest_data)
    )


with col2:

    st.metric(
        "Total Records",
        len(df)
    )


with col3:

    st.metric(
        "Last Updated",
        latest_time
    )


# =====================================
# LATEST DATA
# =====================================

st.subheader("📊 Latest Cryptocurrency Data")

st.dataframe(
    latest_data,
    width="stretch"
)


# =====================================
# WATCHLIST
# =====================================

st.subheader("⭐ My Watchlist")


coins = sorted(
    df["Name"].unique()
)


selected_watchlist = st.multiselect(
    "Select cryptocurrencies:",
    coins,
    default=coins[:3]
)


if selected_watchlist:

    watchlist_data = latest_data[
        latest_data["Name"].isin(
            selected_watchlist
        )
    ]

    st.dataframe(
        watchlist_data,
        width="stretch"
    )


# =====================================
# PORTFOLIO
# =====================================

st.subheader("💼 My Portfolio")


portfolio = []


for coin in selected_watchlist:

    coin_row = latest_data[
        latest_data["Name"] == coin
    ]

    if not coin_row.empty:

        price_text = coin_row.iloc[0]["Price"]

        try:

            price = float(
                price_text
                .replace("$", "")
                .replace(",", "")
            )

        except:

            price = 0


        quantity = st.number_input(
            f"{coin} Quantity",
            min_value=0.0,
            value=0.0,
            step=0.01,
            key=f"quantity_{coin}"
        )


        value = quantity * price


        portfolio.append({
            "Coin": coin,
            "Price": price,
            "Quantity": quantity,
            "Value": value
        })


if portfolio:

    portfolio_df = pd.DataFrame(
        portfolio
    )

    total_value = portfolio_df[
        "Value"
    ].sum()


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Portfolio Value",
            f"${total_value:,.2f}"
        )


    with col2:

        st.metric(
            "Coins in Portfolio",
            len(portfolio_df)
        )


    st.dataframe(
        portfolio_df,
        width="stretch"
    )


    st.subheader(
        "📊 Portfolio Distribution"
    )

    chart_data = portfolio_df.set_index(
        "Coin"
    )

    st.bar_chart(
        chart_data["Value"]
    )


# =====================================
# CRYPTO SELECTOR
# =====================================

st.subheader(
    "🔍 Cryptocurrency Details"
)


selected_coin = st.selectbox(
    "Choose a cryptocurrency:",
    coins
)


coin_data = df[
    df["Name"] == selected_coin
].copy()


# =====================================
# PRICE HISTORY
# =====================================

st.subheader(
    f"📈 {selected_coin} Price History"
)


coin_data["Price_Number"] = (
    coin_data["Price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)


price_chart = coin_data[
    ["Timestamp", "Price_Number"]
].copy()


price_chart["Timestamp"] = pd.to_datetime(
    price_chart["Timestamp"]
)


price_chart = price_chart.set_index(
    "Timestamp"
)


st.line_chart(
    price_chart["Price_Number"]
)


# =====================================
# CURRENT DETAILS
# =====================================

latest_coin = coin_data.iloc[-1]


st.subheader("💰 Current Details")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Price",
        latest_coin["Price"]
    )


with col2:

    st.metric(
        "24h Change",
        latest_coin["24h Change"]
    )


with col3:

    st.metric(
        "Market Cap",
        latest_coin["Market Cap"]
    )


# =====================================
# HISTORICAL DATA
# =====================================

st.subheader(
    "📋 Historical Records"
)


st.dataframe(
    coin_data,
    width="stretch"
)