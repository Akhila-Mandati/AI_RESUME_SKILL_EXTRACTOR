# List of education keywords

EDUCATION = [
    "SSC",
    "10th",
    "Intermediate",
    "12th",
    "Diploma",
    "B.Tech",
    "B.E",
    "B.Sc",
    "BCA",
    "B.Com",
    "BA",
    "MCA",
    "M.Tech",
    "MBA",
    "M.Sc",
    "PhD"
]


def extract_education(text):
    found_education = []

    text = text.lower()

    for course in EDUCATION:
        if course.lower() in text:
            found_education.append(course)

    return sorted(set(found_education))