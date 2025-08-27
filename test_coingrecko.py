import requests
import time

def fetch_sol_trending_meme_coins(top_n=70):
    """Fetch trending meme coins and filter for Solana-based ones from CoinGecko."""
    # 1. Get trending coins by search popularity
    url = "https://api.coingecko.com/api/v3/search/trending"
    trending = requests.get(url).json().get("coins", [])
    coin_ids = [coin["item"]["id"] for coin in trending][:top_n]
    if not coin_ids:
        return []
    # 2. Get market data
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": ",".join(coin_ids),
        "order": "market_cap_desc",
        "per_page": top_n,
        "page": 1,
        "sparkline": False
    }
    market_data = requests.get(url, params=params).json()
    # 3. For each, check if Solana is one of the platforms by looking up /coins/{id}
    solana_meme_coins = []
    for coin in market_data:
        coin_id = coin["id"]
        detail_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
        detail_data = requests.get(detail_url).json()
        # Defensive: check platforms exists and contains 'solana'
        platforms = detail_data.get("platforms", {})
        if "solana" in platforms and platforms["solana"]:
            solana_meme_coins.append({**coin, "contract_address": platforms["solana"]})
        # Sleep a bit to avoid API rate limiting
        time.sleep(1.1)
    return solana_meme_coins

# Example usage
if __name__ == "__main__":
    trending_sol_meme_coins = fetch_sol_trending_meme_coins()
    for coin in trending_sol_meme_coins:
        print(f"{coin['name']} ({coin['symbol']}): {coin['contract_address']}")