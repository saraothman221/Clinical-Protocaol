import streamlit as st
import json

def info_box(icon,label,value):
    st.markdown(f'''
    <div class="info-box">
        <div class="icon-circle">
            <i class="bi {icon}"></i>
        </div>
        <div class="info-content">
            <div class="info-label">{label}</div>
            <div class="info-value">{value}</div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

def show_header():
    with open("data/patient.json","r") as file:
        patient=json.load(file)

    st.markdown('<div class="header">',unsafe_allow_html=True)
    left,center,right=st.columns([1.2,4,1.2])
    with left:
        st.image("assets/habibi.png",width=400)
    with center:
        st.markdown('''<div class="header-title"><h2>Clinical Decision Support</h2><p>Protocol Compliance & Alerting</p></div>''',unsafe_allow_html=True)
    with right:
        st.image("assets/cloud.png",width=145)
    st.markdown("<hr>",unsafe_allow_html=True)
    c1,c2,c3,c4=st.columns(4)
    with c1: info_box("bi-person-fill","Patient",patient["name"])
    with c2: info_box("bi-postcard","MRN",patient["mrn"])
    with c3: info_box("bi-calendar3","Age",patient["age"])
    with c4: info_box("bi-gender-ambiguous","Gender",patient["gender"])
    st.write("")
    c5,c6,c7=st.columns([1.2,2.2,1.2])
    with c5: info_box("bi-building","Ward",patient["ward"])
    with c6: info_box("bi-clipboard2-pulse","Procedure",patient["procedure"])
    with c7: info_box("bi-shield-check","Allergy",patient["allergy"])
    st.markdown("</div>",unsafe_allow_html=True)
    