from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Symptom-Disease-Medicine Mapping
data = {
    "fever": {
        "diseases": ["Flu", "Malaria"],
        "medicines": ["Paracetamol", "Ibuprofen"]
    },
    "cough": {
        "diseases": ["Bronchitis", "Pneumonia"],
        "medicines": ["Dextromethorphan", "Ambroxol"]
    },
    "headache": {
        "diseases": ["Migraine", "High Blood Pressure"],
        "medicines": ["Aspirin", "Sumatriptan"]
    },
    "stomach pain": {
        "diseases": ["Gastric Issues", "Appendicitis"],
        "medicines": ["Omeprazole", "Antacids"]
    },
    "cold": {
        "diseases": ["Common Cold", "Sinus Infection"],
        "medicines": ["Cetirizine", "Phenylephrine"]
    },
    "sore throat": {
        "diseases": ["Tonsillitis", "Strep Throat"],
        "medicines": ["Amoxicillin", "Chlorhexidine Gargle"]
    },
    "chest pain": {
        "diseases": ["Heart Attack", "Acid Reflux"],
        "medicines": ["Aspirin", "Antacids"]
    },
    "shortness of breath": {
        "diseases": ["Asthma", "COPD"],
        "medicines": ["Salbutamol", "Budesonide Inhaler"]
    },
    "fatigue": {
        "diseases": ["Anemia", "Diabetes"],
        "medicines": ["Iron Supplements", "Metformin"]
    },
    "nausea": {
        "diseases": ["Food Poisoning", "Pregnancy"],
        "medicines": ["Domperidone", "Vitamin B6"]
    },
    "diarrhea": {
        "diseases": ["Food Poisoning", "Gastroenteritis"],
        "medicines": ["ORS Solution", "Loperamide"]
    },
    "dizziness": {
        "diseases": ["Low Blood Pressure", "Anemia"],
        "medicines": ["Fludrocortisone", "Iron Supplements"]
    },
    "joint pain": {
        "diseases": ["Arthritis", "Lupus"],
        "medicines": ["Ibuprofen", "Methotrexate"]
    },
    "itching": {
        "diseases": ["Allergy", "Fungal Infection"],
        "medicines": ["Antihistamines", "Clotrimazole Cream"]
    }
}

# Disease Explanations
disease_explanations = {
    "Flu": "Fever and body aches are common flu symptoms caused by a viral infection.",
    "Malaria": "High fever with chills can indicate malaria, often caused by mosquito bites.",
    "Bronchitis": "A persistent cough with mucus suggests bronchitis, an inflammation of the airways.",
    "Pneumonia": "A cough with chest pain and fever could indicate pneumonia, a lung infection.",
    "Migraine": "Headaches with sensitivity to light may indicate migraines caused by nerve changes in the brain.",
    "High Blood Pressure": "Frequent headaches can be a sign of high blood pressure, leading to strain on arteries.",
    "Gastric Issues": "Stomach pain with bloating could mean indigestion or gastritis due to excess acid.",
    "Appendicitis": "Sharp lower stomach pain on the right side may indicate appendicitis, which needs urgent care.",
    "Common Cold": "Runny nose and sneezing are signs of the common cold, caused by viral infections.",
    "Sinus Infection": "Nasal congestion with headache suggests sinus infection due to blocked sinuses.",
    "Heart Attack": "Severe chest pain with shortness of breath may indicate a heart attack due to blocked arteries.",
    "Acid Reflux": "Burning chest pain after meals suggests acid reflux, where stomach acid moves into the throat.",
    "Asthma": "Shortness of breath with wheezing is common in asthma due to airway inflammation.",
    "COPD": "Breathing difficulty with chronic cough may indicate COPD, often linked to smoking.",
    "Anemia": "Fatigue and dizziness are common in anemia due to low red blood cell levels.",
    "Diabetes": "Unexplained fatigue and weight loss could indicate diabetes due to blood sugar issues.",
    "Food Poisoning": "Nausea and vomiting after eating suggest food poisoning caused by bacteria.",
    "Pregnancy": "Nausea (morning sickness) is a common early pregnancy symptom due to hormonal changes.",
    "Gastroenteritis": "Vomiting and diarrhea together may indicate gastroenteritis caused by infections.",
    "Arthritis": "Joint pain with swelling could be arthritis, an inflammatory joint disease.",
    "Lupus": "Joint pain with fatigue may indicate lupus, an autoimmune disease.",
    "Allergy": "Itching and rash may indicate an allergic reaction to food, pollen, or medication.",
    "Fungal Infection": "Persistent skin itching in one area could be a fungal infection like ringworm."
}

@app.route("/chat", methods=["POST"])
def chat():
    symptoms_list = request.json.get("symptoms", [])
    matched_diseases = {}

    for symptom in symptoms_list:
        if symptom in data:
            diseases = data[symptom]["diseases"]
            for disease in diseases:
                if disease in matched_diseases:
                    matched_diseases[disease] += 1
                else:
                    matched_diseases[disease] = 1

    if not matched_diseases:
        return jsonify({"response": "No relevant data found. Please consult a doctor."})

    # Sort diseases by how many symptoms match
    sorted_diseases = sorted(matched_diseases, key=matched_diseases.get, reverse=True)

    # Pick top 1 or 2 diseases
    top_diseases = sorted_diseases[:2]

    # Formulate response
    response = []
    for disease in top_diseases:
        explanation = disease_explanations.get(disease, "Possible match based on symptoms.")
        medicines = []
        for symptom in symptoms_list:
            if symptom in data and disease in data[symptom]["diseases"]:
                medicines.extend(data[symptom]["medicines"])
        
        medicine_list = list(set(medicines))  # Remove duplicates
        response.append(f"{disease}: {explanation} Suggested Medicines: {', '.join(medicine_list)}")

    return jsonify({"response": " | ".join(response)})

if __name__ == "__main__":
    app.run(debug=True)
