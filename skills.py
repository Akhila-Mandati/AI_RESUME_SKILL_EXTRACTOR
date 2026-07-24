# List of predefined skills

SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "SQL",
    "MySQL",
    "Oracle",
    "MongoDB",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "NLP",
    "TensorFlow",
    "Scikit-learn",
    "Git",
    "GitHub",
    "Streamlit",
    "Django",
    "Flask"
]


def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(set(found_skills))