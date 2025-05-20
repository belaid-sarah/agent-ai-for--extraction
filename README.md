# 📄 Agent IA de Remplissage Automatique de Documents Juridiques

## 🎯 Objectif

Ce projet vise à automatiser la génération de documents juridiques, notamment les **Procès-Verbaux d'Assemblées Générales**, à partir de données comptables issues d'un fichier Excel et d'un modèle Word.  
L'objectif est de faciliter le traitement de gros volumes de documents, de réduire les erreurs humaines et de garantir la conformité légale.

---

## 🧱 Architecture du projet
auto-legal-agent/
├── app/
│ ├── main.py # Script principal
│ └── utils/
│ ├── excel_reader.py # Lecture Excel + mapping dynamique
│ ├── doc_generator.py # Remplissage du modèle Word
│ └── ai_assistant.py # (optionnel) Appels à Gemini ou GPT
│
├── interface/
│ └── streamlit_app.py # Interface utilisateur avec Streamlit
│
├── templates/
│ └── Proces-Verbal_AGO_Template.docx
├── data/
│ └── Affectation_Resultats.xlsx # Jeu de données de test
├── outputs/
│ └── (fichiers Word générés)
├── .env 
├── requirements.txt
└── README.md



---

## ⚙️ Stack technique

- **Langage** : Python 3.11+
- **Librairies** :
  - `pandas` pour la lecture du fichier Excel
  - `openpyxl` pour gérer les `.xlsx`
  - `python-docx` pour manipuler les fichiers Word
  - `streamlit` pour l’interface utilisateur
  - `difflib` pour le mapping intelligent des colonnes
  - `dotenv`, `requests` (si intégration LLM)
- **Option IA** : Gemini ou OpenAI (structure prête)

---

## 🚀 Lancer le projet

### 1. Installation des dépendances

```bash
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
pip install -r requirements.txt
streamlit run interface/streamlit_app.py


