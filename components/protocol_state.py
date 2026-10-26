import streamlit as st

START_SECONDS = 600

# Clinical Workflow
STEPS = [
    "Patient Admitted",
    "Consent Verified",
    "CBC Reviewed",
    "Antibiotic Due",
    "Ready for Surgery"
]


def initialize_protocol():

    if "current_step" not in st.session_state:
        st.session_state.current_step = 0

    if "remaining_seconds" not in st.session_state:
        st.session_state.remaining_seconds = START_SECONDS


def get_current_step():

    initialize_protocol()

    if protocol_completed():
        return "Protocol Completed"

    return STEPS[st.session_state.current_step]


def get_compliance():

    initialize_protocol()

    completed_steps = min(
        st.session_state.current_step + 1,
        len(STEPS)
    )

    return int((completed_steps / len(STEPS)) * 100)


def next_step():

    initialize_protocol()

    if not protocol_completed():
        st.session_state.current_step += 1


def protocol_completed():

    initialize_protocol()

    return st.session_state.current_step >= len(STEPS)


def timer_started():

    initialize_protocol()

    # يبدأ المؤقت فقط عند خطوة Antibiotic Due
    return (
        st.session_state.current_step >= 3
        and not protocol_completed()
    )