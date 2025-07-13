import fitz  # PyMuPDF

def load_document(file):
    if file.type == "application/pdf":
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join(page.get_text() for page in doc)
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    else:
        return "Unsupported file format"
