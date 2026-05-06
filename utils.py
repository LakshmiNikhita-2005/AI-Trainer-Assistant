from pypdf import PdfReader
import docx

def extract_text(file):

    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text

    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text

    else:
        return file.read().decode("utf-8")