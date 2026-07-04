"""Natural Language Processing Engine for Eugene AI"""

import re
from collections import Counter
from config.settings import NLP_SETTINGS


class NLPEngine:
    """Advanced NLP processing system"""

    def __init__(self):
        """Initialize NLP Engine"""
        self.settings = NLP_SETTINGS
        self.vocabulary = set()
        self.word_embeddings = {}
        self.sentiment_scores = {}
        self.context_history = []

    def tokenize(self, text):
        """Tokenize input text"""
        # Convert to lowercase and split
        tokens = re.findall(r'\b\w+\b', text.lower())
        return tokens

    def analyze_sentiment(self, text):
        """Analyze sentiment of text"""
        positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful',
            'fantastic', 'love', 'awesome', 'best', 'happy'
        }
        negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'hate',
            'worst', 'sad', 'angry', 'disappointed', 'wrong'
        }

        tokens = self.tokenize(text)
        pos_count = sum(1 for token in tokens if token in positive_words)
        neg_count = sum(1 for token in tokens if token in negative_words)

        total = pos_count + neg_count
        if total == 0:
            return 0.5  # Neutral

        sentiment = pos_count / total
        return sentiment

    def extract_entities(self, text):
        """Extract named entities from text"""
        # Simple entity extraction based on patterns
        entities = {
            'persons': re.findall(r'\b[A-Z][a-z]+\b', text),
            'numbers': re.findall(r'\b\d+\b', text),
            'emails': re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text),
            'urls': re.findall(r'http[s]?://\S+', text),
        }
        return entities

    def detect_intent(self, text):
        """Detect user intent from text"""
        intents_keywords = {
            'greeting': ['hello', 'hi', 'hey', 'greetings'],
            'question': ['what', 'how', 'why', 'where', 'when', 'who'],
            'command': ['do', 'execute', 'run', 'start', 'stop'],
            'request': ['please', 'can', 'could', 'would'],
            'statement': ['is', 'are', 'believe', 'think', 'know'],
        }

        text_lower = text.lower()
        intent_scores = {}

        for intent, keywords in intents_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            intent_scores[intent] = score

        return max(intent_scores, key=intent_scores.get) if intent_scores else 'unknown'

    def extract_keywords(self, text, top_n=5):
        """Extract top keywords from text"""
        tokens = self.tokenize(text)
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at',
            'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are'
        }
        filtered = [t for t in tokens if t not in stop_words]
        word_freq = Counter(filtered)
        return word_freq.most_common(top_n)

    def build_context(self, texts):
        """Build context from multiple texts"""
        all_tokens = []
        for text in texts:
            all_tokens.extend(self.tokenize(text))
        self.vocabulary.update(all_tokens)
        return all_tokens

    def process_text(self, text):
        """Complete text processing pipeline"""
        return {
            'original': text,
            'tokens': self.tokenize(text),
            'sentiment': self.analyze_sentiment(text),
            'intent': self.detect_intent(text),
            'entities': self.extract_entities(text),
            'keywords': self.extract_keywords(text),
        }

    def __repr__(self):
        return f"NLPEngine(Vocabulary: {len(self.vocabulary)})"
