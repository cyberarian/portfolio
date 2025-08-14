import streamlit as st
import pandas as pd
from utils import div_card

def show_projects_tab():
    projects = [
        {
            "title": "WaskitaHusada",
            "url": "https://s.id/waskitahusada",
            "description": "a medical chatbot app providing educational information and assistance. It uses Llama3-OpenBioLLM-70B designed for biomedical domain and Gemini1.5 Flash for accurate translation. Tested with MedQA dataset.",
            "skills": ["Chatbot", "Shiny", "Gemini 1.5 Flash", "Llama3-OpenBioLLM-70B"],
            "link": "https://github.com/cyberarian/waskita"
        },
        {
            "title": "IDocspy",
            "url": "https://s.id/idocspy",
            "description": "an Intelligent Document Processing and Understanding. IDocspy is expected to contribute strategically as a complementary component that enhances the functionality of EDRMS.",
            "skills": ["OCR", "Streamlit", "gemini-2.5-flash-preview-04-17", "Mistral-OCR"],
            "link": "https://github.com/cyberarian/ocearin"
        },
        {
            "title": "OCEARIN",
            "url": "https://s.id/ocearin",
            "description": "OCR evaluator with Vision Language Models (VLMs). VLMs can interpret text in its context more accurately, better understand the structure of tables and forms, and analyze visual elements to gain deeper insights.",
            "skills": ["OCR", "Streamlit", "gemini-2.5-flash-preview-04-17", "Mistral-OCR"],
            "link": "https://github.com/cyberarian/ocearin"
        },
        {
            "title": "Arsipy",
            "url": "https://arsipy.streamlit.app/",
            "description": "AI-powered guide to archive manuals from trusted sources",
            "skills": ["Retrieval-Augmented Generation (RAG)", "Streamlit", "OCR", "Groq as the LLM provider", "Google Gemini 2.0 Flash"],
            "link": "https://github.com/cyberarian/arsipy"
        },
        {
            "title": "Ask Socrates",
            "url": "https://asksocrates.streamlit.app/",
            "description": "This app gives you the chance to engage in discussions with an AI representation of Socrates, renowned for his technique of inquiry and questioning. My aim is to recreate his method, guiding you through philosophical questions and challenging your own perspectives.",
            "skills": ["Python", "Streamlit", "Meta-Llama-3.3-70b-versatile"],
            "link": "https://github.com/cyberarian/socrates"
        },
        {
            "title": "FactChecker_ID",
            "url": "https://factcheckerid.streamlit.app/",
            "description": "An open-source tool designed to help users verify information against reliable Wikipedia sources and supported by image analysis. My goal is to make fact-checking accessible to everyone, supporting multilingual functionality in eight languages.",
            "skills": ["Python", "Streamlit", "OCR", "Groq as the LLM provider", "Google Gemini 2.0 Flash"],
            "link": "https://github.com/cyberarian/factcheckid"
        },
        {
            "title": "PawangData",
            "url": "https://pawangdata.streamlit.app/",
            "description": "a simple tool designed for data wrangling and visualization, making complex data tasks more manageable. Whether you're cleaning, transforming, or visualizing data, PawangData simplifies the process with intuitive tools and customizable options.",
            "skills": ["Python", "Streamlit", "Pandas", "Groq as the LLM provider", "Google Gemini 2.0 Flash"],
            "link": "https://github.com/cyberarian/PawangData"
        },
        {
            "title": "Degex",
            "url": "https://www.youtube.com/watch?v=3NV9O5n0VVk&t=48s",
            "description": '''A comprehensive Ubuntu-based Live Linux distribution specifically crafted for library professionals. This remastered edition includes over 25 essential tools for Library and Information Science (LIS), seamlessly integrated with the Senayan Library Management System (SLiMS). Built to make Linux accessible and practical for librarians, emphasizing ease of use without requiring installation.<div class="coverage-section"><details><summary>Webpage Coverage</summary><div class="coverage-links"><ul><li><a href="https://ugos.ugm.ac.id/2010/12/29/workshop-series-pelatihan-degex-dan-instalasi-linux-bagi-%20pustakawan-dan-umum/" target="_blank">UGM Workshop Coverage</a></li><li><a href="http://ovanmulia.wordpress.com/2011/01/12/aplikasi-open-source-untuk-pustakawan/" target="_blank">Open Source Apps for Librarians</a></li><li><a href="http://desawarna.blogspot.com/2011/02/ada-linux-degex-di-perpustakaan.html" target="_blank">Degex in Libraries</a></li><li><a href="http://jogjalib.blogspot.com/2010/10/degex-linux-distribution-with-lis-apps.html" target="_blank">Jogjalib Review</a></li></ul></div></details></div>''',
            "skills": ["GNU/Linux", "System Administration", "Library Systems"],
            "link": "none"
        },
        {
            "title": "Puppylib",
            "url": "https://www.youtube.com/watch?v=7CBas1TRgRo",
            "description": '''A lightweight Puppy Linux remaster was optimized for library operations. This distribution packed essential library tools, including SLiMS, into a compact, resource-efficient system that ran smoothly on older hardware. Perfect for libraries with limited computing resources, it maintained full functionality without compromising performance.<div class="coverage-section"><details><summary>Webpage Coverage</summary><div class="coverage-links"><ul><li><a href="http://puppylinux.org/main/Puplet%20for%20special%20features.htm" target="_blank">PuppyLinux.org Feature</a></li><li><a href="http://murga-linux.com/puppy/viewtopic.php?t=59919" target="_blank">Murga Linux Forum</a></li><li><a href="http://obiblio.sourceforge.net/index.php/Main/Gallery" target="_blank">OpenBiblio Gallery</a></li><li><a href="http://www.purwo.co/2009/07/puppylib-linux-livecd-rasa-perpustakaan.html" target="_blank">Purwo.co Review</a></li><li><a href="https://gadgetboi.wordpress.com/2009/09/01/distro-linux-lokal-part-2-mengenal-lebih-jauh-" target="_blank">GadgetBoi Review</a></li><li><a href="https://pkbmedukasi.wordpress.com/links/daftar-distro-linux-lokal/" target="_blank">Local Linux Distro List</a></li><li><a href="https://archive.org/browse.php?field=subject&mediatype=software&collection=linux_distributio%20ns" target="_blank">Internet Archive</a></li><li><a href="https://toko.baliwae.com/product_info.php?products_id=1632" target="_blank">Baliwae Store</a></li></ul></div></details></div>''',
            "skills": ["GNU/Linux", "System Optimization", "System Administration", "Library Systems"],
            "link": "none"
        },
        {
            "title": "Poetica",
            "url": "https://s.id/poettica",
            "description": "Generate beautiful poetry inspired by legendary Indonesian poets such as Sapardi Djoko Damono, Chairil Anwar, Wiji Thukul, WS Rendra, and Sutardji Calzoum Bachri. This app also supports analysis for aesthetic analysis, hermeneutic analysis, and literature analysis.",
            "skills": ["Python", "Streamlit", "Groq as the LLM provider"],
            "link": "https://github.com/cyberarian/poetica"
        },
        {
            "title": "XpertChat",
            "url": "https://xpertchat.streamlit.app/",
            "description": "This chatbot is designed to represent four key domains: Computer Science, Library and Information Science, Archival Studies, and Data Science. My goal is to provide students and the general public with a tool that enhances their understanding and knowledge across these fields through a chat interface.",
            "skills": ["Python", "Streamlit", "Groq as the LLM provider"],
            "link": "https://github.com/cyberarian/xpertchat"
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
        },
        {
            "title": "KYCPy",
            "url": "https://knowyourcustomer.streamlit.app/",
            "description": "The KYCPy platform represents a comprehensive solution for Know Your Customer (KYC) processes in banking institutions. Our AI-powered document verification system leverages Google's Gemini AI technology to provide advanced document processing capabilities.",
            "skills": ["OCR", "Python", "Streamlit", "Gemini Flash"],
            "link": "https://github.com/cyberarian/KYCPy"
        }        
    ]
    
    # Convert projects to DataFrame
    df = pd.DataFrame(projects)
    
    # Format skills as comma-separated strings
    df['skills'] = df['skills'].apply(lambda x: ', '.join(x))
    
    # Create clickable links with styling (fixed formatting)
    df['title'] = df.apply(lambda x: 
        f'<h4 style="margin:0"><a href="{x["url"]}" target="_blank" style="color: inherit; text-decoration: none; border-bottom: 2px solid #0096c7;">{x["title"]}</a></h3>', 
        axis=1
    )

    # Style repository links
    df['repository'] = df.apply(
        lambda x: f'<a href="{x.get("link", x["url"])}" target="_blank" class="project-link" style="color: #0096c7;">{"View on GitHub →" if x.get("link") and x["link"] != "none" else "Watch Demo →" if x["link"] != "none" else ""}</a>', 
        axis=1
    )

    # Reorder and rename columns
    df = df[['title', 'description', 'skills', 'repository']]
    df.columns = ['Project', 'Description', 'Technologies', 'Links']
    
    # Display the DataFrame with HTML
    st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    # CSS for this table is now expected to be in static/styles.css
    # and loaded by home.py
    pass
