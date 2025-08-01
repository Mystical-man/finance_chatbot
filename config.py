# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Finance Data API Keys
# FINNHUB_KEY = os.getenv("FINNHUB_KEY")
# MARKETAUX_KEY = os.getenv("MARKETAUX_KEY")
# FMP_KEY = os.getenv("FMP_KEY")
# CURRENCYFREAKS_KEY = os.getenv("CURRENCYFREAKS_KEY")
# EXCHANGERATEAPI_KEY = os.getenv("EXCHANGERATEAPI_KEY")
# EODHD_KEY = os.getenv("EODHD_KEY")
# NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
# ALPHAVANTAGE_KEY = os.getenv("ALPHAVANTAGE_KEY")
# TWELVEDATA_KEY = os.getenv("TWELVEDATA_KEY")

# # LLM Providers
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  
# TOGETHERAI_KEY = os.getenv("TOGETHERAI_KEY")
# FIREWORKSAI_KEY = os.getenv("FIREWORKSAI_KEY")
# OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
# HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")


import os
from dotenv import load_dotenv

# Load environment variables from a .env file, if present
load_dotenv()

# --- MAIN API KEYS (required for your codebase) ---

FMP_KEY = os.getenv("FMP_KEY")                       # Financial Modeling Prep
ALPHAVANTAGE_KEY = os.getenv("ALPHAVANTAGE_KEY")     # Alpha Vantage
EODHD_KEY = os.getenv("EODHD_KEY")                   # EOD Historical Data
TWELVEDATA_KEY = os.getenv("TWELVEDATA_KEY")         # Twelve Data
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")               # NewsAPI.org
FINNHUB_KEY = os.getenv("FINNHUB_KEY")               # Finnhub (for bonds)
CURRENCYFREAKS_KEY = os.getenv("CURRENCYFREAKS_KEY") # CurrencyFreaks
EXCHANGERATEAPI_KEY = os.getenv("EXCHANGERATEAPI_KEY") # ExchangeRate API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")         # Google Gemini LLM

# --- OPTIONAL/FUTURE: Add any more as needed ---
# COINGECKO_KEY = os.getenv("COINGECKO_KEY")         # CoinGecko API (not required for free tier/basic usage)
# RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")           # For CoinGecko via RapidAPI if needed

# yfinance does not require a key

# Add further keys and config values here as new APIs or features are introduced

# App Info
APP_NAME = "Finance AI Assistant"
DEFAULT_THEME = "light"
DEFAULT_LANGUAGE = "en"