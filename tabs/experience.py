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
            "title": "(Freelance) Editor",
            "company": "Hallo Lifestyle",
            "duration": "Mar 2022 – Present",
            "description": "Research, develop, and publish news stories while optimizing content for search engines and social media platforms. " +
                         "<a href='https://lifestyle.hallo.id/author/9726/Adnuri-Mohamidi' target='_blank' style='color: #0096c7;'>View articles</a>"
        },
        {
            "title": "Technical Manager",
            "company": "CV Mucha Persada",
            "duration": "May 2021 – Jun 2022",
            "description": '''Led project management team for launching three new outlets across West Kalimantan: Pontianak, Mempawah, Sintang.
            <div style="margin-top: 10px;">
                    <details>
                        <summary style="color: #0096c7; cursor: pointer;">Media Coverage</summary>
                        <ul style="margin-top: 8px;">
                        <li><a href="https://widya.ai/widya-robotics-sebagai-distributor-resmi-my-nitro/" target="_blank">Widya Robotics</a></li>
                            <li><a href="https://www.viva.co.id/berita/nasional/1438880-inovasi-muncul-di-spbu-ada-alat-pengisian-nitrogen-bak-atm" target="_blank">Viva.co.id</a></li>
                            <li><a href="https://www.gridoto.com/read/222261823/mau-punya-bisnis-outlet-nitrogen-siapkan-modal-segini" target="_blank">Gridoto</a></li>
                            <li><a href="https://www.gridoto.com/read/222260688/isi-nitrogen-kini-bisa-transaksi-non-tunai-segini-harganya" target="_blank">Gridoto</a></li>
                            <li><a href="https://www.motorplus-online.com/read/252263227/menggiurkan-bisnis-outlet-nitrogen-modalnya-terjangkau-omzet-perbulannya-tembus-rp-30-jutaan" target="_blank">Motorplus</a></li>
                            <li><a href="https://www.liputan6.com/otomotif/read/4315647/harganya-lebih-mahal-ini-keunggulan-nitrogen-dibanding-angin-biasa" target="_blank">Liputan6</a></li>
                            <li><a href="https://autonetmagz.com/my-nitro-isi-nitrogen-self-service-bayarnya-cashless/107262/" target="_blank">Autonetmagz</a></li>
                            <li><a href="https://mobilkomersial.com/2020/07/17/profil-pemilik-my-nitro-muchlis-bisa-isi-angin-ban-nitrogen-dengan-cashless-dan-self-service/" target="_blank">Mobilkomersial</a></li>
                            <li><a href="https://www.merdeka.com/otomotif/mynitro-cara-isi-ban-kendaraan-dengan-nitrogen-murni-yang-canggih-nontunai.html" target="_blank">Merdeka.com</a></li>
                        </ul>
                    </details>
                </div>
        '''
        },
        {
            "title": "Deputy of Research & Information Center",
            "company": "The Jakarta Post (Indonesia’s leading English-language daily)",
            "duration": "Jul 2011 – Feb 2021",
            "description": "Managed the library, its related services, and supervised three staff members to ensure the smooth operation of daily tasks. " +
                          "<a href='https://www.thejakartapost.com/news/2014/03/26/did-you-know-christian-based-political-parties.html' target='_blank' style='color: #0096c7;'>My article</a>"
        },
        {
            "title": "Reference Librarian",
            "company": "The Jakarta Post (Indonesia’s leading English-language daily)",
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
