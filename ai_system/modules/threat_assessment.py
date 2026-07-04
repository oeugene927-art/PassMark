"""Threat Assessment Module for Eugene AI"""

from config.settings import THREAT_SETTINGS
from config.constants import THREAT_TYPES


class ThreatAssessmentSystem:
    """System for detecting and assessing threats"""

    def __init__(self):
        """Initialize threat assessment system"""
        self.settings = THREAT_SETTINGS
        self.threat_log = []
        self.threat_level = "none"
        self.active_threats = []

    def assess_threat(self, threat_type, severity=0.5, context=None):
        """Assess a specific threat"""
        if threat_type not in THREAT_TYPES:
            return None

        threat_data = {
            'type': threat_type,
            'severity': min(1.0, max(0.0, severity)),
            'context': context,
            'timestamp': __import__('datetime').datetime.now(),
            'mitigated': False,
        }

        self.threat_log.append(threat_data)
        self._update_threat_level()

        return threat_data

    def _update_threat_level(self):
        """Update overall threat level based on active threats"""
        if not self.threat_log:
            self.threat_level = "none"
            return

        recent_threats = self.threat_log[-10:]  # Last 10 threats
        avg_severity = sum(t['severity'] for t in recent_threats) / len(recent_threats)

        if avg_severity >= 0.9:
            self.threat_level = "critical"
        elif avg_severity >= 0.7:
            self.threat_level = "high"
        elif avg_severity >= 0.5:
            self.threat_level = "medium"
        elif avg_severity >= 0.3:
            self.threat_level = "low"
        else:
            self.threat_level = "none"

    def mitigate_threat(self, threat_id):
        """Take action to mitigate threat"""
        if 0 <= threat_id < len(self.threat_log):
            self.threat_log[threat_id]['mitigated'] = True
            self._update_threat_level()
            return True
        return False

    def get_threat_status(self):
        """Get current threat status"""
        return {
            'threat_level': self.threat_level,
            'active_threats': len([t for t in self.threat_log if not t['mitigated']]),
            'total_threats': len(self.threat_log),
        }

    def __repr__(self):
        return f"ThreatAssessment(Level: {self.threat_level}, Active: {len([t for t in self.threat_log if not t['mitigated']])})"
