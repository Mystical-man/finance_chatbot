import streamlit as st
from theme import get_theme

def apply_theme():
    """
    Apply light or dark theme dynamically based on session_state['theme'].
    This function sets Streamlit's page config and styles.
    """
    theme_mode = st.session_state.get("theme", "dark")
    colors = get_theme(theme_mode)

    # Streamlit default theming for major components:
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background-color: {colors['background_color']};
            color: {colors['text_color']};
        }}
        .css-1xarl3l input[type="text"] {{
            background-color: {colors['input_background']} !important;
            color: {colors['text_color']} !important;
        }}
        .stButton > button {{
            background-color: {colors['primary_color']} !important;
            color: white !important;
            font-weight: 600 !important;
        }}
        .stButton > button:hover {{
            background-color: #2f75d6 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
