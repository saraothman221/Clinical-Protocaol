import time
import streamlit as st

from components.header import show_header
from components.protocol_card import show_protocol_card
from components.reminder_card import show_reminder_card
from components.timeline import show_timeline
from components.protocol_state import timer_started, protocol_completed
import components.ai_insight as ai


st.set_page_config(
    page_title="Clinical Decision Support",
    layout="wide"
)

# =========================
# Initialize Timer
# =========================

if "remaining_seconds" not in st.session_state:
    st.session_state.remaining_seconds = 600

# =========================
# CSS
# =========================

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<link rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
""", unsafe_allow_html=True)

# =========================
# Header
# =========================

show_header()

# =========================
# Layout
# =========================

left, right = st.columns([2.3, 1], gap="large")

with left:
    show_protocol_card()
    show_timeline()

with right:
    show_reminder_card()
    ai.show_ai_insight()

# =========================
# Auto Refresh
# =========================

if timer_started() and not protocol_completed():

    if st.session_state.remaining_seconds > 0:

        time.sleep(1)

        st.session_state.remaining_seconds -= 1

        st.rerun()





