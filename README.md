# Solana Meme Coin Filter

## Overview
This project fetches the top 70 trending coins from [CoinGecko](https://www.coingecko.com/), filters them to identify meme coins built on the Solana blockchain, and returns both the meme coin name and its contract address.

The output has been validated by cross-referencing the returned contract addresses with actual Solana-based meme coins using tools like [Solscan](https://solscan.io/). For example, the token below was successfully verified:
👉 [DriFtupJYLTosbwoN8koMbEYSx54aFAVLddWsbksjwg7 on Solscan](https://solscan.io/token/DriFtupJYLTosbwoN8koMbEYSx54aFAVLddWsbksjwg7).

## Example Response from today(27th Aug, 2025)
Here is an example of the data that is returned by the filter:

- **Pudgy Penguins** (pengu): `2zMMhcVQEXDtdE6vsFS7S7D5oUodfJHE8vd1gnBouauv`
- **Jupiter** (jup): `JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN`
- **Pump.fun** (pump): `pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn`
- **Drift Protocol** (drift): `DriFtupJYLTosbwoN8koMbEYSx54aFAVLddWsbksjwg7`

## How it works
1. The project queries the CoinGecko API to fetch the list of the top 70 trending coins.
2. It then filters this list to identify meme coins on the Solana blockchain.
3. For each identified meme coin, it returns the name and contract address.

## Tools Used
- **CoinGecko API**: To fetch trending coins.
- **Solscan**: To validate contract addresses and ensure they belong to Solana-based tokens.

## Requirements
- Python 3.x
- Requests library (`pip install requests`)
- Access to the CoinGecko API (no authentication required for basic use)

## Installation

# 1. Clone the repository
git clone https://github.com/sam253narula/trending-solana-memecoin-coingecko-python-filter

# 2. Navigate into the project directory

# 3. (Optional) Create a virtual environment (recommended)
python -m venv venv

# 4. Activate the virtual environment
source venv/bin/activate

# 5. Install the required dependencies
pip3 install -r requirements.txt

# 6. Run the script to filter Solana-based meme coins
python test_coingrecko.py
