import pandas as pd


from utils.excel_reader import load_excel_with_mapping
from utils.doc_generator import generate_word_doc



from dotenv import load_dotenv
load_dotenv()


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_PATH = os.path.join(BASE_DIR, "data", "Affectation_Resultats.xlsx")
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "Proces-Verbal_AGO_Template.docx")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")


df = load_excel_with_mapping(EXCEL_PATH)

for _, row in df.iterrows():
    data = row.to_dict()
    filename = f"{data['NomSociete'].replace(' ', '_')}_PV.docx"
    output_path = f"{OUTPUT_FOLDER}{filename}"
    generate_word_doc(data, TEMPLATE_PATH, output_path)
    print(f"[✔] Généré : {filename}")
