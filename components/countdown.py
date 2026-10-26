import streamlit as st

START_SECONDS = 600

# Initialize timer once
if "remaining_seconds" not in st.session_state:
    st.session_state.remaining_seconds = START_SECONDS


def show_countdown():

    remaining = st.session_state.remaining_seconds

    # Timer color
    if remaining > 300:
        color = "#16A34A"      # Green

    elif remaining > 0:
        color = "#F59E0B"      # Orange

    else:
        color = "#DC2626"      # Red

    minutes = remaining // 60
    seconds = remaining % 60

    st.markdown(
        f"""
<div style="
background:white;
border-radius:16px;
padding:16px;
border-left:6px solid {color};
font-size:22px;
font-weight:700;
margin-bottom:15px;
">

⏰ Remaining Time

<h2 style="margin:8px 0;color:{color};">
{minutes:02}:{seconds:02}
</h2>

</div>
""",
        unsafe_allow_html=True,
    )