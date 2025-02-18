import streamlit as st
from utils import div_card

def show_projects_tab():
    
    projects = [
        {
            "title": "Degex",
            "url": "https://www.youtube.com/watch?v=3NV9O5n0VVk&t=48s",
            "description": '''
                A comprehensive Ubuntu-based Live Linux distribution specifically crafted for library professionals. This remaster includes essential Library and Information Science (LIS) tools, with integrated Senayan Library Management System (SLiMS). Built to make Linux accessible and practical for librarians, emphasizing ease of use without requiring installation.
                <div style="margin-top: 10px;">
                    <details>
                        <summary style="color: #0096c7; cursor: pointer;">Webpage Coverage</summary>
                        <ul style="margin-top: 8px;">
                            <li><a href="https://ugos.ugm.ac.id/2010/12/29/workshop-series-pelatihan-degex-dan-instalasi-linux-bagi-%20pustakawan-dan-umum/" target="_blank">UGM Workshop Coverage</a></li>
                            <li><a href="http://ovanmulia.wordpress.com/2011/01/12/aplikasi-open-source-untuk-pustakawan/" target="_blank">Open Source Apps for Librarians</a></li>
                            <li><a href="http://desawarna.blogspot.com/2011/02/ada-linux-degex-di-perpustakaan.html" target="_blank">Degex in Libraries</a></li>
                            <li><a href="http://jogjalib.blogspot.com/2010/10/degex-linux-distribution-with-lis-apps.html" target="_blank">Jogjalib Review</a></li>
                        </ul>
                    </details>
                </div>
            ''',
            "skills": ["GNU/Linux", "System Administration", "Library Systems"]
        },
        {
            "title": "Puppylib",
            "url": "https://www.youtube.com/watch?v=7CBas1TRgRo",
            "description": '''
                A lightweight Puppy Linux remaster optimized for library operations. This distribution packs essential library tools including SLiMS into a compact, resource-efficient system that runs smoothly on older hardware. Perfect for libraries with limited computing resources while maintaining full functionality.
                <div style="margin-top: 10px;">
                    <details>
                        <summary style="color: #0096c7; cursor: pointer;">Webpage Coverage</summary>
                        <ul style="margin-top: 8px;">
                            <li><a href="http://puppylinux.org/main/Puplet%20for%20special%20features.htm" target="_blank">PuppyLinux.org Feature</a></li>
                            <li><a href="http://murga-linux.com/puppy/viewtopic.php?t=59919" target="_blank">Murga Linux Forum</a></li>
                            <li><a href="http://obiblio.sourceforge.net/index.php/Main/Gallery" target="_blank">OpenBiblio Gallery</a></li>
                            <li><a href="http://www.purwo.co/2009/07/puppylib-linux-livecd-rasa-perpustakaan.html" target="_blank">Purwo.co Review</a></li>
                            <li><a href="https://gadgetboi.wordpress.com/2009/09/01/distro-linux-lokal-part-2-mengenal-lebih-jauh-" target="_blank">GadgetBoi Review</a></li>
                            <li><a href="https://pkbmedukasi.wordpress.com/links/daftar-distro-linux-lokal/" target="_blank">Local Linux Distro List</a></li>
                            <li><a href="https://archive.org/browse.php?field=subject&mediatype=software&collection=linux_distributio%20ns" target="_blank">Internet Archive</a></li>
                            <li><a href="https://toko.baliwae.com/product_info.php?products_id=1632" target="_blank">Baliwae Store</a></li>
                        </ul>
                    </details>
                </div>
            ''',
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
