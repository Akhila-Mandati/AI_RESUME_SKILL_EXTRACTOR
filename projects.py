# List of project keywords

PROJECTS = [
    "Heart Disease Prediction",
    "AI Resume Skill Extractor",
    "Mobile Market Trend Prediction",
    "Student Management System",
    "Library Management System",
    "Bank Management System",
    "Hospital Management System",
    "Attendance Management System",
    "Face Recognition System",
    "Weather Prediction",
    "Chatbot",
    "E-Commerce Website"
]


def extract_projects(text):
    found_projects = []

    text = text.lower()

    for project in PROJECTS:
        if project.lower() in text:
            found_projects.append(project)

    return sorted(set(found_projects))