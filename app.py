import streamlit as st
from resume_parser import extract_text
from skills import extract_skills
from education import extract_education
from projects import extract_projects

# Page Configuration
st.set_page_config(page_title="AI Resume Skill Extractor")

# Title
st.title("📄 AI Resume Skill Extractor")

st.write("Upload your resume (PDF or DOCX) to extract skills, education, and projects.")

# File Upload
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file is not None:

    st.success("Resume Uploaded Successfully!")

    # Extract Text
    text = extract_text(uploaded_file)

    st.subheader("📃 Resume Text")
    st.text_area("Resume Content", text, height=250)

    # Extract Skills
    skills = extract_skills(text)

    st.subheader("💻 Skills")
    if skills:
        for skill in skills:
            st.write("✅", skill)
    else:
        st.write("No skills found.")

    # Extract Education
    education = extract_education(text)

    st.subheader("🎓 Education")
    if education:
        for course in education:
            st.write("🎓", course)
    else:
        st.write("No education found.")

    # Extract Projects
    projects = extract_projects(text)

    st.subheader("📂 Projects")
    if projects:
        for project in projects:
            st.write("📌", project)
    else:
        st.write("No projects found.")

    # Candidate Summary
    st.subheader("📋 Candidate Summary")

    st.write("### Skills")
    for skill in skills:
        st.write("-", skill)

    st.write("### Education")
    for course in education:
        st.write("-", course)

    st.write("### Projects")
    for project in projects:
        st.write("-", project)