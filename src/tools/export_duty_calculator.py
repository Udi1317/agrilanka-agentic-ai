"""
Export Duty & Cess Tax Calculator Tool for Sri Lankan Spices & Agricultural Products
"""
from typing import Dict, Any

def calculate_export_duty(crop: str, quantity_kg: float, package_type: str = "bulk") -> Dict[str, Any]:
    """
    Calculates export Cess tax, estimated Freight FOB value, and EDB rebate eligibility.
    """
    crop_clean = crop.lower()
    base_fob_price = {
        "cinnamon": 18.50, # USD / kg
        "pepper": 7.20,
        "cardamom": 32.00,
        "clove": 9.50,
        "tea": 5.80,
        "coconut": 2.10
    }.get(crop_clean, 8.00)

    fob_val_usd = base_fob_price * quantity_kg

    # Retail packaging incentive (< 1kg per pack)
    if package_type.lower() == "retail":
        cess_rate = 0.0
        edb_rebate_rate = 0.05 # 5% EDB grant
        incentive_note = "Eligible for 0% Export Cess Levy and 5% EDB Value-Addition Grant."
    else:
        cess_rate = 0.035 # 3.5% raw bulk export levy
        edb_rebate_rate = 0.0
        incentive_note = "Subject to 3.5% Export Cess Levy to encourage local processing."

    cess_usd = fob_val_usd * cess_rate
    rebate_usd = fob_val_usd * edb_rebate_rate
    net_export_value = fob_val_usd - cess_usd + rebate_usd

    return {
        "crop": crop.capitalize(),
        "quantity_kg": quantity_kg,
        "package_type": package_type.capitalize(),
        "estimated_fob_price_per_kg_usd": base_fob_price,
        "total_fob_value_usd": round(fob_val_usd, 2),
        "cess_levy_usd": round(cess_usd, 2),
        "edb_grant_usd": round(rebate_usd, 2),
        "net_realizable_value_usd": round(net_export_value, 2),
        "incentive_note": incentive_note
    }
