## **📌 MediAI - AI-Powered Intelligent Healthcare Assistant**  
MediAI is an AI-powered healthcare assistant that predicts potential diseases based on user-reported symptoms. It provides reasoning for predictions and suggests possible medicines for symptom relief.  

### **🚀 Features**  
✅ Symptom-Based Disease Prediction 🏥  
✅ AI-Driven Medical Explanations 📊  
✅ Suggested Medicines for Symptom Relief 💊  
✅ User-Friendly Interface 💬  
✅ Scalable for ML Integration & Real-Time Pharmacy APIs  

---

## **📁 Project Structure**  

📂 **Frontend** → `healthcare-assistant` (React.js)  
📂 **Backend** → Flask API for symptom analysis and disease prediction  

---

## **💻 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Sandeepmopidevi/MediAI-AI-Powered-Intelligent-Healthcare-Assistant.git
cd MediAI-AI-Powered-Intelligent-Healthcare-Assistant
```

### **2️⃣ Backend Setup (Flask API)**  
```bash
cd backend
pip install -r requirements.txt
python app.py
```
- The Flask server will start at `http://127.0.0.1:5000/`

### **3️⃣ Frontend Setup (React.js)**  
```bash
cd healthcare-assistant
npm install
npm start
```
- The React app will start at `http://localhost:3000/`

---

## **🛠 API Endpoints**  

📌 **POST `/chat`** (Predict Disease & Suggest Medicines)  
- **Request Body:**  
  ```json
  {
    "symptoms": ["fever", "cough"]
  }
  ```
- **Response:**  
  ```json
  {
    "response": "Flu: Fever and body aches are common flu symptoms caused by a viral infection. Suggested Medicines: Paracetamol, Ibuprofen"
  }
  ```

---

## **📌 Future Enhancements**  
🔹 **Machine Learning-Based Symptom Checker** 🤖  
🔹 **Real-Time Pharmacy API Integration** 💊  
🔹 **Voice Input for Hands-Free Use** 🎙  

---

## **📝 License**  
This project is licensed under the **MIT License**.
