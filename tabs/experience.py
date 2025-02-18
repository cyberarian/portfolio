import streamlit as st
from utils import div_card

def show_experience_tab():
    
    experiences = [
        {
            "title": "Field Researcher",
            "company": "INFID",
            "duration": "Aug – Sep 2022",
            "description": "Conduct and document field interviews, ensuring proper audio/video recording and transcription in accordance with specified protocols, then present all research findings to the committee."
        },
        {
            "title": "Editor (Freelance)",
            "company": "Hallo Lifestyle",
            "duration": "Mar 2022 – Present",
            "description": "Research, develop, and publish news stories while optimizing content for search engines and social media platforms. " +
                         "<a href='https://lifestyle.hallo.id/author/9726/Adnuri-Mohamidi' target='_blank' style='color: #0096c7;'>View articles</a>"
        },
        {
            "title": "Technical Manager",
            "company": '<a href="https://www.viva.co.id/berita/nasional/1438880-inovasi-muncul-di-spbu-ada-alat-pengisian-nitrogen-bak-atm" target="_blank" style="color: #0096c7;">CV Mucha Persada</a>',
            "duration": "May 2021 – Jun 2022",
            "description": '''
                <p>Led project management team for launching three new outlets across West Kalimantan with responsibilities including:</p>
                <ul style="list-style-type: disc; padding-left: 20px; margin-top: 8px;">
                    <li>Ensure the company's operational needs is sufficient (nitrogen, etc)</li>
                    <li>Coordination with partners and vendors (Widya Robotics, Pertamina Retail, Samator, Jasa Marga, Gas Stations, etc)</li>
                    <li>Ensure the machine is functioning properly for daily use</li>
                    <li>Monitor daily revenue through web-based dashboard</li>
                    <li>Prepare machines, operators, booths for opening plans in the new location</li>
                </ul>
            '''
        },
        {
            "title": "Deputy of Research & Information Center",
            "company": "English Daily The Jakarta Post",
            "duration": "Jul 2011 – Feb 2021",
            "description": "Managed the daily operations of the library, ensuring seamless delivery of all services."
        },
        {
            "title": "Reference Librarian",
            "company": "English Daily The Jakarta Post",
            "duration": "Feb 2002 – Jun 2011",
            "description": "Led data support services including infographics and fact-checking while training reporters on research methods. Managed IPTC-compliant data warehouse and content management system, while implementing Senayan Library Management System (SLiMS) for efficient collection organization."
        },
        {
            "title": "Acting chief of the Library",
            "company": "the Interdisciplinary Postgraduate Library of UI (Salemba campus)",
            "duration": "Oct 2001 – Feb 2002",
            "description": "Revitalized a dormant library by establishing its infrastructure, implementing a comprehensive library system, and overseeing its ongoing operation."
        },
        {
            "title": "Scanner Operator",
            "company": "Lubis Ganie Surowidjojo (LGS) Law Firm",
            "duration": "Nov 2000 – Sep 2001",
            "description": "This project focused on digitizing a treasure trove of legal documents, breathing new life into historical records for easier access and preservation."
        }
    ]
    
    for i, exp in enumerate(experiences):
        st.markdown(div_card(f'''
        <div class="timeline-item" style="margin-bottom: 8px;">
            <h3 style="margin-bottom: 4px;">{exp["title"]} at {exp["company"]}</h3>
            <div class="timeline-date">{exp["duration"]}</div>
            <p style="margin-top: 6px;">{exp["description"]}</p>
        </div>
        ''', f"experience-{i}"), unsafe_allow_html=True)
