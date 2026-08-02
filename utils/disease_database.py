import json
import os

# 100% Comprehensive & Dynamic Agronomic Knowledge Base for PlantVillage Classes
DISEASE_KNOWLEDGE_BASE = {
    "Pepper__bell___Bacterial_spot": {
        "name": "Pepper Bell - Bacterial Spot (Xanthomonas euvesicatoria)",
        "description": "Bacterial spot affects foliage and fruit of bell pepper plants. Leaves develop dark, water-soaked lesions that turn necrotic, leading to severe leaf drop.",
        "causes": "Bacterium Xanthomonas euvesicatoria favored by high temperatures (>25°C), high humidity, and splashing rain.",
        "symptoms": "Small, water-soaked dark brown leaf spots, yellow halos surrounding spots, premature defoliation, rough raised spots on fruits.",
        "prevention": "Use certified disease-free seeds, practice crop rotation (avoid solanaceous crops for 3 years), use drip irrigation instead of overhead spray.",
        "treatment": "Apply copper-based bactericides combined with Mancozeb at early disease onset to manage bacterial spread.",
        "pesticide": "Copper Hydroxide + Mancozeb spray, or Streptomycin sulfate.",
        "organic_treatment": "Copper octanoate liquid soap or Bacillus subtilis bio-bactericide spray every 7-10 days.",
        "fertilizer": "Maintain balanced N-P-K (10-10-10) with adequate calcium; avoid excessive quick-release nitrogen."
    },
    "Pepper__bell___healthy": {
        "name": "Pepper Bell - Healthy Plant",
        "description": "The pepper leaf displays uniform chlorophyll distribution, intact leaf tissue, and zero signs of bacterial or fungal infection.",
        "causes": "Optimal soil nutrients, balanced watering, and effective integrated pest management.",
        "symptoms": "Vibrant dark green leaf, clean vein structure, smooth margins, strong petiole attachment.",
        "prevention": "Maintain routine soil testing, proper plant spacing, drip irrigation, and clean field hygiene.",
        "treatment": "No disease treatment required.",
        "pesticide": "None needed.",
        "organic_treatment": "Preventative cold-pressed neem oil spray for general pest management.",
        "fertilizer": "Standard balanced fertilizer schedule suitable for flowering and fruit-setting stages."
    },
    "Potato___Early_blight": {
        "name": "Potato - Early Blight (Alternaria solani)",
        "description": "Fungal disease causing dark brown spots with characteristic concentric rings ('targetboard' pattern) on older potato leaves.",
        "causes": "Fungus Alternaria solani thriving in alternating warm dry and humid weather conditions.",
        "symptoms": "Concentric ring spots on lower mature leaves, yellowing surrounding spots, leaf drop, reduced tuber yield.",
        "prevention": "Practice 3-year crop rotation, plant resistant cultivars, maintain vigorous plant growth, eliminate plant debris.",
        "treatment": "Apply protective fungicides at first sign of lower leaf lesions; maintain regular application until harvest.",
        "pesticide": "Chlorothalonil, Mancozeb, or Azoxystrobin fungicide.",
        "organic_treatment": "Bacillus amyloliquefaciens or bio-copper fungicides.",
        "fertilizer": "Maintain high nitrogen and phosphorus fertility; stressed plants are significantly more susceptible."
    },
    "Potato___Late_blight": {
        "name": "Potato - Late Blight (Phytophthora infestans)",
        "description": "A highly destructive water-mold disease that rapidly rots potato foliage, stems, and tubers under cool, wet conditions.",
        "causes": "Oomycete Phytophthora infestans spread by airborne sporangia in high humidity (>90%) and mild temps (15-22°C).",
        "symptoms": "Large water-soaked dark green/brown lesions, white cottony mold growth on underside of leaves, rapid canopy collapse.",
        "prevention": "Destroy volunteer potatoes, plant certified seed tubers, eliminate cull piles, use drip irrigation.",
        "treatment": "Immediate application of systemic fungicides upon regional disease detection.",
        "pesticide": "Mafenoxam / Metalaxyl-M, Cymoxanil, or Fluazinam.",
        "organic_treatment": "Fixed copper hydroxide or copper oxychloride sprayed preventatively before rain events.",
        "fertilizer": "Avoid excess nitrogen; boost plant cell wall strength with soluble silicon and potassium."
    },
    "Potato___healthy": {
        "name": "Potato - Healthy Plant",
        "description": "Potato leaf specimen shows healthy green foliage, sturdy stem attachment, and zero signs of fungal or bacterial blight.",
        "causes": "Proper seed selection, adequate soil moisture, and balanced fertility.",
        "symptoms": "Deep green leaf color, crisp texture, intact margins, clean leaf underside.",
        "prevention": "Continue preventative crop care, balanced irrigation, and routine scouting.",
        "treatment": "No corrective treatment needed.",
        "pesticide": "None needed.",
        "organic_treatment": "Preventative neem oil or compost tea foliar spray.",
        "fertilizer": "Balanced potato fertilizer (10-20-20 NPK) rich in potassium for tuber development."
    },
    "Tomato_Bacterial_spot": {
        "name": "Tomato - Bacterial Spot (Xanthomonas perforans)",
        "description": "Bacterial infection causing small water-soaked spots on leaves and stems, leading to severe defoliation and scabbed fruit.",
        "causes": "Bacterium Xanthomonas species transmitted via infected seeds, splashing rain, and contaminated equipment.",
        "symptoms": "Dark brown/black spots with yellow halos, leaf drop, raised rough black scabs on green tomatoes.",
        "prevention": "Plant certified disease-free seeds/transplants, sanitize stakes and tools, avoid overhead irrigation.",
        "treatment": "Spray preventative copper bactericides combined with Mancozeb.",
        "pesticide": "Copper Hydroxide + Mancozeb tank mix.",
        "organic_treatment": "Copper octanoate combined with Bacillus subtilis or Reynoutria sachalinensis extract.",
        "fertilizer": "Maintain balanced calcium to nitrogen ratio; avoid excessive ammonium nitrate."
    },
    "Tomato_Early_blight": {
        "name": "Tomato - Early Blight (Alternaria linariae)",
        "description": "Common fungal disease causing dark brown spots with yellow halos and concentric target-like rings on tomato leaves.",
        "causes": "Fungus Alternaria linariae overwintering in crop residues and spread by wind and rain splashing.",
        "symptoms": "Targetboard concentric ring spots on mature lower leaves, leaf yellowing, stem cankers, blossom end fruit rot.",
        "prevention": "Stake and prune plants for air circulation, mulch soil base, rotate crops out of Solanaceae family.",
        "treatment": "Apply protective fungicides starting at lower leaf symptom onset.",
        "pesticide": "Chlorothalonil, Difenoconazole, or Mancozeb.",
        "organic_treatment": "Liquid copper fungicide or bio-fungicide containing Trichoderma species.",
        "fertilizer": "Ensure adequate nitrogen and potassium levels to maintain leaf vigor."
    },
    "Tomato_Late_blight": {
        "name": "Tomato - Late Blight (Phytophthora infestans)",
        "description": "Rapidly spreading water-mold disease causing large dark water-soaked leaf spots and greasy brown fruit rot.",
        "causes": "Oomycete Phytophthora infestans favored by cool, foggy, or rainy weather.",
        "symptoms": "Irregular dark water-soaked spots, white fuzzy fungal growth on leaf undersides in morning, firm brown fruit rot.",
        "prevention": "Plant resistant tomato varieties, destroy infected crop residues immediately, avoid foliage wetting.",
        "treatment": "Apply curative systemic fungicides immediately upon detection.",
        "pesticide": "Cymoxanil, Dimethomorph, or Mandipropamid.",
        "organic_treatment": "Copper sulfate / Copper hydroxide preventative sprays.",
        "fertilizer": "Provide adequate potassium and calcium; avoid high nitrogen."
    },
    "Tomato_Leaf_Mold": {
        "name": "Tomato - Leaf Mold (Passalora fulva)",
        "description": "Fungal disease prevalent in high-humidity greenhouses and tunnels, causing pale yellow leaf spots with velvety olive mold underneath.",
        "causes": "Fungus Passalora fulva thriving in relative humidity above 85% and warm temperatures.",
        "symptoms": "Pale green/yellow spots on upper leaf surfaces; velvety olive-brown mold on underside of leaves.",
        "prevention": "Increase greenhouse ventilation, keep relative humidity below 85%, space plants widely.",
        "treatment": "Apply fungicides at the first sign of lower leaf yellowing.",
        "pesticide": "Difenoconazole, Chlorothalonil, or Cyprodinil.",
        "organic_treatment": "Potassium bicarbonate (MilStop) or Bacillus subtilis bio-fungicide.",
        "fertilizer": "Maintain balanced potassium levels; avoid dense foliage caused by excess nitrogen."
    },
    "Tomato_Septoria_leaf_spot": {
        "name": "Tomato - Septoria Leaf Spot (Septoria lycopersici)",
        "description": "Fungal disease causing numerous small, circular spots with dark borders and gray/tan centers containing tiny black specks.",
        "causes": "Fungus Septoria lycopersici spread by splashing water, insects, and garden equipment in warm wet weather.",
        "symptoms": "Abundant small round spots with gray centers on lower leaves, dark borders, black pycnidia specks in center, defoliation.",
        "prevention": "Remove lower leaves near soil, mulch heavily under plants, practice 3-year crop rotation.",
        "treatment": "Fungicide sprays applied at 7-14 day intervals upon symptom appearance.",
        "pesticide": "Chlorothalonil, Mancozeb, or Azoxystrobin.",
        "organic_treatment": "Copper soap or sulfur-based organic fungicide.",
        "fertilizer": "Maintain balanced soil organic matter and N-P-K fertility."
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "name": "Tomato - Two-Spotted Spider Mites (Tetranychus urticae)",
        "description": "Microscopic arachnid pests that suck plant sap from leaf undersides, causing yellow stippling and fine webbing.",
        "causes": "Spider mite infestations favored by dry, hot, dusty weather conditions.",
        "symptoms": "Yellowish-white stippling dots on leaves, bronze leaf color, fine silky webbing on undersides, leaf drying.",
        "prevention": "Keep plants well-watered, control dust around garden beds, preserve natural predatory insects.",
        "treatment": "Spray miticides or insecticidal soaps targeting leaf undersides thoroughly.",
        "pesticide": "Abamectin, Bifenazate, or Spiromesifen miticide.",
        "organic_treatment": "Insecticidal soap, cold-pressed Neem oil, or release predatory mites (Phytoseiulus persimilis).",
        "fertilizer": "Avoid over-fertilizing with nitrogen which increases sap sugar and attracts mites."
    },
    "Tomato__Target_Spot": {
        "name": "Tomato - Target Spot (Corynespora cassiicola)",
        "description": "Fungal disease producing brown leaf lesions with light brown centers and yellow halos, resembling target rings.",
        "causes": "Fungus Corynespora cassiicola favored by warm temperatures (20-30°C) and high humidity.",
        "symptoms": "Small pinprick spots expanding into target-like brown spots, defoliation starting from lower canopy.",
        "prevention": "Prune lower leaves, maintain plant spacing, avoid working with wet plants.",
        "treatment": "Fungicide application starting when symptoms first appear.",
        "pesticide": "Azoxystrobin + Difenoconazole, or Chlorothalonil.",
        "organic_treatment": "Copper octanoate or Bacillus subtilis spray.",
        "fertilizer": "Ensure adequate soil potassium and calcium."
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "name": "Tomato - Yellow Leaf Curl Virus (TYLCV)",
        "description": "Devastating viral disease transmitted by silverleaf whiteflies, causing extreme plant stunting and upward leaf curling.",
        "causes": "Begomovirus transmitted exclusively by the whitefly vector Bemisia tabaci.",
        "symptoms": "Severe plant stunting, leaves curling upward with bright yellow margins, flower abortion, poor fruit set.",
        "prevention": "Plant TYLCV-resistant tomato varieties, install 50-mesh insect netting, remove infected plants immediately.",
        "treatment": "No cure for the virus itself; focus entirely on controlling whitefly vector populations.",
        "pesticide": "Imidacloprid, Thiamethoxam, or Spirotetramat for whitefly control.",
        "organic_treatment": "Yellow sticky traps for monitoring, Neem oil, or insecticidal soap sprays.",
        "fertilizer": "Apply foliar micronutrient spray (Zinc, Iron) to help infected plants stay vigorous."
    },
    "Tomato__Tomato_mosaic_virus": {
        "name": "Tomato - Tomato Mosaic Virus (ToMV)",
        "description": "Highly contagious viral disease causing mottling, mosaic yellow-green leaf patterns, and leaf distortion.",
        "causes": "Tobamovirus spread mechanically by touch, hands, tools, clothes, and infected seeds.",
        "symptoms": "Alternating light and dark green mosaic patterns on leaves, fern-like leaf distortion, stunted growth, brown internal fruit necrosis.",
        "prevention": "Plant resistant tomato cultivars, wash hands with milk/soap before handling plants, sanitize all garden tools.",
        "treatment": "No chemical treatment available; remove and destroy infected plants immediately.",
        "pesticide": "None effective against viruses.",
        "organic_treatment": "Spray skim milk solution as preventative barrier; use non-fat dry milk to decontaminate hands/tools.",
        "fertilizer": "Provide balanced nutrition; avoid excess nitrogen."
    },
    "Tomato_healthy": {
        "name": "Tomato - Healthy Plant",
        "description": "The tomato leaf exhibits pristine dark green foliage, uniform leaf veins, sturdy structure, and zero disease symptoms.",
        "causes": "Optimal soil health, proper spacing, drip irrigation, and proactive pest monitoring.",
        "symptoms": "Vibrant uniform green color, crisp compound leaflets, smooth intact edges, healthy petiole.",
        "prevention": "Continue routine watering at soil level, mulch soil base, and maintain crop rotation.",
        "treatment": "No disease treatment required.",
        "pesticide": "None needed.",
        "organic_treatment": "Preventative neem oil or seaweed extract foliar spray.",
        "fertilizer": "Standard tomato fertilization (5-10-10 NPK) rich in phosphorus and potassium."
    }
}

def get_disease_details(disease_key):
    """
    Returns the comprehensive dynamic dictionary for the given PlantVillage disease key.
    """
    if disease_key in DISEASE_KNOWLEDGE_BASE:
        return DISEASE_KNOWLEDGE_BASE[disease_key]
        
    # Clean fallback for any class name
    clean_name = str(disease_key).replace("___", " - ").replace("_", " ")
    return {
        "name": clean_name,
        "description": f"Diagnosis identified visual symptoms matching {clean_name}.",
        "causes": "Pathogen infection (fungal, bacterial, viral) or environmental stress.",
        "symptoms": f"Discoloration, spots, or tissue deformation matching {clean_name}.",
        "prevention": "Practice crop rotation, plant sanitation, proper spacing, and drip irrigation.",
        "treatment": "Apply targeted crop protection products according to local agricultural guidelines.",
        "pesticide": "Registered protective fungicide or insecticide.",
        "organic_treatment": "Apply neem oil spray or organic copper fungicide.",
        "fertilizer": "Balanced N-P-K fertilizer based on soil testing."
    }
