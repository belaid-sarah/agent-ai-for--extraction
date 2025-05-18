import pandas as pd
from difflib import get_close_matches

# Liste des colonnes attendues
PLACEHOLDER_KEYS = [
    "NomSociete", "FormeJuridique", "CapitalSocial", "AdresseSiegeSocial",
    "DateClotureExercice", "ResultatNetComptable", "ReservesAnterieures",
    "PropositionAffectation", "MontantAffecteReserves",
    "MontantDividendes", "MontantReportANouveau", "DateAssemblee"
]

def load_excel_with_mapping(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath)
    mapped_columns = {}

    for key in PLACEHOLDER_KEYS:
        # Essaye de trouver un nom proche dans les colonnes du fichier Excel
        match = get_close_matches(key, df.columns, n=1, cutoff=0.6)
        if match:
            mapped_columns[match[0]] = key
        else:
            raise ValueError(f"Impossible de mapper la colonne : {key}")

    df = df.rename(columns=mapped_columns)
    df = df[PLACEHOLDER_KEYS]  # Réorganise les colonnes
    return df
