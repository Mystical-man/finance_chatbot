import streamlit as st

# Append bot reply to chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

from theme_helpers import apply_theme
from chat_logic_1 import process_user_message
from api_handlers_1 import is_finance_query

# Page settings
st.set_page_config(page_title="Finance AI Assistant", page_icon=":money_with_wings:", layout="centered")

# Apply theme (light/dark)
apply_theme()

# Title
st.markdown(
    "<h2 style='text-align:center; color:#3A86FF; margin-bottom: 0.3rem;'>Finance AI Assistant</h2>",
    unsafe_allow_html=True,
)

# Initialize message history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat message container with updated color scheme
with st.container():
    for speaker, msg in st.session_state["messages"]:
        align = "right" if speaker == "user" else "left"
        user_bg = "#4B7398" if speaker == "user" else "#C9F5C4"
        user_text = "#000000"
        if st.session_state.get("theme", "light") == "dark":
            user_bg = "#065F46" if speaker == "user" else "#134E4A"
            user_text = "#D1FAE5"

        st.markdown(
            f"""
            <div style='text-align:{align}; margin: 0.5rem 0;'>
                <div style='display:inline-block; background-color:{user_bg}; padding: 0.75rem 1rem; 
                            border-radius: 20px; max-width: 70%; color:{user_text};'>
                    <b>{speaker.title()}:</b> {msg}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Input form (with accessible label via Streamlit's label param)
with st.form(key="input_form", clear_on_submit=True):
    user_input = st.text_input(
        label="Ask about finance or chat with me!",
        key="user_message_input",
        placeholder="Type your message here...",
        help="You can ask about stock prices, news, or general finance questions.",
    )
    sent = st.form_submit_button("Send")

# On form submission handle user input
if sent and user_input.strip():
    # Append user message to chat history
    st.session_state["messages"].append(("user", user_input))

    # Determine if finance context to route queries
    if is_finance_query(user_input):
        reply = process_user_message(user_input, context="finance")
    else:
        reply = process_user_message(user_input, context="general")

    st.session_state["messages"].append(("bot", reply))

    # Refresh UI to reflect new messages
    st.rerun()
