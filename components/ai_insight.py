import streamlit as st


def show_ai_insight():

    remaining = st.session_state.get("remaining_seconds", 600)

    if remaining > 300:
        status = "Active"

    elif remaining > 0:
        status = "Warning"

    else:
        status = "Overdue"

    if status == "Active":

        icon = "🟢"

        assessment = (
            "The patient is progressing according to the selected clinical protocol."
        )

        attention = (
            "No protocol deviations have been detected at this stage."
        )

        recommendation = (
            "Continue monitoring until antibiotic administration is documented."
        )

    elif status == "Warning":

        icon = "🟠"

        assessment = (
            "The protocol is approaching its intervention deadline."
        )

        attention = (
            "One critical task remains before surgery."
        )

        recommendation = (
            "Notify the assigned nurse if medication has not yet been administered."
        )

    else:

        icon = "🔴"

        assessment = (
            "A protocol deviation has been detected."
        )

        attention = (
            "The recommended administration window has expired."
        )

        recommendation = (
            "Escalate immediately to the surgical team."
        )

    st.markdown(f"""

<div class="ai-card">

<div class="ai-header">

<div class="ai-title">
🧠 AI Assessment
</div>

<div class="ai-badge">
<div class="ai-live"></div>
Live
</div>

</div>

<div class="ai-bubble">

<div class="ai-heading">
{icon} Overall Assessment
</div>

<div class="ai-text">
{assessment}
</div>

</div>

<div class="ai-bubble">

<div class="ai-heading">
⚠ Attention
</div>

<div class="ai-text">
{attention}
</div>

</div>

<div class="ai-bubble">

<div class="ai-heading">
💡 Recommendation
</div>

<div class="ai-text">
{recommendation}
</div>

</div>

</div>

""", unsafe_allow_html=True)