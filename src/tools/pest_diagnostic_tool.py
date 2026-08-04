"""
AgriLanka Pest & Crop Disease Diagnostic Tool
"""
from typing import Dict, Any

PEST_DATABASE = {
    "mite": {
        "crop": "Coconut",
        "pest_name": "Coconut Aceria Mite (Aceria guerreronis)",
        "treatment": "2% Neem oil + garlic emulsion; release predatory mites (Neoseiulus baraki)",
        "phi_days": 0
    },
    "blast": {
        "crop": "Paddy Rice",
        "pest_name": "Rice Blast Fungus (Magnaporthe oryzae)",
        "treatment": "Apply Tebuconazole 250 EC (1 ml/L); reduce excess nitrogen fertilizer",
        "phi_days": 14
    },
    "fruit fly": {
        "crop": "Mango / Papaya",
        "pest_name": "Oriental Fruit Fly (Bactrocera dorsalis)",
        "treatment": "Methyl eugenol MAT traps (10 traps/ha) & Protein bait spray",
        "phi_days": 7
    }
}

def diagnose_pest(symptom_keywords: str) -> Dict[str, Any]:
    symptom_clean = symptom_keywords.lower()
    for key, data in PEST_DATABASE.items():
        if key in symptom_clean or any(word in symptom_clean for word in key.split()):
            return {
                "matched": True,
                "diagnostic": data,
                "confidence": 0.94
            }
    
    return {
        "matched": False,
        "diagnostic": {
            "crop": "General Crop",
            "pest_name": "Unspecified Fungal / Insect Infestation",
            "treatment": "Consult RAG knowledge base or local Agriculture Department extension officer.",
            "phi_days": 14
        },
        "confidence": 0.60
    }
