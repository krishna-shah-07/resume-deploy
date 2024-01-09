from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Krishna Shah"
PAGE_ICON = ":wave:"
NAME = "Krishna Shah"
DESCRIPTION = """
Machine Learning Engineer | Writer 
"""
EMAIL = "krishnashah131103@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/krishna-shah-104b711a7/",
    "GitHub": "https://github.com/krishna-shah-07",
    "Leetcode": "https://leetcode.com/krish1311/",
    "Twitter": "https://twitter.com/ahiknrs7",
}
PROJECTS = {
    "🏆 Implement BERT Algorithm to enhance product recommendation": "https://github.com/krishna-shah-07/Recommendation_System_BERT",
    "🏆 Spam Email Detection - Research Paper": "https://github.com/krishna-shah-07/SpamEmailDetection",
    "🏆 Machine Learning based Image Fusion": "https://github.com/mohit-2210/Image-Fusion-using-AI-ML",
    "🏆 Income and Expense Tracker - Flutter Application": "https://github.com/krishna-shah-07/Expense_Tracker",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("---")
st.write(
    """
- ✔️ 5+ years of experience working with Python
- ✔️ Strong hands on experience and knowledge in Machine Learning and AI
- ✔️ Working on development of flutter application
- ✔️ Excellent leader and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), JAVA, SQL, FLUTTER
- 📊 Data Visulization: PowerBi, Tableau, MS Excel
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Oracle, MySQL, Firebase, MS SQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Placement Coordinator | Career Development and Placement Cell**")
st.write("January 2024 - Present")
st.write(
    """
- ► Efficient Placement Coordinator ensuring smooth transitions for students into jobs. Connects students with employers, organizes events, and guarantees successful career starts.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Chief Technical Officer (CTO) | Charusat Learning and Development Club**")
st.write("March 2023 - November 2023")
st.write(
    """
- ► As the CTO for AI/ML and Data Science, I have diligently expanded my expertise while leading a collaborative team in executing diverse projects.
- ► This role has allowed me to enhance my knowledge, drive innovation, and deliver impactful solutions in artificial intelligence, machine learning, and data science.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Public Relations coordinator (PR) | GDSC CHARUSAT**")
st.write("August 2022 - July 2023")
st.write(
    """
- ► Handling the participation and engagements of the technical events taking place and learning actively from them.
- ► A part of team handling GDSC CHARUSAT's official LinkedIn page.
- ► Enhanced my technical knowledge and improved my public speaking skills.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Database design / development Intern | Reliance Industries Limited**")
st.write("May 2023 - June 2023")
st.write(
    """
- ► I gained invaluable insights into cooperative sector work and witnessed the collaborative efforts of all team members on various projects.
- ► Taking charge of database designing allowed me to bridge the gap between theoretical knowledge and practical application.
- ► Enhanced my technical knowledge and improved my public speaking skills.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
