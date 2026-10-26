import streamlit as st

from components.protocol_state import (
    STEPS,
    initialize_protocol,
)


def show_timeline():

    initialize_protocol()

    current = st.session_state.current_step

    html = """
<div class="timeline-card">

<div class="timeline-title">
📋 Protocol Timeline
</div>

<div class="timeline-horizontal">
"""

    for i, step in enumerate(STEPS):

        if i < current:
            circle = '<div class="timeline-circle completed">✓</div>'

        elif i == current:
            circle = '<div class="timeline-circle current"></div>'

        else:
            circle = '<div class="timeline-circle pending"></div>'

        html += f"""
<div class="timeline-step-box">

{circle}

<div class="timeline-step-title">
{step}
</div>
"""

        if i != len(STEPS) - 1:
            html += """
<div class="timeline-connector"></div>
"""

        html += """
</div>
"""

    html += """
</div>
</div>
"""

    st.markdown(html, unsafe_allow_html=True)