import streamlit as st
import json

from components.protocol_state import (
    STEPS,
    initialize_protocol,
    next_step,
    protocol_completed,
)


def show_reminder_card():

    initialize_protocol()

    current = st.session_state.current_step

    if protocol_completed():

        priority = "Completed"
        message = "Clinical protocol completed successfully."
        responsible = "System"

    else:

        with open("data/reminders.json", "r", encoding="utf-8") as file:
            reminder = json.load(file)

        priority = reminder["priority"]
        responsible = reminder["responsible"]

        reminder_messages = [
            "Complete patient admission.",
            "Verify informed consent.",
            "Review CBC results.",
            "Administer Cefazolin 2 g IV.",
            "Prepare patient for surgery."
        ]

        message = reminder_messages[current]

    st.markdown(
        f"""
<div class="reminder-card">

<div class="reminder-title">
🔔 Action Required
</div>

<div class="reminder-item">

<div class="reminder-label">
Priority
</div>

<div class="priority-high">
{priority}
</div>

</div>

<div class="reminder-item">

<div class="reminder-label">
Action
</div>

<div class="reminder-value">
{message}
</div>

</div>

<div class="reminder-item">

<div class="reminder-label">
Responsible
</div>

<div class="reminder-value">
👩‍⚕️ {responsible}
</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    if not protocol_completed():

        if st.button(
            "✅ Complete & Continue",
            use_container_width=True,
            key="complete_protocol_step",
        ):
            next_step()
            st.rerun()