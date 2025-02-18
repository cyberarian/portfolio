import streamlit as st
from utils import div_card

def show_contact_tab():
    st.markdown("<h2>Contact Me</h2>", unsafe_allow_html=True)
    
    # Contact channels
    st.markdown(div_card('''
    <p>Feel free to reach out to me through:</p>
    <div class="contact-links">
        <a href="mailto:cyberariani@gmail.com" class="contact-item">
            <div class="contact-icon">📧</div>
            <span>Email</span>
        </a>
        <a href="https://github.com/cyberarian" target="_blank" class="contact-item">
            <div class="contact-icon">🐙</div>
            <span>GitHub</span>
        </a>
    </div>
    ''', "contact-info"), unsafe_allow_html=True)
    
    # Availability
    st.markdown(div_card('''
    <h3>Availability</h3>
    <p>I am currently <span style="color: #4CAF50;">available</span> for collaborations and opportunities, and I would be delighted to explore new possibilities.</p>
    <p>Preferred work type: Full-time / Contract / Project</p>
    ''', "availability"), unsafe_allow_html=True)
