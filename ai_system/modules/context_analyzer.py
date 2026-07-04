"""Context Analysis Module for Eugene AI"""

from collections import deque
from datetime import datetime, timedelta


class ContextAnalyzer:
    """System for understanding and managing context"""

    def __init__(self, context_window_size=5):
        """Initialize context analyzer"""
        self.context_window = deque(maxlen=context_window_size)
        self.conversation_history = []
        self.current_topic = None
        self.entities_in_context = {}

    def add_context(self, data):
        """Add context data"""
        context_item = {
            'data': data,
            'timestamp': datetime.now(),
        }
        self.context_window.append(context_item)
        self.conversation_history.append(context_item)

    def analyze_context(self):
        """Analyze current context"""
        analysis = {
            'window_size': len(self.context_window),
            'current_topic': self.current_topic,
            'entities': self.entities_in_context,
            'conversation_length': len(self.conversation_history),
        }
        return analysis

    def identify_topic(self, text):
        """Identify main topic from text"""
        topics_keywords = {
            'technical': ['code', 'program', 'system', 'data', 'algorithm'],
            'general': ['hello', 'hi', 'how', 'what', 'why'],
            'business': ['company', 'profit', 'market', 'sales', 'customer'],
            'science': ['research', 'study', 'hypothesis', 'experiment', 'theory'],
        }

        text_lower = text.lower()
        topic_scores = {}

        for topic, keywords in topics_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            topic_scores[topic] = score

        if max(topic_scores.values()) > 0:
            self.current_topic = max(topic_scores, key=topic_scores.get)
        else:
            self.current_topic = 'general'

        return self.current_topic

    def update_entities(self, entities):
        """Update entities in current context"""
        self.entities_in_context.update(entities)

    def get_context_summary(self):
        """Get summary of current context"""
        return {
            'topic': self.current_topic,
            'context_items': len(self.context_window),
            'entities': len(self.entities_in_context),
            'history_length': len(self.conversation_history),
        }

    def __repr__(self):
        return f"ContextAnalyzer(Topic: {self.current_topic}, Window: {len(self.context_window)})"
