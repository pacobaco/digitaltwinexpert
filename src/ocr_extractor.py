import pytesseract
from PIL import Image

class OCRExtractor:
    def extract_text(self, image_path):
        return pytesseract.image_to_string(Image.open(image_path))
