from pathlib import Path

import streamlit as st
from PIL import Image

current_path = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_path / "styles" / "main.css"
resume_file = current_path / "assets" / "CV.pdf"
profile_pic = current_path / "assets" / "prof_pic.png"

NAME = "VLADIMER GARANCHO"
SUB_TITLE = "Aspiring Data Analyst/Document Controller"
PAGE_TITLE = "Digital CV | Vladimer Garancho"
PAGE_ICON = ":wave:"
DESCRIPTION = '''
Dynamic and detail oriented with 14+ experience in handling and managing
documentations on construction industry. Having some transferable skills that
meet the current requirements for the data related jobs. Adept at receiving and
monitoring data from multiple data streams, including Access, SQL, and Excel
data sources. Proven track record of generating summary documents for senior
management for monthly and quarterly audit and compliance reporting. Versatile
and fast learner with less to none supervision.'''
EMAIL = "amerlitong@yahoo.com"
SOC_MED = {
  "LinkedIn" : "https://www.linkedin.com/in/vladimer-garancho-98b66270/",
  "Facebook" : "https://www.facebook.com/amer.garancho/",
  "Github" : "https://github.com/amerlitong/",
  "Projects" : "https://www.google.com.ph/"
}

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

with open(css_file) as f:
  st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
  PDFfile = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1,col2 = st.columns(2)
with col1:
  st.image(profile_pic,width=450)

with col2:
  st.title(NAME)
  st.caption(SUB_TITLE)
  st.write(DESCRIPTION)
  st.download_button(
    label = 'Download Resume',
    data = PDFfile,
    file_name = resume_file.name,
    mime = 'application/octet-stream',
  )
  st.write(EMAIL)

cols = st.columns(len(SOC_MED))

for i,(k,v) in enumerate(SOC_MED.items()):
  cols[i].write(f'[{k}]({v})')
  
st.write('---')
st.header('QUALIFICATION')
st.write('''
  - PCEP (Python Certified Entry Level Programmer)
  - Google Data Analyst
  - IBM Data Analyst
  - MOS (Microsoft Office Specialist) Excel 2013
  - Comptia A+
  ''')

st.write('---')
st.header('SKILLS')
st.subheader('Technical')
st.write('''
- Programming (Python/VBA/SQL)
- Database (MS Access/SQLite/Spreadsheet)
- Data Management (Data collection, organize and manage including cleaning and transforming)
- Data Visualization (Tableau/PowerBI/Excel/Plotly)
- MS Office Suite
- Inhouse Electronic Document Management System(EDMS)
''')

st.subheader('Soft')
st.write('''
- Attention to detail
- Problem solving
- Analythical thinking
- Organization
- Communication
''')

st.write('---')
st.header('WORK HISTORY')
st.subheader('Document Controller/Punchlist Controller, Tecnicas Reunidas, Al-Ahmadi, Kuwait')
st.text('Jan. 2018 - Feb. 2022')
st.write('''
- Successfully handover all the required client approved construction dossiers
to KNPC earlier than the scheduled turnover.
- Developed and managed inspection and test package punchlist database
(Access).
- In-house application operator for piping and welding tracking system and
extraction of ICAPS punchlist for elimination of redundant punch items.
- Reduced document turnaround time by 15% and enabled a 10% increase in
project completion rate.
- Developed document control system that ensured electronic tracking and
version control of key project documents.
- Automated database maintenance and document audit processes ensuring
requirements are met and streamlined.
- Managed and monitored document distribution ensuring all requirements are
met and approvals are obtained.
- Established a clear naming standard and tracked the storage location of all
documentation utilizing the database.
''')

st.subheader('Document Controller, Hyundai Engineering and Construction, Shuaiba, Kuwait')
st.text('Nov. 2012 - Dec. 2017')
st.write('''
- Review and prepare of required dossiers for turnover to the client (KOC).
- Piping reports (welding/NDT) and files management.
- Test package punchlist tracking. In-house application operator for piping and
welding tracking system.
- Responsible for assigning test package details on the system.
- Scanning and filing QC related reports.
- Developed document control system that ensured electronic tracking and
version control of key project documents.
- Automated database maintenance and document audit processes ensuring
requirements are met and streamlined.
- Managed and monitored document distribution ensuring all requirements are
met and approvals are obtained.
- Established a clear naming standard and tracked the storage location of all
documentation utilizing the database
''')

st.subheader('Document Controller, Hyundai Engineering and Construction, Khursaniya, Kingdom of Saudi Arabia')
st.text('Apr. 2010 - Jun. 2012')
st.write('''
- Piping drawings (Isometric/P&ID) filing and arrangement.
- In-house application operator for piping and welding tracking system.
- Responsible for assigning test package details on the system.-Established a clear naming standard and tracked the storage location of all
documentation utilizing the database.
''')

st.subheader('Computer Operator, Kentz, Jubail, Kingdom of Saudi Arabia')
st.text('Oct. 2007 - Nov. 2009')
st.write('''
- Assisting on material take-offs on electrical and instrumentation drawings.
- Clerical works and file managements.
- Daily manpower and man hours reporting.
''')

st.write('---')
st.header('EDUCATION')
st.subheader('BS Computer Engineering, AMA Computer University, Davao City, Philippines')
st.text('May 2002 - Jun. 2006')

st.write('---')
st.header('PROJECTS AND ACCOMPLISHMENTS')