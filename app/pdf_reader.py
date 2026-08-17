from pypdf import PdfReader


def read_pdf(file_path):

    try:

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if not text.strip():
            return "No readable text found in the PDF."

        return text

    except Exception as e:

        return f"Error reading PDF: {e}"