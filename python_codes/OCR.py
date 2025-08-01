import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import os

# Set path to tesseract.exe (Windows only)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Function to extract text from an image
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# Example usage
if __name__ == "__main__":
    # PDF Extraction
    pdf_file = "sample.pdf"
    if os.path.exists(pdf_file):
        pdf_text = extract_text_from_pdf(pdf_file)
        print(" Text extracted from PDF:\n", pdf_text)
    else:
        print("PDF file not found:", pdf_file)

    # Image Extraction
    image_file = "sample_image.jpg"
    if os.path.exists(image_file):
        image_text = extract_text_from_image(image_file)
        print("\n Text extracted from Image:\n", image_text)
    else:
        print("Image file not found:", image_file)
