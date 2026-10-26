import streamlit as st
import json

from components.protocol_state import (
    get_compliance,
    protocol_completed,
    timer_started,
)


def show_protocol_card():

    with open("data/protocol.json", "r", encoding="utf-8") as file:
        protocol = json.load(file)

    remaining = st.session_state.get("remaining_seconds", 600)

    # ==========================
    # Status
    # ==========================

    if protocol_completed():

        status = "Completed"
        badge_color = "#16A34A"
        badge_bg = "#DCFCE7"

    elif not timer_started():

        status = "Pending"
        badge_color = "#2563EB"
        badge_bg = "#DBEAFE"

    elif remaining > 300:

        status = "Active"
        badge_color = "#16A34A"
        badge_bg = "#DCFCE7"

    elif remaining > 0:

        status = "Warning"
        badge_color = "#D97706"
        badge_bg = "#FEF3C7"

    else:

        status = "Overdue"
        badge_color = "#DC2626"
        badge_bg = "#FEE2E2"

    # ==========================
    # Timer Display
    # ==========================

    if protocol_completed():

        timer_display = "✓"
        timer_label = "Completed"
        timer_class = "timer-completed"

    elif not timer_started():

        timer_display = "🕐"
        timer_label = "Not Started"
        timer_class = "timer-inactive"

    else:

        minutes = remaining // 60
        seconds = remaining % 60

        timer_display = f"{minutes:02}:{seconds:02}"
        timer_label = "Remaining Time"
        timer_class = "timer-active"

    # ==========================
    # Compliance
    # ==========================

    compliance = get_compliance()

    # ==========================
    # Protocol Card
    # ==========================

    html = f"""
<div class="protocol-card">

<div class="protocol-title">
<span class="protocol-dot"></span>
Clinical Protocol
</div>

<div class="protocol-label">
Protocol
</div>

<div class="protocol-value">
{protocol["protocol_name"]}
</div>

<div class="protocol-status-area">

<div class="protocol-status-item">

<div
class="status-badge-large"
style="
background:{badge_bg};
color:{badge_color};
">
{status}
</div>

<div class="status-caption">
Protocol Status
</div>

</div>

<div class="protocol-timer-item">

<div
class="{timer_class}"
style="color:{badge_color};">
{timer_display}
</div>

<div class="timer-label">
{timer_label}
</div>

</div>

</div>

<div class="compliance-section">

<div class="compliance-header">

<div class="protocol-label">
Compliance
</div>

<div class="compliance-percent">
{compliance}%
</div>

</div>

<div class="progress-bg">

<div
class="progress-fill"
style="width:{compliance}%">
</div>

</div>

</div>

</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )