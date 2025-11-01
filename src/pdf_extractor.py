def extract_text_from_pdf(uploaded_file):
    import fitz  # PyMuPDF
    # Use uploaded_file as a file-like object
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text
