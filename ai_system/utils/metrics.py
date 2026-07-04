"""Performance Metrics Utilities"""

from datetime import datetime
from collections import defaultdict


class MetricsCollector:
    """Collect and analyze performance metrics"""

    def __init__(self):
        """Initialize metrics collector"""
        self.metrics = defaultdict(list)
        self.start_time = datetime.now()

    def record_metric(self, metric_name, value):
        """Record a metric value"""
        self.metrics[metric_name].append({
            'value': value,
            'timestamp': datetime.now(),
        })

    def get_average(self, metric_name):
        """Get average value for a metric"""
        values = [m['value'] for m in self.metrics[metric_name]]
        return sum(values) / len(values) if values else 0

    def get_max(self, metric_name):
        """Get max value for a metric"""
        values = [m['value'] for m in self.metrics[metric_name]]
        return max(values) if values else 0

    def get_min(self, metric_name):
        """Get min value for a metric"""
        values = [m['value'] for m in self.metrics[metric_name]]
        return min(values) if values else 0

    def get_summary(self):
        """Get summary of all metrics"""
        summary = {}
        for metric_name in self.metrics:
            summary[metric_name] = {
                'average': self.get_average(metric_name),
                'max': self.get_max(metric_name),
                'min': self.get_min(metric_name),
                'count': len(self.metrics[metric_name]),
            }
        return summary
