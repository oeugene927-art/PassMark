"""Settings and configuration for Eugene AI"""

import os
from datetime import datetime

# AI Configuration
AI_NAME = "Eugene de Survivor"
AI_VERSION = "1.0.0"
AI_BUILD_DATE = datetime.now().isoformat()

# Neural Network Settings
NEURAL_SETTINGS = {
    "input_layer_size": 256,
    "hidden_layers": [512, 256, 128],
    "output_layer_size": 64,
    "activation_function": "relu",
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 100,
    "dropout_rate": 0.2,
}

# Memory System Settings
MEMORY_SETTINGS = {
    "short_term_capacity": 1000,  # Recent interactions
    "long_term_capacity": 10000,  # Historical data
    "consolidation_threshold": 0.7,
    "recall_speed": "fast",
    "retention_period_days": 365,
}

# Decision Engine Settings
DECISION_SETTINGS = {
    "decision_threshold": 0.75,
    "exploration_rate": 0.2,
    "confidence_minimum": 0.60,
    "strategy_type": "adaptive",
    "optimization_method": "policy_gradient",
}

# NLP Settings
NLP_SETTINGS = {
    "language_model": "bert-base-uncased",
    "max_sequence_length": 512,
    "sentiment_threshold": 0.5,
    "emotion_detection": True,
    "context_window": 5,
}

# Threat Assessment Settings
THREAT_SETTINGS = {
    "threat_levels": ["critical", "high", "medium", "low", "none"],
    "response_time_ms": 50,
    "assessment_frequency": "continuous",
    "mitigation_strategies": True,
}

# Resource Management Settings
RESOURCE_SETTINGS = {
    "total_memory_mb": 2048,
    "cpu_utilization_target": 0.7,
    "optimization_enabled": True,
    "resource_pooling": True,
}

# Adaptation Settings
ADAPTATION_SETTINGS = {
    "learning_rate_adaptive": True,
    "evolution_speed": "fast",
    "mutation_rate": 0.1,
    "fitness_threshold": 0.8,
    "population_size": 100,
}

# Logging Settings
LOGGING_SETTINGS = {
    "log_level": "INFO",
    "log_file": "logs/eugene_ai.log",
    "max_log_size_mb": 100,
    "backup_count": 5,
    "log_format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
}

# Paths
PATHS = {
    "models_dir": "ai_system/data/models",
    "training_data_dir": "ai_system/data/training_data",
    "logs_dir": "logs",
    "config_dir": "ai_system/config",
}

# Performance Targets
PERFORMANCE_TARGETS = {
    "response_time_ms": 100,
    "accuracy_percentage": 95,
    "throughput_requests_per_sec": 100,
    "uptime_percentage": 99.9,
}

# Feature Flags
FEATURES = {
    "multi_agent_support": True,
    "predictive_analytics": True,
    "real_time_learning": True,
    "emotional_intelligence": True,
    "strategic_planning": True,
    "threat_detection": True,
}
