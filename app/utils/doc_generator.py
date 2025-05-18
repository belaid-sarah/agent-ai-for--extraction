from docx import Document
import os

def generate_word_doc(data: dict, template_path: str, output_path: str):
    doc = Document(template_path)
    
    for p in doc.paragraphs:
        for key, value in data.items():
            placeholder = f"{{{{{key}}}}}"
            if placeholder in p.text:
                p.text = p.text.replace(placeholder, str(value))
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)
