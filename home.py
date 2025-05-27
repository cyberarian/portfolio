import streamlit as st
from PIL import Image
from pathlib import Path
from typing import Optional
from utils import div_card
from tabs import about, experience, education, skills, projects, contact

def load_css(css_file: str) -> None:
    """Load and inject CSS from file."""
    try:
        css_path = Path(__file__).parent / css_file
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading CSS: {e}")

def load_image(image_path: str) -> Optional[Image.Image]:
    """Load image from path with error handling."""
    try:
        return Image.open(image_path)
    except Exception:
        return None

# Page configuration
st.set_page_config(
    page_title="My CV/Resume",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Global Font Configuration ---
google_fonts_and_global_styles = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&family=Tinos:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&display=swap" rel="stylesheet">

<style>
/* Apply Newsreader/Tinos to the entire Streamlit app interface for body text */
html, body, [class*="st-"], [class*="css-"] {
    font-family: 'Newsreader', 'Tinos', serif !important;
}

/* Specifically target headers if you want them to use Newsreader/Tinos as well */
/* Or, you can define a different font like Montserrat for headers if preferred */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Newsreader', 'Tinos', serif !important; /* Default to Newsreader/Tinos */
}

</style>
"""
st.markdown(google_fonts_and_global_styles, unsafe_allow_html=True)

# Load external CSS
load_css('static/styles.css')

def display_header():
    st.markdown('''
    <div style="display: flex; justify-content: center; align-items: center; gap: 20px; padding: 20px 0;">
        <div style="width: 120px; text-align: right;">
            <div style="display: inline-block;">
    ''', unsafe_allow_html=True)
    
    img_path = Path(__file__).parent / "images/profile.png"
    img = load_image(str(img_path))
    if img:
        st.image(img, width=100, use_container_width=False)
    else:
        st.markdown('<div class="profile-img">👤</div>', unsafe_allow_html=True)
    
    st.markdown('''
        </div></div>
        <div>
            <h1 style="font-family: 'Montserrat', sans-serif; font-weight: 700; font-size: 3.2em; margin-bottom: 10px; animation: fadeIn 1.5s;">Adnuri Mohamidi</h1> 
            <p style="font-weight: 500; font-size: 1.5em; color: #bbbbbb; margin: 0; animation: fadeIn 2s;">Helping organizations thrive through smart, tech-driven information stewardship</p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# Main function
def main():
    container = st.container()
    with container:
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            # Display profile image and header
            display_header()
            
            # Create tabs
            tabs = st.tabs(["About Me", "Experience", "Education", "Skills", "Projects", "Contact"])
            
            # Load tab content from separate files
            with tabs[0]: about.show_about_tab()
            with tabs[1]: experience.show_experience_tab()
            with tabs[2]: education.show_education_tab()
            with tabs[3]: skills.show_skills_tab()
            with tabs[4]: projects.show_projects_tab()
            with tabs[5]: contact.show_contact_tab()
            
            # Simplified professional footer
            st.markdown('''
            <div style="text-align: center; margin-top: 30px; padding: 20px; border-top: 1px solid #333;">
                <p style="color: #777; font-size: 0.9em;">© 2025 Adnuri Mohamidi</p>
            </div>
            ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()