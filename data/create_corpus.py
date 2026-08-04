import os

corpus_dir = r"C:\Users\Lenovo\.gemini\antigravity\scratch\agrilanka-agentic-ai\data\corpus"
os.makedirs(corpus_dir, exist_ok=True)

docs = {
    "doc_02_tea_export_eu_mrl_compliance.md": """# EU Maximum Residue Limits (MRL) for Ceylon Tea Exports

## 1. Regulatory Context
The European Union (EU) enforces strict Maximum Residue Limits (MRLs) under Regulation (EC) No 396/2005 for pesticide residues in black and green tea (*Camellia sinensis*). Sri Lankan tea exporters must ensure strict adherence to prevent shipment rejections at EU ports of entry (e.g., Rotterdam, Hamburg).

## 2. Key Agrochemical MRL Thresholds
- **Glyphosate**: 2.0 mg/kg (strict limit enforced since 2021).
- **Thiamethoxam**: 0.01 mg/kg (default limit of analytical determination).
- **Imidacloprid**: 0.05 mg/kg.
- **Tebuconazole**: 0.05 mg/kg.
- **Hexaconazole**: 0.02 mg/kg.

## 3. Pre-Harvest Interval (PHI) Guidelines
- Tea estates must observe a minimum Pre-Harvest Interval (PHI) of 14 to 21 days after spraying synthetic agrochemicals before harvesting tea leaves.
- Organic tea estates must use only Sri Lanka Tea Board approved bio-pesticides (e.g., Neem seed kernel extract).

## 4. Analytical Testing Protocol
- Every export batch exceeding 5 metric tons to the EU requires a Certificate of Analysis (CoA) issued by an ISO/IEC 17025 accredited laboratory in Sri Lanka (e.g., ITI, SGS Lanka).
""",
    "doc_03_pepper_harvest_postharvest_quality.md": """# Black and White Pepper Post-Harvest Standards (SLS 105)

## 1. Grade Specifications
Sri Lankan pepper (*Piper nigrum*) is renowned for its high piperine content (up to 7-15%).
- **Grade 1 (Special)**: Bulk density minimum 550 g/l, moisture max 12%, light berries max 2%.
- **Grade 2**: Bulk density minimum 500 g/l, moisture max 12.5%, light berries max 5%.
- **FAQ (Fair Average Quality)**: Bulk density minimum 450 g/l, moisture max 13%.

## 2. Processing Protocols
- **Black Pepper**: Mature green pepper spikes are threshed, blanched in hot water (80°C for 1 minute) to activate polyphenol oxidase enzyme, and sun-dried on clean solar drying racks for 3-4 days until moisture drops below 12%.
- **White Pepper**: Fully ripe red berries are soaked in running clean water for 7-10 days in retting tanks, pericarp removed, washed, and dried to a creamy white color.

## 3. Microbiological and Heavy Metal Limits
- **Salmonella**: Absent in 25g.
- **Aflatoxin B1**: Max 5 ppb; Total Aflatoxins (B1+B2+G1+G2) max 10 ppb.
- **Lead (Pb)**: Max 2.0 mg/kg.
""",
    "doc_04_coconut_mite_control_fertilizer.md": """# Coconut Cultivation: Aceria Mite Control & Fertilizer Protocol

## 1. Pest Management - Coconut Mite (*Aceria guerreronis*)
- **Symptoms**: Triangular pale patches near the calyx of young button nuts (3-4 months old), progressing to deep suberized fissures and stunted nut size.
- **Integrated Pest Management (IPM)**:
  - Spraying 2% Neem oil + garlic emulsion (20ml Neem oil + 20g crushed garlic per 1L water with 5g soap powder).
  - Application of predatory mites (*Neoseiulus baraki*) released at 5,000 mites per hectare.
  - Crown cleaning twice a year before monsoon season.

## 2. Recommended Fertilizer Mixture (Cri Mixture)
- **Adult Palms (> 6 years)**: Apply 3.0 kg of Coconut Research Institute (CRI) Adult Palm Mixture per palm per year.
  - Urea: 1.0 kg
  - Eppawala Rock Phosphate (ERP): 0.8 kg
  - Muriate of Potash (MOP): 1.2 kg
  - Dolomite: 1.0 kg per palm per year applied separately to correct soil acidity (pH 5.5 - 6.5).
""",
    "doc_05_paddy_disease_management_yala_maha.md": """# Rice Paddy Cultivation: Yala and Maha Season Disease Advisory

## 1. Rice Blast (*Magnaporthe oryzae*)
- **Symptoms**: Diamond-shaped lesions with gray/white centers on leaf blades; neck rot resulting in empty panicles ("chaffy grains").
- **Control**: Avoid excessive nitrogen fertilizer (> 100 kg N/ha). Apply Tebuconazole 250 EC (1 ml/L) or Kasugamycin at first onset of leaf blast.

## 2. Bacterial Leaf Blight (*Xanthomonas oryzae*)
- **Symptoms**: Water-soaked streaks starting from leaf margins turning yellow and drying up ("kresek" phase in seedlings).
- **Control**: Use resistant varieties (Bg 300, Bg 352, At 362). Drain field temporarily; refrain from spraying nitrogen during active outbreak.

## 3. Crop Calendar
- **Maha Season**: Planting September/October (Northeast Monsoon), harvesting February/March.
- **Yala Season**: Planting April/May (Southwest Monsoon), harvesting August/September.
""",
    "doc_06_agro_ecological_zones_sri_lanka.md": """# Agro-Ecological Zones (AEZ) of Sri Lanka

## 1. Zonal Classification
Sri Lanka is divided into 3 main climatic zones based on annual rainfall:
- **Wet Zone**: Annual rainfall > 2,500 mm. Divided into Low Country (WL1-WL4), Mid Country (WM1-WM3), and Up Country (WU1-WU3). Suitable for Tea, Rubber, Cinnamon, Vegetables.
- **Intermediate Zone**: Annual rainfall 1,750 - 2,500 mm. Divided into Low Country (IL1-IL3), Mid Country (IM1-IM3), and Up Country (IU1-IU3). Suitable for Coconut, Pepper, Coffee, Cocoa, Maize.
- **Dry Zone**: Annual rainfall < 1,750 mm (mainly from NE monsoon). Low Country (DL1-DL5). Suitable for Paddy, Grain Legumes, Sesame, Chilli, Onion, Mango.

## 2. Soil Types by Region
- Red Yellow Podzolic soils: Wet zone (acidic, pH 4.5 - 5.5).
- Reddish Brown Latosolic soils: Intermediate zone.
- Reddish Brown Earths (RBE) & Low Humic Gley (LHG) soils: Dry zone.
""",
    "doc_07_cardamom_processing_export_standards.md": """# Ceylon Cardamom Processing & SLS Quality Requirements

## 1. Overview
Ceylon Cardamom (*Elettaria cardamomum*) is grown primarily in the central hills (altitude 800 - 1500m MSL). Known as "Green Gold of Sri Lanka".

## 2. Grades
- **Lankika Green (LG)**: Whole green pods, diameter > 7 mm, no split pods, moisture < 10%.
- **Green Split (GS)**: Mature green pods split naturally.
- **Bleached White**: Pods treated with sulfur dioxide fumes to achieve uniform off-white color.

## 3. Curing Process
- Freshly harvested green capsules are cured within 24 hours in fuel-wood or electric flue-curing kilns at 45°C - 50°C for 30 hours to retain vibrant green color.
""",
    "doc_08_edb_export_procedures_tariffs.md": """# Sri Lanka Export Development Board (EDB) Tariff & Incentive Guide

## 1. Export Customs Formalities
- Exporters must register with Sri Lanka Customs (ASYCUDA system) and EDB.
- Documents required: Commercial Invoice, Packing List, Certificate of Origin (Form A / GSP or APTA), Phytosanitary Certificate (Plant Quarantine Department), Quality Certificate (SLSI).

## 2. Export Cess and Taxes on Spices
- Raw un-processed spices carry an export Cess levy to encourage local value addition (e.g., essential oils, oleoresins, ground retail packs).
- Value-added retail spice packs (< 1kg) enjoy 0% export Cess and qualify for EDB Export Development Grants.
""",
    "doc_09_organic_certification_eu_usda.md": """# Organic Agricultural Certification (EU & USDA-NOP)

## 1. Conversion Period
- Annual crops: 2-year conversion period before harvest can be sold as certified organic.
- Perennial crops (Tea, Cinnamon, Coconut): 3-year conversion period.

## 2. Prohibited Inputs
- Synthetic chemical fertilizers (Urea, MOP, TSP).
- Synthetic insecticides, herbicides (Glyphosate, Paraquat), and fungicides.
- Genetically Modified Organisms (GMOs).

## 3. Permitted Soil Amendments
- Compost certified under SLS 1624.
- Biochar, Rock Phosphate (ERP), Fish emulsion, Neem cake.
""",
    "doc_10_nutmeg_mace_quality_control.md": """# Nutmeg and Mace Export Quality Specifications

## 1. Definitions
- **Nutmeg**: Dried seed kernel of *Myristica fragrans*.
- **Mace**: Dried aril surrounding the nutmeg shell.

## 2. Quality Requirements
- **Nutmeg (Sifted Whole)**: Heavy, sound kernels, moisture max 10%, volatile oil min 6.0% v/w.
- **Mace (Handpicked Premium)**: Whole red/yellow arils, moisture max 10%, volatile oil min 15.0% v/w.
- **Aflatoxin Risk**: High risk of Aspergillus flavus infestation during drying. Solar dryers with temperature control (40°C) mandatory.
""",
    "doc_11_soil_ph_nutrient_management.md": """# Soil pH Correction and Micronutrient Management in Sri Lanka

## 1. Soil Acidity Management
- Acidic soils (pH < 5.0) are prevalent in Sri Lanka's Wet Zone (Tea & Rubber estates).
- **Dolomite Application**: Apply 1.0 to 1.5 metric tons/ha of ground agricultural dolomite (CaMg(CO3)2) every 2-3 years to raise soil pH to optimal 5.5 - 6.0 and supply Magnesium (Mg).

## 2. Soil Salinity in Dry Zone
- Coastal Dry Zone soils (DL1) prone to electrical conductivity (EC) > 4 dS/m.
- Remediation: Gypsum application (2-3 tons/ha) combined with deep leaching irrigation.
""",
    "doc_12_clove_stem_oil_extraction.md": """# Ceylon Clove and Clove Bud Oil Quality Guidelines

## 1. Product Varieties
- **Clove Buds (Handpicked Fine)**: Moisture max 12%, volatile oil min 17.0% v/w (eugenol content > 85%).
- **Clove Stem**: Stalks connecting buds, volatile oil 5-7%.
- **Clove Bud Essential Oil**: Distilled via steam distillation, eugenol content 85-95%.
""",
    "doc_13_drip_irrigation_chilli_onion.md": """# Smart Drip Irrigation and Fertigation for Dry Zone Chilli & Onion

## 1. Water Requirements
- Chilli (*Capsicum annuum*): Requires 500-600 mm water per crop cycle. Drip emitter rate: 2.0 L/hr.
- Big Onion: Requires 400-450 mm water. Fertigation using soluble NPK (19:19:19) at weekly intervals.

## 2. Yield Optimization
- Yield increase of 35-50% compared to furrow flood irrigation; water saving up to 45%.
""",
    "doc_14_slsi_gmp_haccp_certification.md": """# Good Manufacturing Practices (GMP) & HACCP for Spice Processing

## 1. Facilities Standards (SLS 1493)
- Spice processing plants must have washable epoxy flooring, stainless steel (SS 304/316) grinding/packing equipment, and positive pressure HEPA air filtration in packing rooms.
- Staff hygiene: Stainless steel foot baths, hairnets, beard covers, and no jewelry policy.

## 2. Hazard Analysis Critical Control Point (HACCP)
- CCP 1: Metal detection (magnetic separator + 1.5mm ferrous / 2.0mm non-ferrous detector).
- CCP 2: Steam sterilization / ethylene oxide pasteurization to eliminate Salmonella & E. coli.
""",
    "doc_15_essential_oil_distillation_standards.md": """# Essential Oil Extraction: Cinnamon Leaf and Bark Oil

## 1. Cinnamon Leaf Oil
- Steam distilled from dried leaves. Yield 0.7 - 1.2%.
- Primary constituent: **Eugenol** (75 - 85%). Cinnamaldehyde < 5%.
- Specific gravity at 20°C: 1.035 - 1.055.

## 2. Cinnamon Bark Oil
- Hydro-distilled from scrapings and quillings. Yield 0.5 - 1.0%.
- Primary constituent: **Cinnamaldehyde** (65 - 75%). Eugenol 4 - 10%.
- Premium pricing ($250 - $400/kg in export markets).
""",
    "doc_16_vanilla_curing_and_export.md": """# Bourbon Vanilla Curing Protocol in Central Sri Lanka

## 1. Harvesting Criteria
- Vanilla beans (*Vanilla planifolia*) harvested at 8-9 months when tip turns yellow-green.

## 2. Four-Step Curing Process
1. **Killing**: Scalding beans in 63°C-65°C water for 2-3 minutes.
2. **Sweating**: Wrapping beans in wool blankets in wooden boxes at 45°C for 24-48 hours.
3. **Sun Drying**: Drying on wooden trays 3-4 hours daily for 12-15 days.
4. **Conditioning**: Aging in parchment-lined wax boxes for 3 months to develop vanillin aroma (min 1.8-2.2% vanillin).
""",
    "doc_17_rubber_processing_rss_latex.md": """# Ribbed Smoked Sheet (RSS) Rubber Processing Guidelines

## 1. Grading (RSS 1 to RSS 5)
- **RSS 1**: Premium grade, free from mold, rust, pinholes, sand, or resinous specs.
- Latex coagulated using 1% Formic Acid (30ml per 10kg dry rubber content).
- Smoked in smokehouses at 40°C - 60°C for 4-5 days using Rubberwood fuel.
""",
    "doc_18_phytosanitary_certificate_quarantine.md": """# National Plant Quarantine Service (NPQS) Export Compliance

## 1. Purpose
NPQS issues Phytosanitary Certificates verifying export consignments are free from regulated quarantine pests (e.g., Trogoderma granarium, Bactrocera dorsalis).

## 2. Inspection Workflow
- Exporter submits application 48 hours prior to shipment.
- NPQS inspector draws random samples (sqrt(N)+1 containers).
- Laboratory analysis for nematodes, fungi, insects, weed seeds.
- Issue Phytosanitary Certificate within 24 hours of passing inspection.
""",
    "doc_19_tea_smallholder_factory_advisory.md": """# Tea Smallholder Green Leaf Quality Index (GLQI)

## 1. Plucking Standard
- Optimal plucking: "Two leaves and a bud" (minimum 65% fine leaf count).
- Coarse leaf (> 35%) leads to high fiber, low liquidity, and reduced auction prices at Colombo Tea Auction.

## 2. Transport & Leaf Handling
- Leaves transported in aerated plastic crates (max 15kg per crate).
- Sack compaction causes leaf fermentation and bruising ("red leaf" defect).
""",
    "doc_20_fruit_fly_management_mango_papaya.md": """# Oriental Fruit Fly (*Bactrocera dorsalis*) IPM Guide

## 1. Crop Vulnerability
- Mango (Karutha Colomban, Willard), Papaya, Guava.

## 2. Suppression Strategy
- **Male Annihilation Technique (MAT)**: Methyl eugenol trap suspended at 10 traps per hectare.
- **Protein Bait Spray**: Torula yeast / hydrolysed protein sprayed on lower leaf canopy.
- **Bagging**: Wrapping young fruit with double-layered paper bags 30 days post-fruit set.
""",
    "doc_21_sustainable_agriculture_gap_certification.md": """# Sri Lanka Good Agricultural Practices (SL-GAP) Certification

## 1. Core Pillar Requirements
- Traceability: Farm record books detailing date of agrochemical application, batch number, operator name.
- Water Source Testing: E. coli < 100 CFU/100ml for irrigation water.
- Heavy Metal Soil Screening: Cadmium < 1.0 mg/kg, Arsenic < 5.0 mg/kg.
""",
    "doc_22_cocoa_fermentation_drying.md": """# Ceylon Fine Flavor Cocoa Fermentation Standards

## 1. Fermentation
- Trinitario & Forastero beans fermented in sweat boxes made of Jackwood (*Artocarpus heterophyllus*) for 5-6 days.
- Temperature reaches 48°C - 50°C by Day 3. Turns beans chocolate brown.

## 2. Drying
- Sun-dried on elevated bamboo mats to < 7.5% moisture.
""",
    "doc_23_climate_resilience_agroforestry.md": """# Agroforestry & Intercropping Systems in Spice Gardens (Kandyan Forest Gardens)

## 1. Spatial Structure
- Multi-tier canopy system: Coconut/Arecanut (upper), Pepper on Support Trees/Cinnamon (mid-tier), Ginger/Turmeric/Cardamom (lower).

## 2. Microclimate Benefits
- Maintains soil moisture during dry spells; reduces ambient temp by 2-3°C; prevents soil erosion on hilly terrain (> 20% slope).
""",
    "doc_24_ginger_turmeric_curcumin_content.md": """# Ginger and Turmeric Cultivation & Curcumin Guidelines

## 1. Turmeric (*Curcuma longa*)
- High-curcumin varieties: Local Lak-Parakum yields 5.0 - 5.8% curcumin content (exceeds global benchmark of 3.5%).
- Harvested at 9-10 months when foliage turns yellow and dries.

## 2. Processing
- Rhizomes boiled in water for 45 minutes, sun-dried, and polished in drum polishers.
""",
    "doc_25_export_documentation_procedure.md": """# Comprehensive Export Logistics & Document Verification Checklist

## 1. Mandatory Document Suite for Sri Lankan Agri-Exporters
1. **Commercial Invoice & Packing List** (detailing HS Codes, e.g., HS 0906.11 for Ceylon Cinnamon).
2. **Bill of Lading (B/L) / Air Waybill (AWB)**.
3. **Phytosanitary Certificate** (NPQS).
4. **Certificate of Origin** (Department of Commerce / Ceylon Chamber of Commerce).
5. **SLSI Quality Certificate** (for regulated commodities).
6. **Certificate of Analysis (CoA)** for Heavy Metals, Pesticides, and Aflatoxins.
""",
}

for filename, content in docs.items():
    filepath = os.path.join(corpus_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print(f"Successfully generated {len(docs)} corpus documents in {corpus_dir}")
