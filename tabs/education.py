import streamlit as st
from utils import div_card

def show_education_tab():
    st.markdown("<h3>Formal education</h3>", unsafe_allow_html=True)
    educations = [
        {
            "degree": "Bachelor's Degree",
            "field": "Library and Information Science",
            "institution": "University of Indonesia",
            "duration": "1996 - 2001"
        }
    ]
    
    for i, edu in enumerate(educations):
        st.markdown(div_card(f'''
        <div class="timeline-item">
            <h3>{edu["degree"]} in {edu["field"]}</h3>
            <h4>{edu["institution"]}</h4>
            <div class="timeline-date">{edu["duration"]}</div>
        </div>
        ''', f"education-{i}"), unsafe_allow_html=True)
    
    # Languages and Certifications without columns
    st.markdown("<h3>Additional Qualifications</h3>", unsafe_allow_html=True)
    
    # Languages section
    st.markdown(div_card('''
    <h3>Languages</h3>
    <div class="row">
        <div><strong>English:</strong> Working-level</div>
    </div>
    ''', "languages"), unsafe_allow_html=True)
    
    # Certifications section
    st.markdown(div_card('''
    <h3>Certifications</h3>
    <ul style="list-style-type: disc; padding-left: 20px; margin-top: 8px;">
        <li>MikroTik Certified Network Associate (MTCNA)  - ID-Networkers (Sep 2022)</li>
        <li>Web Scraping  - Sekolah Stata (July 2022)</li>
        <li>OSINT Beginners course - Kapsuun Group (July 2022)</li>
        <li>Open-source Intelligence (OSINT) - The Basel Institute of Governance (July 2022)</li>
        <li>Reuters Training Course: Introduction to Digital Journalism - Reuters/Meta Journalism Project (July 2022)</li>
        <li>Online Investigative Skills - AFP/Google News Initiative (July 2022)</li>
        <li>Business Intelligence Analyst (BIA) Bootcamp - Binar Academy (Wave 8) (May-Jul 2022)</li>
        <li>Problem Solving and Decisions Making - Prasetiya Mulya Business School (July 2013)</li>
        <li>Linux for Corporate - Ardelindo Linux Institute, Depok (Mar 2007)</li>
        <li>SysAdmin & Networking - Linux Community Center (KPLI Jakarta) (February 2007)</li>
    </ul>
    ''', "certifications"), unsafe_allow_html=True)
