import streamlit as st
from utils import div_card

def show_skills_tab():
    # Technical Skills
    st.markdown(div_card('''<h3>Technical Skills</h3>''', "tech-skills-header"), unsafe_allow_html=True)
    
    tech_skills = {
        "AI Development": {"RAG Applications": 85, "Chatbot Development": 85, "Prompt Engineering": 85, "AI Pair Programming": 85},
        "Programming Languages": {"Python": 25},
        "Web Development": {"HTML/CSS": 25, "Streamlit": 25},
        "Data Science": {"SQL": 25, "Pandas": 25},
        "Tools & Methods": {"GNU/Linux": 65, "Git": 40, "Visual Studio Code": 60, "GitHub Copilot": 60, "Online Researching": 85, "Writing": 85, "Touch/Blind Typing": 85},
    }
    
    for category, skills in tech_skills.items():
        st.markdown(f"<h4>{category}</h4>", unsafe_allow_html=True)
        for skill, level in skills.items():
            st.markdown(f"<p>{skill}</p>", unsafe_allow_html=True)
            st.progress(level/100)
    
    # Soft Skills
    st.markdown(div_card('''
    <h3>Soft Skills</h3>
    <div class="row" style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px;">
        <div class="skill-tag">Library Management</div>
        <div class="skill-tag">Document Management</div>
        <div class="skill-tag">Leadership</div>
        <div class="skill-tag">Communication</div>
        <div class="skill-tag">Problem Solving</div>
        <div class="skill-tag">Team Collaboration</div>
        <div class="skill-tag">Time Management</div>
        <div class="skill-tag">Adaptability</div>
        <div class="skill-tag">Critical Thinking</div>
        <div class="skill-tag">Creativity</div>
        <div class="skill-tag">Teaching</div>
    </div>
    ''', "soft-skills"), unsafe_allow_html=True)
