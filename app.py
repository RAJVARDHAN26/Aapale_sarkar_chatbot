import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from langdetect import detect
from intent_matcher import IntentClassifier

# Flask setup
app = Flask(__name__)
matcher = IntentClassifier("chatbot_dataset/converted_dataset2.json")

# Configure Gemini
genai.configure(api_key="AIzaSyBw0I-fL2HdCDObR8ntZ4XSmv65I8ImAnM")
gemini_model = genai.GenerativeModel("models/gemini-2.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query", "")
    
    # Detect the intent of the user query
    response, lang, confidence = matcher.predict_intent(query)
    
    # If intent confidence is low, fallback to Gemini with a shorter, more direct prompt
    if response is None or confidence < 0.7:
        try:
            detected_lang = detect(query)
        except:
            detected_lang = "en"

        # Shorter and more precise response request
        if 'scholarships' in query.lower():  # Check if query contains 'scholarships'
            if detected_lang == "mr":
                gemini_prompt = f"स्नातक विद्यार्थ्यांसाठी शिष्यवृत्त्यांची माहिती थोडक्यात द्या."
            else:
                gemini_prompt = f"Give a brief answer about scholarships for undergraduate students."

            gemini_response = gemini_model.generate_content(gemini_prompt)
            response = gemini_response.text.strip()
            lang = detected_lang
        else:
            # Handle general fallback with shorter prompt
            if detected_lang == "mr":
                gemini_prompt = f"हा प्रश्न थोडक्यात उत्तर द्या: {query}"
            else:
                gemini_prompt = f"Give a short and precise answer: {query}"

            gemini_response = gemini_model.generate_content(gemini_prompt)
            response = gemini_response.text.strip()
            lang = detected_lang

    return jsonify({"response": response, "lang": lang})

if __name__ == "__main__":
    app.run(debug=True)
