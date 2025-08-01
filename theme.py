LIGHT_THEME = {
    "background_color": "#ffffff",
    "text_color": "#000000",
    "input_background": "#f0f0f0",
    "primary_color": "#3A86FF",
    "chat_user_bg": "#D0E8FF",
    "chat_bot_bg": "#F0F0F0"
}

DARK_THEME = {
    "background_color": "#121212",
    "text_color": "#E0E0E0",
    "input_background": "#1E1E1E",
    "primary_color": "#3A86FF",
    "chat_user_bg": "#065F46",
    "chat_bot_bg": "#134E4A"
}

def get_theme(theme_mode: str):
    if theme_mode.lower() == "dark":
        return DARK_THEME
    return LIGHT_THEME
