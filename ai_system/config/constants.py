"""Constants for Eugene AI System"""

# Emotion Types
EMOTIONS = [
    "joy", "sadness", "anger", "fear", "surprise",
    "disgust", "neutral", "anticipation", "trust"
]

# Threat Types
THREAT_TYPES = {
    "resource_scarcity": "Low resources available",
    "system_failure": "System component failure",
    "adversarial_attack": "Malicious attack detected",
    "data_corruption": "Data integrity compromised",
    "network_failure": "Network connectivity lost",
    "unknown_environment": "Uncharted territory detected",
}

# Decision Strategies
STRATEGIES = [
    "aggressive",
    "defensive",
    "balanced",
    "adaptive",
    "conservative",
    "exploratory"
]

# Learning Modes
LEARNING_MODES = [
    "supervised",
    "unsupervised",
    "reinforcement",
    "semi_supervised",
    "transfer"
]

# Success Thresholds
SUCCESS_THRESHOLDS = {
    "decision_accuracy": 0.95,
    "threat_detection": 0.98,
    "resource_optimization": 0.90,
    "response_quality": 0.92,
}

# Time Constants (in seconds)
TIME_CONSTANTS = {
    "decision_timeout": 2.0,
    "learning_interval": 60.0,
    "memory_consolidation": 3600.0,
    "adaptation_cycle": 300.0,
}

# Resource Limits
RESOURCE_LIMITS = {
    "max_concurrent_processes": 10,
    "max_memory_percent": 80,
    "max_cpu_percent": 90,
    "max_network_bandwidth_mbps": 100,
}

# Model Versions
MODEL_VERSIONS = {
    "neural_network": "v2.1",
    "nlp_engine": "v1.5",
    "decision_engine": "v1.3",
    "memory_system": "v1.2",
}

# Status Codes
STATUS_CODES = {
    "SUCCESS": 200,
    "PROCESSING": 202,
    "ERROR": 400,
    "THREAT_DETECTED": 403,
    "SYSTEM_ERROR": 500,
    "RESOURCE_EXHAUSTED": 507,
}
