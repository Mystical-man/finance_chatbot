from utils.api_handlers_1 import handle_finance_query, is_finance_query
from config import GEMINI_API_KEY
import google.generativeai as genai

# Load Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Gemini models to try
GEMINI_MODELS = ["gemini-pro", 
                 "models/gemini-1.5-flash-latest",
                 "gemini-2.5-pro",
                 "gemini-2.5-flash",
                 "gemini-2.5-flash-lite"]

# Try generating a response with a specific model
def try_generate_with_model(prompt, model_name):
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return True, response.text
    except Exception as e:
        return False, f"Gemini error with {model_name}: {e}"

# Shorten long responses if necessary
def summarize_text(text, max_lines=10):
    lines = text.splitlines()
    if len(lines) <= max_lines:
        return text.strip()
    return "\n".join(lines[:max_lines]) + "\n[...response truncated]"

# Count how many lines a response has
def count_lines(text):
    return len(text.splitlines())

# Core message processing logic
def process_user_message(user_message: str, context: str = "general") -> str:
    """
    Handles general and finance messages. Falls back to general LLM reply if finance data is unavailable.
    """
    if context == "finance":
        data_context, has_data = handle_finance_query(user_message)
        if has_data:
            prompt = data_context
        else:
            prompt = (
                f"The user asked a finance-related question, but no real-time market data was available.\n"
                f"Please try to answer helpfully using general financial knowledge.\n\n"
                f"User message: {user_message}"
            )
    else:
        prompt = user_message

    # Try Gemini models in order
    for model_name in GEMINI_MODELS:
        success, response = try_generate_with_model(prompt, model_name)
        if success:
            if count_lines(response) > 10:
                return summarize_text(response)
            else:
                return response.strip()
        else:
            print(f"Fallback triggered: {response}")

    return "Sorry, I couldn’t generate a response right now. Please try again later."
