import streamlit as st
import os
import sys
from io import BytesIO
from docx import Document

# Corriger le chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils.excel_reader import load_excel_with_mapping
from app.utils.doc_generator import generate_word_doc

st.set_page_config(page_title="Générateur de PV", layout="centered")
st.title("📄 Générateur automatique de Procès-Verbaux")

uploaded_file = st.file_uploader("📥 Uploade ton fichier Excel (.xlsx)", type=["xlsx"])

if uploaded_file:
    st.success("✅ Fichier chargé avec succès")
    
    try:
        df = load_excel_with_mapping(uploaded_file)
        st.dataframe(df)

        if st.button("🚀 Générer les documents Word"):
            os.makedirs("outputs", exist_ok=True)
            st.info("📄 Génération en cours...")

            generated_files = []

            for _, row in df.iterrows():
                data = row.to_dict()
                filename = f"{data['NomSociete'].replace(' ', '_')}_PV.docx"
                output_path = os.path.join("outputs", filename)
                generate_word_doc(data, "templates/Proces-Verbal_AGO_Template.docx", output_path)
                generated_files.append(output_path)

            st.success("✅ Tous les documents ont été générés.")
            st.subheader("📥 Télécharger les documents générés")

            for filepath in generated_files:
                with open(filepath, "rb") as file:
                    file_bytes = file.read()
                    filename = os.path.basename(filepath)
                    st.download_button(
                        label=f"📄 Télécharger {filename}",
                        data=file_bytes,
                        file_name=filename,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

    except Exception as e:
        st.error(f"❌ Erreur lors du traitement : {e}")
