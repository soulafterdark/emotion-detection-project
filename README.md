# Emotion Detection Project (IBM Python & Watson NLP)
This project is a Flask-based Emotion Detection web application created as part of the IBM “Building Generative AI-Powered Applications” course. It analyzes text and returns both the dominant emotion and detailed emotion scores using a local Watson NLP model.

## 🚀 Features
- Detects emotions from any text input
- Returns dominant emotion + full probability distribution
- Flask API endpoint (/emotionDetector)
- Browser-based UI
- Modular Python package (EmotionDetection/)
- Includes unit tests
- Runs 100% locally using Watson NLP runtime

## 📂 Project Structure
emotion-detection-project/
├── EmotionDetection/
│   ├── __init__.py
│   ├── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md

## 🧠 How It Works
1. User enters text
2. Text is classified using Watson NLP's emotion model
3. App returns the dominant emotion and raw probability scores

Example Output:
{
  "anger": 0.02,
  "disgust": 0.01,
  "fear": 0.03,
  "joy": 0.88,
  "sadness": 0.06,
  "dominant_emotion": "joy"
}

## ▶️ Running the App Locally
### 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

### 2. Install dependencies
pip install flask
pip install ibm-watson-machine-learning
pip install pytest

### 3. Run the server
python server.py

Open your browser: http://127.0.0.1:5000

## 🧪 Running Tests
pytest -q

## 🌐 API Endpoint
POST /emotionDetector

Request:
{ "text": "I am feeling fantastic today!" }

Response:
{
  "dominant_emotion": "joy",
  "joy": 0.91,
  "sadness": 0.02,
  "fear": 0.01,
  "anger": 0.01,
  "disgust": 0.01
}

## 🛠️ Technologies Used
- Python
- Flask
- Watson NLP
- HTML & JavaScript
- Unit Testing (pytest)

## 📸 Screenshots (Optional)
Add your IBM peer-review screenshots here.

## 📘 License
Licensed under the MIT License.

## ✨ Future Enhancements
- Add sentiment + emotion combined analysis
- Containerize with Docker
- UI/UX improvements
- Batch text processing
- Add logging & analytics

## 👤 Author
Gabe Chavez  
GitHub: https://github.com/soulafterdark
