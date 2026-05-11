import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from langdetect import detect
from nltk.tokenize import RegexpTokenizer  # ✅ using RegexpTokenizer (no punkt needed)

class IntentClassifier:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        self.intents = {}
        self.X = []
        self.y = []
        self.lang_map = {}  # maps each query to its language
        self.tokenizer = RegexpTokenizer(r'\w+')  # ✅ initialize tokenizer
        self._load_dataset()
        self._train()

    def _load_dataset(self):
        with open(self.dataset_path, "r", encoding="utf-8") as f:
            self.intents = json.load(f)

        for intent, content in self.intents.items():
            for q in content["queries"]:
                self.X.append(q["text"])
                self.y.append(intent)
                self.lang_map[q["text"]] = q["lang"]

    def _train(self):
        X_vectors = self.vectorizer.fit_transform(self.X)
        self.model.fit(X_vectors, self.y)

    def predict_intent(self, query):
        lang = detect(query)
        tokens = self.tokenizer.tokenize(query.lower())
        best_intent = None
        best_score = -1
    
        for intent, content in self.intents.items():
            for sample in content["queries"]:
                sample_text = sample["text"]
                sample_tokens = self.tokenizer.tokenize(sample_text.lower())
                common = set(tokens) & set(sample_tokens)
                score = len(common)
    
                if score > best_score:
                    best_score = score
                    best_intent = intent
    
        confidence = best_score / max(len(tokens), 1)  # Normalize score (0 to 1)
    
        if best_intent and confidence >= 0.1:  # Adjust threshold as needed
            for sample_query, response in zip(self.intents[best_intent]["queries"], self.intents[best_intent]["responses"]):
                if detect(sample_query["text"]) == lang:
                    return response["text"], lang, confidence
            return self.intents[best_intent]["responses"][0]["text"], lang, confidence
        else:
            return None, lang, 0.0


    def _detect_language_from_training(self, user_input):
        """Try to match exact input first; fallback to langdetect (optional)"""
        for q in self.lang_map:
            if user_input.strip().lower() == q.strip().lower():
                return self.lang_map[q]
        return 'en'
