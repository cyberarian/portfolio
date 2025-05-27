import streamlit as st
from utils import div_card
import re # Import the 're' module for regular expressions

def highlight_keywords(text, keywords, color="blue"):
    """
    Wraps specified keywords in a text with a span tag for highlighting.
    Uses regex to ensure whole word matching and case-insensitivity.
    """
    for keyword in keywords:
        # Use regex to find whole words, case-insensitive
        # The \b ensures word boundaries, so 'OCR' doesn't match 'OCREAN'
        # re.escape handles special characters in keywords
        pattern = r"\b(" + re.escape(keyword) + r")\b"
        replacement = f'<span style="color: {color}; font-weight: bold;">\\1</span>'
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def show_about_tab():
    keywords_to_highlight = [
        "librarianship", "information organization", "managing records",
        "documents", "knowledge assets", "OCR", "IDP",
        "IDocspy", "OCEARIN", "Arsipy", "document analysis",
        "records handling", "knowledge validation", "open-source tools",
        "digital documentation", "document control", "records management",
        "information governance", "knowledge management", "metadata",
        "classification", "compliance", "information integrity"
    ]
    highlight_color = "#0eeb58" # A bright green color

    original_html_content = '''
   <p style="text-align: justify; line-height: 1.8; margin-bottom: 20px;">
   With a professional background in librarianship and a strong interest in information organization, I have developed a solid foundation in managing records, documents, and knowledge assets across sectors such as media, legal services, education, and automotive care. My work has focused on structuring, classifying, and maintaining information to support access, compliance, and strategic use. 
   </p>
   <p style="text-align: justify; line-height: 1.8; margin-bottom: 20px;">
   I have explored various OCR and intelligent document processing (IDP) techniques to enhance workflows involving documentation, verification, and structured content extraction. Through self-initiated projects like IDocspy (an IDP tool), OCEARIN (an OCR evaluation framework), and Arsipy (AI-powered guide to archive manuals from trusted sources), I have built practical solutions that address real-world challenges in document analysis, records handling, and knowledge validation.
   </p>
   <p style="text-align: justify; line-height: 1.8;">
    While I am not a technical specialist by formal training, I actively engage with open-source tools and digital documentation practices. I am now seeking to transition into a career path spanning document control, records management, information governance, or knowledge management, where I can apply my skills in metadata, classification, compliance, and information integrity to support organizational effectiveness.
   </p>
   <p>Please refer to my repos on <a href="https://github.com/cyberarian" target="_blank" style="color: #c70000;">GitHub</a> for examples of my works. See also my Projects page.
   </p>
    '''

    highlighted_content = highlight_keywords(original_html_content, keywords_to_highlight, highlight_color)

    st.markdown(div_card(highlighted_content, "about-me"), unsafe_allow_html=True)