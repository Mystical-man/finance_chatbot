# finance_chatbot
Overview
Finance AI Assistant is an interactive chatbot application built using Streamlit and Gemini LLMs. It can answer both general and finance-related queries, fetch real-time stock prices, financial news, and currency exchange rates.
Project Structure
- `app.py`: Streamlit frontend with chat UI and theming support.
- `utils/chat_logic_1.py`: Handles message routing and LLM logic.
- `utils/api_handlers_1.py`: Fetches finance data (stock price, news, currency) using external APIs.
- `utils/theme_helpers.py`: Dynamically applies light/dark theme.
- `theme.py`: Contains theme color definitions.
- `config.py`: Loads all API keys from environment variables.
- `custom.css`: UI enhancements and style overrides.
- `requirements.txt`: Dependencies required to run the app.
Getting Started
1. Clone the repository:
   git clone <repo_url>
   cd finance_chatbot

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  (Windows: venv\Scripts\activate)

3. Install dependencies:
   pip install -r requirements.txt

4. Set up a `.env` file with your API keys for:
   - FINNHUB_KEY
   - NEWSAPI_KEY
   - CURRENCYFREAKS_KEY
   - GEMINI_API_KEY

5. Run the app:
   streamlit run app.py
Features
- Real-time stock lookup using Finnhub
- Currency rate retrieval using CurrencyFreaks
- Financial news headlines via NewsAPI
- Gemini LLM-based answers for both general and finance queries
- Light and Dark mode theme support
Core Logic
- Detects finance-related queries using keyword matching.
- For finance queries:
  - Extracts symbols from user text
  - Fetches stock price, news, and currency rate
  - Builds prompt with this data for Gemini to respond
- For non-finance queries:
  - Sends user input directly to Gemini model
- Multiple Gemini models tried in fallback sequence
Theming
- Uses `theme.py` and `theme_helpers.py` to support dynamic light/dark theme
- Additional CSS customizations applied via `custom.css`
Dependencies
- streamlit
- requests
- python-dotenv
- pandas
- google-generativeai
License
This project is open source and available under the MIT License.
