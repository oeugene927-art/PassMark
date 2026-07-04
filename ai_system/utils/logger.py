"""Logging Utilities for Eugene AI"""

import logging
from datetime import datetime
from config.settings import LOGGING_SETTINGS


class EugeneLogger:
    """Custom logger for Eugene AI System"""

    def __init__(self, name="Eugene"):
        """Initialize logger"""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(LOGGING_SETTINGS["log_level"])
        self.setup_handlers()

    def setup_handlers(self):
        """Setup logging handlers"""
        formatter = logging.Formatter(LOGGING_SETTINGS["log_format"])

        # File handler
        try:
            file_handler = logging.FileHandler(LOGGING_SETTINGS["log_file"])
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        except Exception as e:
            print(f"Could not setup file handler: {e}")

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log_action(self, action, details=None):
        """Log an action"""
        message = f"[{action}] {details or ''}"
        self.logger.info(message)

    def log_error(self, error_msg):
        """Log an error"""
        self.logger.error(error_msg)

    def log_warning(self, warning_msg):
        """Log a warning"""
        self.logger.warning(warning_msg)
