import streamlit as st
from utils import div_card

def show_about_tab():
    st.markdown(div_card('''
    <p style="text-align: justify; line-height: 1.8; margin-bottom: 20px;">
        I am an open source enthusiast who is passionate about libraries and their potential. I have served in various leadership roles across different domains such as law firms, universities, media companies, and the auto care sector. 
    </p>
    <p style="text-align: justify; line-height: 1.8; margin-bottom: 20px;">
        As an advocate of open-source software, I have built (or rather, remastered) two live-Linux distributions based on Puppy Linux and Ubuntu 10.04 LTS (Lucid Lynx). These distributions are packed with numerous library and information science (LIS) software applications.
    </p>
    <p style="text-align: justify; line-height: 1.8;">
        I'm developing a growing interest in Artificial Intelligence (AI) applications that enhance workplace efficiency and decision-making processes. Please refer to my projects on <a href="https://github.com/cyberarian" target="_blank" style="color: #0096c7;">GitHub</a> for examples of this work. See also my Projects page.
    </p>
    ''', "about-me"), unsafe_allow_html=True)