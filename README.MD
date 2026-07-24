# AI Resume Skill Extractor

## Project Overview

AI Resume Skill Extractor is a Streamlit web application that extracts important information from resumes. It analyzes PDF or DOCX resumes and identifies skills, education, and projects, then displays the extracted details in a simple format.

## Features

- Upload PDF or DOCX Resume
- Extract Resume Text
- Extract Skills
- Extract Education
- Extract Projects
- Display Candidate Summary
- Simple and User-Friendly Interface

## Technologies Used

- Python
- Streamlit
- pdfplumber
- python-docx
- pandas

## Project Structure

AI_Resume_Skill_Extractor/
│── app.py
│── resume_parser.py
│── skills.py
│── education.py
│── projects.py
│── requirements.txt
│── README.md
└── resumes/
    └── sample_resume.pdf

## Installation

1. Clone the repository.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

## Screenshots

### Home Page

![alt text](<Screenshot 2026-07-23 213817.png>)

### Resume Upload

![alt text](<Screenshot 2026-07-23 214300.png>)

### Output

![alt text](<Screenshot 2026-07-23 214329.png>)




## Future Enhancements

- Experience Extraction
- Certification Extraction
- Resume Score Analysis
- Export Candidate Summary as PDF

## Author

 Mandati.Akhila