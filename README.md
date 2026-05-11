🤖 Aaple Sarkar Multilingual AI Chatbot
📌 Project Overview

The Aaple Sarkar Multilingual AI Chatbot is an AI-powered web-based chatbot system developed using Python, Flask, Machine Learning, and Google Gemini API. The chatbot is designed to provide quick and intelligent responses related to government services, scholarships, and public information in multiple languages.

The system combines:

Intent-based Machine Learning
Natural Language Processing (NLP)
Language Detection
Generative AI (Gemini API)
Multilingual Query Handling

The chatbot first tries to identify the user’s intent using a trained ML intent classifier. If the confidence score is low, the system automatically switches to Google Gemini AI for generating intelligent fallback responses.

This project aims to provide a smart, scalable, and user-friendly virtual assistant for citizens.

🚀 Features

✅ Multilingual Chat Support
✅ AI-Based Intent Detection
✅ Gemini AI Integration
✅ Scholarship Query Handling
✅ Automatic Language Detection
✅ Machine Learning-Based Response Prediction
✅ Flask Web Application
✅ Fast and Lightweight System
✅ JSON Dataset-Based Training
✅ Real-Time User Interaction

🧠 Technologies Used
Technology	Purpose
Python	Core Backend Programming
Flask	Web Framework
Scikit-Learn	Machine Learning Model
NLP	Text Processing
CountVectorizer	Feature Extraction
Multinomial Naive Bayes	Intent Classification
Google Gemini API	AI Response Generation
HTML/CSS/JavaScript	Frontend Development
LangDetect	Language Detection
JSON Dataset	Training Data

📂 Project Structure
chatbot_project/
│
├── app.py
├── intent_matcher.py
├── convert_dataset.py
├── test.py
├── voice_utils.py
├── chatbot.db
├── requirements.txt
│
├── chatbot_dataset/
│   ├── aaple_sarkar_chatbot_dataset_final.json
│   ├── converted_dataset.json
│   └── converted_dataset2.json
│
├── static/
│   ├── script.js
│   ├── styles.css
│   └── images/
│       └── logo.png
│
├── templates/
│   └── index.html
│
└── __pycache__/
