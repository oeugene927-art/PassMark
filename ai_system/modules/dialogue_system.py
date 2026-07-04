"""Dialogue System for Eugene AI"""

from datetime import datetime


class DialogueSystem:
    """System for managing conversations and dialogue"""

    def __init__(self):
        """Initialize dialogue system"""
        self.conversation_log = []
        self.dialogue_state = "idle"
        self.turn_count = 0
        self.greeting_phrases = [
            "Hello! I am Eugene de Survivor.",
            "Greetings! How may I assist you?",
            "Welcome! Let's begin.",
        ]
        self.response_templates = {
            'greeting': "Hello! Nice to meet you.",
            'question': "That's an interesting question. Let me think about it.",
            'statement': "I understand. Thank you for sharing that.",
            'request': "I'll do my best to help you with that.",
        }

    def start_conversation(self, user_input):
        """Start a new conversation"""
        self.dialogue_state = "active"
        self.turn_count = 0
        self.add_turn(user_input, None)

    def add_turn(self, user_input, ai_response=None):
        """Add a turn to conversation"""
        turn = {
            'turn_number': self.turn_count,
            'user_input': user_input,
            'ai_response': ai_response,
            'timestamp': datetime.now(),
        }
        self.conversation_log.append(turn)
        self.turn_count += 1

    def generate_response(self, user_input, intent):
        """Generate appropriate response based on intent"""
        if intent in self.response_templates:
            return self.response_templates[intent]
        else:
            return f"I understand: {user_input}. How can I help you further?"

    def end_conversation(self):
        """End conversation"""
        self.dialogue_state = "idle"
        return "Thank you for the conversation. Goodbye!"

    def get_conversation_history(self):
        """Get full conversation history"""
        return self.conversation_log

    def get_conversation_stats(self):
        """Get conversation statistics"""
        return {
            'state': self.dialogue_state,
            'turn_count': self.turn_count,
            'conversation_length': len(self.conversation_log),
        }

    def __repr__(self):
        return f"DialogueSystem(State: {self.dialogue_state}, Turns: {self.turn_count})"
