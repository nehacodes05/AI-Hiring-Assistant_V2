from pypdf import PdfReader


# helper function for extracting text for Ai analysis


def extract_text_from_pdf(filepath):

    # open pdf located at this filepath
    reader = PdfReader(filepath)

    text = ""

    # read every page bcus resume can have multipage
    for page in reader.pages:
        extracted_text = page.extract_text()

        # some pages may not contain extractable text(ie images,scanned documents)
        if extracted_text:
            text += extracted_text
    return text
