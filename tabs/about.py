import streamlit as st
from utils import div_card

def show_about_tab():
    st.markdown(div_card('''
   <p style="text-align: justify; line-height: 1.8; margin-bottom: 20px;">
   With a background in librarianship and a strong interest in information organization, I have developed a keen understanding of managing and structuring records across sectors such as media, legal services, education, and automotive care. 
   </p>
   <p style="text-align: justify; line-height: 1.8; margin-bottom: 20px;">
   I have explored various OCR techniques to extract structured content from documents and enhance documentation and verification workflows. Through self-initiated projects like IDocspy—an intelligent document processing (IDP) tool, OCEARIN—an OCR evaluation framework, and Factchecker_ID—a multilingual information verification assistant—I’ve developed practical solutions that address real-world challenges in document analysis and fact-checking.
   </p>
   <p style="text-align: justify; line-height: 1.8;">
    Though not a technical specialist, I’m passionate about open-source tools and digital documentation practices. I am now seeking to transition into a career in document control, where I can apply my skills in classification, compliance, and information integrity in a professional setting. Please refer to my repos on <a href="https://github.com/cyberarian" target="_blank" style="color: #0096c7;">GitHub</a> for examples of my works. See also my Projects page.
   </p>
    ''', "about-me"), unsafe_allow_html=True)