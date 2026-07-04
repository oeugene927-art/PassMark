#!/usr/bin/env python3
"""
Eugene de Survivor - Advanced AI System
Main entry point
"""

import sys
from datetime import datetime

from core.neural_network import EugeneAI
from core.nlp_engine import NLPEngine
from core.decision_engine import DecisionEngine
from core.memory_system import Memory
from core.adaptation_system import AdaptationSystem
from modules.threat_assessment import ThreatAssessmentSystem
from modules.resource_manager import ResourceManager
from modules.context_analyzer import ContextAnalyzer
from modules.dialogue_system import DialogueSystem
from utils.logger import EugeneLogger
from utils.metrics import MetricsCollector
from config.settings import AI_NAME, AI_VERSION


class EugeneSystem:
    """Main Eugene AI System coordinator"""

    def __init__(self):
        """Initialize Eugene System"""
        self.name = AI_NAME
        self.version = AI_VERSION
        self.status = "initializing"
        self.logger = EugeneLogger("Eugene")

        # Initialize core systems
        self.ai = EugeneAI(self.name)
        self.nlp = NLPEngine()
        self.decision_engine = DecisionEngine()
        self.memory = Memory()
        self.adaptation = AdaptationSystem()

        # Initialize modules
        self.threat_system = ThreatAssessmentSystem()
        self.resource_manager = ResourceManager()
        self.context_analyzer = ContextAnalyzer()
        self.dialogue = DialogueSystem()

        # Metrics
        self.metrics = MetricsCollector()

        self.status = "ready"
        self.logger.log_action("INIT", f"{self.name} v{self.version} initialized")

    def process_input(self, user_input):
        """Process user input through all systems"""
        self.logger.log_action("INPUT", user_input)

        # NLP Analysis
        nlp_result = self.nlp.process_text(user_input)
        self.logger.log_action("NLP_ANALYSIS", f"Intent: {nlp_result['intent']}")

        # Memory
        self.memory.remember_short_term(user_input)

        # Context Analysis
        self.context_analyzer.add_context(user_input)
        topic = self.context_analyzer.identify_topic(user_input)

        # Dialogue
        response = self.dialogue.generate_response(user_input, nlp_result['intent'])
        self.dialogue.add_turn(user_input, response)

        # Decision making
        options = ['response_type_a', 'response_type_b', 'response_type_c']
        decision = self.decision_engine.make_decision(options)

        return {
            'input': user_input,
            'nlp': nlp_result,
            'topic': topic,
            'response': response,
            'decision': decision,
            'timestamp': datetime.now().isoformat(),
        }

    def run_interactive(self):
        """Run interactive mode"""
        print(f"\n{'='*60}")
        print(f"  {self.name} v{self.version}")
        print(f"  Advanced AI System")
        print(f"{'='*60}\n")
        print("Commands:")
        print("  'chat' - Chat with Eugene")
        print("  'status' - Show system status")
        print("  'threat' - Assess threats")
        print("  'resources' - Show resource usage")
        print("  'help' - Show this help")
        print("  'quit' - Exit\n")

        while True:
            try:
                command = input(f"{self.name}> ").strip().lower()

                if command == 'quit':
                    print(f"\nShutting down {self.name}... Goodbye!")
                    break
                elif command == 'chat':
                    self.interactive_chat()
                elif command == 'status':
                    self.show_status()
                elif command == 'threat':
                    self.assess_threats_interactive()
                elif command == 'resources':
                    self.show_resources()
                elif command == 'help':
                    self.show_help()
                else:
                    print("Unknown command. Type 'help' for commands.")
            except KeyboardInterrupt:
                print(f"\n{self.name} interrupted.")
                break

    def interactive_chat(self):
        """Interactive chat mode"""
        print("\n--- Chat Mode (type 'back' to return) ---\n")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == 'back':
                break
            if not user_input:
                continue

            result = self.process_input(user_input)
            print(f"Eugene: {result['response']}")
            print(f"  [Topic: {result['topic']}, Intent: {result['nlp']['intent']}]\n")

    def show_status(self):
        """Show system status"""
        print(f"\n--- {self.name} Status ---")
        print(f"Status: {self.status}")
        print(f"AI Status: {self.ai.get_status()}")
        print(f"Memory: {self.memory.get_memory_stats()}")
        print(f"Threat Level: {self.threat_system.get_threat_status()}")
        print(f"Dialogue: {self.dialogue.get_conversation_stats()}\n")

    def assess_threats_interactive(self):
        """Assess threats interactively"""
        print("\n--- Threat Assessment ---")
        print("Available threats: resource_scarcity, system_failure, adversarial_attack, data_corruption, network_failure, unknown_environment")
        threat_type = input("Enter threat type: ").strip()
        severity = float(input("Enter severity (0-1): ").strip())

        result = self.threat_system.assess_threat(threat_type, severity)
        print(f"Threat Assessment Result: {result}")
        print(f"Current Threat Level: {self.threat_system.threat_level}\n")

    def show_resources(self):
        """Show resource usage"""
        status = self.resource_manager.get_resource_status()
        print(f"\n--- Resource Usage ---")
        for key, value in status.items():
            print(f"{key}: {value}")
        print()

    def show_help(self):
        """Show help information"""
        print("\n--- Eugene de Survivor Help ---")
        print("An advanced AI system with:")
        print("  • Neural Network Processing")
        print("  • Natural Language Understanding")
        print("  • Strategic Decision Making")
        print("  • Adaptive Learning")
        print("  • Threat Assessment")
        print("  • Resource Management")
        print("  • Memory Systems\n")


def main():
    """Main entry point"""
    try:
        eugene = EugeneSystem()
        eugene.run_interactive()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
