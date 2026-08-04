"""
Sri Lanka Agro-Ecological Zone & Climate Suitability Tool
"""
from typing import Dict, Any

AGRO_ZONES = {
    "wet_zone": {
        "suitable_crops": ["Ceylon Cinnamon", "Tea", "Rubber", "Vanilla", "Cardamom"],
        "annual_rainfall_mm": "> 2500 mm",
        "soil_type": "Red Yellow Podzolic (pH 4.5 - 5.5)"
    },
    "intermediate_zone": {
        "suitable_crops": ["Coconut", "Pepper", "Coffee", "Cocoa", "Ginger", "Turmeric"],
        "annual_rainfall_mm": "1750 - 2500 mm",
        "soil_type": "Reddish Brown Latosolic"
    },
    "dry_zone": {
        "suitable_crops": ["Rice Paddy", "Chilli", "Big Onion", "Sesame", "Maize", "Mango"],
        "annual_rainfall_mm": "< 1750 mm",
        "soil_type": "Reddish Brown Earths (RBE) & Low Humic Gley (LHG)"
    }
}

def evaluate_climate_suitability(zone: str, crop: str) -> Dict[str, Any]:
    zone_key = zone.lower().replace(" ", "_")
    zone_info = AGRO_ZONES.get(zone_key, AGRO_ZONES["wet_zone"])
    
    is_suitable = any(crop.lower() in c.lower() for c in zone_info["suitable_crops"])
    score = 92 if is_suitable else 55

    return {
        "evaluated_zone": zone.title(),
        "crop": crop.title(),
        "is_suitable": is_suitable,
        "suitability_score": score,
        "rainfall_range": zone_info["annual_rainfall_mm"],
        "dominant_soil": zone_info["soil_type"],
        "recommendation": f"Optimal fit for {zone.title()}" if is_suitable else f"Sub-optimal fit. Requires micro-irrigation and soil pH correction."
    }
