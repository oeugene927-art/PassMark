"""Data Processing Utilities"""

import json
import csv
from datetime import datetime


class DataProcessor:
    """Utilities for processing various data formats"""

    @staticmethod
    def load_json(filepath):
        """Load data from JSON file"""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading JSON: {e}")
            return None

    @staticmethod
    def save_json(data, filepath):
        """Save data to JSON file"""
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            return True
        except Exception as e:
            print(f"Error saving JSON: {e}")
            return False

    @staticmethod
    def load_csv(filepath):
        """Load data from CSV file"""
        try:
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return None

    @staticmethod
    def normalize_data(data, min_val=0, max_val=1):
        """Normalize data to range [min_val, max_val]"""
        if not data:
            return data

        data_min = min(data)
        data_max = max(data)
        range_val = data_max - data_min

        if range_val == 0:
            return [min_val] * len(data)

        normalized = [
            ((x - data_min) / range_val) * (max_val - min_val) + min_val
            for x in data
        ]
        return normalized

    @staticmethod
    def split_data(data, train_ratio=0.8):
        """Split data into training and testing sets"""
        split_index = int(len(data) * train_ratio)
        return data[:split_index], data[split_index:]
