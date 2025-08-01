import requests
from config import (
    FINNHUB_KEY,
    NEWSAPI_KEY,
    CURRENCYFREAKS_KEY,
)

# Symbol lookup using Finnhub search API
def lookup_finnhub_symbol(company_name):
    url = f"https://finnhub.io/api/v1/search?q={company_name}&token={FINNHUB_KEY}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("result", [])
        for r in results:
            if r.get("type") == "Equity":
                return r.get("symbol")
        return None
    except Exception as e:
        print(f"Symbol lookup failed for '{company_name}': {e}")
        return None

# Extract symbols from user message using uppercase tickers and company name lookup
def extract_symbols(user_message):
    import re

    user_message_lower = user_message.lower()
    detected = set()

    # 1. Typed uppercase tickers (e.g., AAPL, TSLA)
    detected.update(re.findall(r"\b[A-Z]{1,5}\b", user_message))

    # 2. Basic hardcoded company/crypto name mapping
    known_symbols = {
        "apple": "AAPL",
        "microsoft": "MSFT",
        "google": "GOOGL",
        "alphabet": "GOOGL",
        "amazon": "AMZN",
        "meta": "META",
        "facebook": "META",
        "tesla": "TSLA",
        "nvidia": "NVDA",
        "tata": "TATAMOTORS.BSE",
        "reliance": "RELIANCE.BSE",
        "infosys": "INFY.BSE",
        "bitcoin": "BTC-USD",
        "btc": "BTC-USD",
        "ethereum": "ETH-USD",
        "eth": "ETH-USD",
        "dogecoin": "DOGE-USD",
        "doge": "DOGE-USD",
    }

    for name, symbol in known_symbols.items():
        if name in user_message_lower:
            detected.add(symbol)

    # 3. Finnhub fallback if nothing found yet
    if not detected:
        words = re.findall(r"\b[a-z]{3,20}\b", user_message_lower)
        for word in words:
            symbol = lookup_finnhub_symbol(word)
            if symbol:
                detected.add(symbol)
                break  # Stop after first valid result

    return list(detected) if detected else ["AAPL"]


# Fetch stock price from Finnhub
def fetch_finnhub_price(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_KEY}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        price = data.get("c")
        return f"{symbol}: ${price:.2f}" if price else f"{symbol}: No Finnhub price data."
    except Exception as e:
        return f"{symbol}: Finnhub error - {e}"

# Fetch top 1 news headline for a symbol
def fetch_news(symbol, page_size=1):
    url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey={NEWSAPI_KEY}&pageSize={page_size}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        articles = data.get("articles", [])
        headlines = [a.get("title") for a in articles if "title" in a]
        return headlines if headlines else ["No recent news found."]
    except Exception as e:
        return [f"NewsAPI error: {e}"]

# Fetch basic currency rate
def fetch_currencyfreaks_usd_to_eur():
    url = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={CURRENCYFREAKS_KEY}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        rate = data.get("rates", {}).get("EUR")
        return f"USD to EUR: {rate}" if rate else "No CurrencyFreaks rate found."
    except Exception as e:
        return f"CurrencyFreaks error: {e}"

# Main handler for finance queries
def handle_finance_query(user_message: str) -> (str, bool):
    symbols = extract_symbols(user_message)
    all_prices_text = []

    # Use only Finnhub for price lookup
    for sym in symbols:
        price_line = fetch_finnhub_price(sym)
        all_prices_text.append(f"{price_line}")

    # Include news only if user asks for it
    include_news = any(word in user_message.lower() for word in ["news", "headlines", "update"])
    news_text = []
    if include_news:
        for sym in symbols:
            news_list = fetch_news(sym, page_size=1)
            news_text.append(f"\nNews for {sym}:\n" + "\n".join(f"- {n}" for n in news_list))

    # Basic currency info
    currency_info = fetch_currencyfreaks_usd_to_eur()

    # Compose final context
    context = (
        "Stock prices:\n" + "\n".join(all_prices_text) +
        ("\n\n" + "\n".join(news_text) if news_text else "") +
        f"\n\nCurrency rate:\n{currency_info}" +
        f"\n\nUser query: {user_message}\nPlease answer ONLY based on the above data."
    )

    # Check if price data is meaningful
    has_real_data = any("no" not in line.lower() and "error" not in line.lower() for line in all_prices_text)

    return (context, has_real_data)

# Classify query as finance-related or not
def is_finance_query(user_input: str) -> bool:
    finance_keywords = [
        "stock", "price", "quote", "shares", "market", "finance", "investment",
        "currency", "exchange rate", "news", "earnings", "dividend", "crypto",
        "bitcoin", "forex", "dow", "nasdaq", "s&p", "fundamental", "technical",
        "alpha", "beta", "pe ratio", "cash flow", "balance sheet",
    ]
    user_input_lower = user_input.lower()
    return any(keyword in user_input_lower for keyword in finance_keywords)
