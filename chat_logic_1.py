from utils.api_handlers_1 import handle_finance_query, is_finance_query
from config import GEMINI_API_KEY
import google.generativeai as genai

# Load Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Gemini models to try
GEMINI_MODELS = [ #"gemini-2.5-pro", if needed
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


# Core message processing logic
def process_user_message(user_message: str, context: str = None) -> str:
    if context is None:
        context = "finance" if is_finance_query(user_message) else "general"

    """
    Handles general and finance messages. Falls back to general LLM reply if finance data is unavailable.
    """
    if context == "finance":
        data_context, has_data = handle_finance_query(user_message)
        if has_data:
            prompt = f"Summarize the following finance data in 10 lines or fewer:\n\n{data_context}"
        else:
            prompt = (
                f"The user asked a finance-related question but no real-time data is available.\n"
                f"Using general financial knowledge, answer briefly.\n"
                f"Summarize in 10 lines or fewer.\n\nUser message: {user_message}"
            )
    else:
        prompt = f"Summarize in 10 lines or fewer: {user_message}"

    # Try Gemini models in order
    for model_name in GEMINI_MODELS:
        success, response = try_generate_with_model(prompt, model_name)
        if success:
            return response.strip()
        else:
            print(f"Fallback triggered: {response}")

    return "Sorry, I couldn’t generate a response right now. Please try again later."
