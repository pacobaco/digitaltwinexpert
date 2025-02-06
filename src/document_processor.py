import pdfplumber
import docx

class DocumentProcessor:
    def process(self, doc_paths):
        results = []
        for path in doc_paths:
            text = ""
            ext = path.split('.')[-1].lower()
            if ext == "pdf":
                with pdfplumber.open(path) as pdf:
                    text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            elif ext == "docx":
                doc = docx.Document(path)
                text = " ".join([para.text for para in doc.paragraphs])
            else:
                with open(path, 'r', encoding='utf-8') as file:
                    text = file.read()
            results.append({"path": path, "text": text})
        return results
