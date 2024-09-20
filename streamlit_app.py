import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st
import requests

# Coinbase API endpoint for available currencies
url = "https://api.coinbase.com/v2/currencies"

# Fetch the data from Coinbase API
response = requests.get(url)
data = response.json()

# Get the list of coins
coins = data['data']

# Streamlit title
st.title("List of Available Coins on Coinbase")

# Display each coin in a simple format
st.write("### Coins Available:")

# Display the list of coins in a table
coin_list = []
for coin in coins:
    coin_list.append([coin['id'], coin['name']])

# Show in a dataframe-like table in Streamlit
st.table(coin_list)
