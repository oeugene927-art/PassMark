"""Memory Management System for Eugene AI"""

from datetime import datetime, timedelta
from collections import deque
import json

from config.settings import MEMORY_SETTINGS


class Memory:
    """Advanced memory system with short and long-term storage"""

    def __init__(self):
        """Initialize memory system"""
        self.settings = MEMORY_SETTINGS
        self.short_term = deque(maxlen=self.settings["short_term_capacity"])
        self.long_term = {}
        self.access_log = []

    def remember_short_term(self, data):
        """Store in short-term memory"""
        memory_item = {
            'data': data,
            'timestamp': datetime.now(),
            'access_count': 0,
        }
        self.short_term.append(memory_item)
        return True

    def remember_long_term(self, key, data):
        """Store in long-term memory"""
        memory_item = {
            'data': data,
            'timestamp': datetime.now(),
            'access_count': 0,
            'importance': 1.0,
        }
        self.long_term[key] = memory_item
        return True

    def recall_short_term(self, query=None):
        """Recall from short-term memory"""
        if query is None:
            return list(self.short_term)

        results = []
        for item in self.short_term:
            if self._matches_query(item['data'], query):
                results.append(item)

        return results

    def recall_long_term(self, key):
        """Recall from long-term memory"""
        if key in self.long_term:
            item = self.long_term[key]
            item['access_count'] += 1
            self.access_log.append({
                'key': key,
                'timestamp': datetime.now(),
            })
            return item['data']
        return None

    def consolidate_memory(self):
        """Move important short-term memories to long-term"""
        consolidation_threshold = self.settings["consolidation_threshold"]

        for item in list(self.short_term):
            if item['access_count'] > consolidation_threshold:
                key = f"mem_{len(self.long_term)}"
                item['importance'] = item['access_count']
                self.long_term[key] = item

    def forget_old_memories(self):
        """Forget old memories based on retention period"""
        retention_days = self.settings["retention_period_days"]
        cutoff_date = datetime.now() - timedelta(days=retention_days)

        keys_to_remove = []
        for key, item in self.long_term.items():
            if item['timestamp'] < cutoff_date:
                keys_to_remove.append(key)

        for key in keys_to_remove:
            del self.long_term[key]

    def _matches_query(self, data, query):
        """Check if data matches query"""
        if isinstance(data, dict):
            for key, value in query.items():
                if key not in data or data[key] != value:
                    return False
            return True
        return str(query) in str(data)

    def get_memory_stats(self):
        """Get memory statistics"""
        return {
            'short_term_items': len(self.short_term),
            'long_term_items': len(self.long_term),
            'total_accesses': len(self.access_log),
            'short_term_capacity': self.settings["short_term_capacity"],
        }

    def __repr__(self):
        return f"Memory(ST: {len(self.short_term)}, LT: {len(self.long_term)})"
