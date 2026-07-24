import pdfplumber
from docx import Document


def extract_text(uploaded_file):
    file_name = uploaded_file.name.lower()

    # Read PDF
    if file_name.endswith(".pdf"):
        text = ""

        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    # Read DOCX
    elif file_name.endswith(".docx"):
        doc = Document(uploaded_file)

        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    else:
        return "Unsupported File Format"