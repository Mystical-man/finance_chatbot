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

# App Info
APP_NAME = "Finance AI Assistant"
DEFAULT_THEME = "light"
DEFAULT_LANGUAGE = "en"
