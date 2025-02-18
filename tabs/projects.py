import streamlit as st
from utils import div_card

def show_projects_tab():
    
    projects = [
        {
            "title": "Degex",
            "url": "https://www.youtube.com/watch?v=3NV9O5n0VVk&t=48s",
            "description": "A comprehensive Ubuntu-based Live Linux distribution specifically crafted for library professionals. This remaster includes essential Library and Information Science (LIS) tools, with integrated Senayan Library Management System (SLiMS). Built to make Linux accessible and practical for librarians, emphasizing ease of use without requiring installation.",
            "skills": ["GNU/Linux", "System Administration", "Library Systems"]
        },
        {
            "title": "Puppylib",
            "url": "https://www.youtube.com/watch?v=7CBas1TRgRo",
            "description": "A lightweight Puppy Linux remaster optimized for library operations. This distribution packs essential library tools including SLiMS into a compact, resource-efficient system that runs smoothly on older hardware. Perfect for libraries with limited computing resources while maintaining full functionality.",
            "skills": ["GNU/Linux", "System Optimization", "System Administration", "Library Systems"]
        },
        {
            "title": "Poetica",
            "url": "https://poetica.streamlit.app/",
            "description": "Generate beautiful poetry inspired by legendary Indonesian poets such as Sapardi Djoko Damono, Chairil Anwar, Wiji Thukul, WS Rendra, and Sutardji Calzoum Bachri. This app also supports analysis for aesthetic analysis, hermeneutic analysis, and literature analysis.",
            "skills": ["Python", "Streamlit", "Groq as the LLM provider"],
            "link": "https://github.com/cyberarian/poetica"
        },
        {
            "title": "Ask Socrates",
            "url": "https://asksocrates.streamlit.app/",
            "description": "This app gives you the chance to engage in discussions with an AI representation of Socrates, the ancient Greek philosopher renowned for the Socratic Method—his technique of inquiry and questioning. My aim is to recreate his method, guiding you through philosophical questions and challenging your own perspectives.",
            "skills": ["Python", "Streamlit", "Meta-Llama-3.3-70b-versatile"],
            "link": "https://github.com/cyberarian/socrates"
        },
        {
            "title": "Arsipy",
            "url": "https://arsipy.streamlit.app/",
            "description": "AI-powered guide to archive manuals and handwriting analysis",
            "skills": ["Retrieval-Augmented Generation (RAG)", "Python", "Streamlit", "OCR", "Groq as the LLM provider", "Google Gemini 2.0 Flash"],
            "link": "https://github.com/cyberarian/arsipy"
        },
        {
            "title": "FactChecker_ID",
            "url": "https://factcheckerid.streamlit.app/",
            "description": "An open-source tool designed to help users verify information against reliable Wikipedia sources. My goal is to make fact-checking accessible to everyone, supporting multilingual functionality in eight languages, including Indonesian, English, Arabic, French, Spanish, Chinese, Japanese, and Russian.",
            "skills": ["Python", "Streamlit", "OCR", "Groq as the LLM provider", "Google Gemini 2.0 Flash"],
            "link": "https://github.com/cyberarian/factcheckid"
        },
        {
            "title": "PawangData",
            "url": "https://pawangdata.streamlit.app/",
            "description": "a Streamlit-based tool designed for data wrangling and visualization. Aimed at data professionals and enthusiasts, this app provides a seamless interface for handling and transforming datasets, making complex data tasks more manageable. Whether you're cleaning, transforming, or visualizing data, PawangData simplifies the process with intuitive tools and customizable options.",
            "skills": ["Python", "Streamlit", "Pandas", "Groq as the LLM provider", "Google Gemini 2.0 Flash"],
            "link": "https://github.com/cyberarian/PawangData"
        },
        {
            "title": "XperChat",
            "url": "https://xpertchat.streamlit.app/",
            "description": "This chatbot is designed to represent four key domains: Computer Science, Library and Information Science, Archival Studies, and Data Science. My goal is to provide students and the general public with a tool that enhances their understanding and knowledge across these fields through a chat interface.",
            "skills": ["Python", "Streamlit", "Groq as the LLM provider"],
            "link": "https://github.com/cyberarian/xperchat"
        },
        {
            "title": "rt20maninjau",
            "url": "https://rt20maninjau.streamlit.app/",
            "description": "As the Head of the Community (Ketua RT), I am proud to introduce this chatbot, designed to provide community services to our neighborhood.",
            "skills": ["Python", "Streamlit", "RAG", "Groq as the LLM provider"],
            "link": "https://github.com/cyberarian/rt20maninjau"
        },
        {
            "title": "FoodXpert",
            "url": "https://foodxpert.streamlit.app/",
            "description": "Introducing a chatbot that provides expert answers to your academic questions across various fields in food technology.",
            "skills": ["Python", "Streamlit", "Groq as the LLM provider"],
            "link": "https://github.com/cyberarian/foodxpert"
        }
    ]
    
    # Display projects in a grid
    cols = st.columns(3)
    for i, project in enumerate(projects):
        with cols[i % 3]:
            st.markdown(div_card(f'''
            <h3>
                <a href="{project["url"]}" target="_blank" style="color: inherit; text-decoration: none; border-bottom: 2px solid #0096c7;">
                    {project["title"]}
                </a>
            </h3>
            <p>{project["description"]}</p>
            <p><strong>Skills:</strong> {", ".join(project["skills"])}</p>
            {"<a href='" + project.get("link", project["url"]) + "' target='_blank' class='project-link'>" + ("View on GitHub →" if "link" in project else "Watch Demo →") + "</a>"}
            ''', f"project-{i}"), unsafe_allow_html=True)
