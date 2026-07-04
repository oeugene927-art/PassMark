"""Resource Management Module for Eugene AI"""

from config.settings import RESOURCE_SETTINGS, RESOURCE_LIMITS


class ResourceManager:
    """System for managing and optimizing resources"""

    def __init__(self):
        """Initialize resource manager"""
        self.settings = RESOURCE_SETTINGS
        self.memory_used_mb = 0
        self.cpu_utilization = 0.0
        self.network_bandwidth_used = 0
        self.active_processes = 0
        self.resource_history = []

    def allocate_memory(self, amount_mb):
        """Allocate memory for a process"""
        if self.memory_used_mb + amount_mb > self.settings["total_memory_mb"]:
            return False

        self.memory_used_mb += amount_mb
        return True

    def deallocate_memory(self, amount_mb):
        """Deallocate memory from a process"""
        self.memory_used_mb = max(0, self.memory_used_mb - amount_mb)
        return True

    def start_process(self):
        """Start a new process"""
        if self.active_processes >= RESOURCE_LIMITS["max_concurrent_processes"]:
            return False

        self.active_processes += 1
        return True

    def end_process(self):
        """End a running process"""
        self.active_processes = max(0, self.active_processes - 1)
        return True

    def update_cpu_utilization(self, utilization):
        """Update CPU utilization percentage"""
        self.cpu_utilization = min(1.0, max(0.0, utilization))

    def optimize_resources(self):
        """Optimize resource allocation"""
        if self.settings["optimization_enabled"]:
            target_cpu = self.settings["cpu_utilization_target"]
            if self.cpu_utilization > target_cpu:
                self.active_processes = max(1, int(self.active_processes * 0.9))

    def get_resource_status(self):
        """Get current resource status"""
        memory_percent = (self.memory_used_mb / self.settings["total_memory_mb"]) * 100
        cpu_percent = self.cpu_utilization * 100

        return {
            'memory_used_mb': self.memory_used_mb,
            'memory_percent': memory_percent,
            'cpu_utilization': cpu_percent,
            'active_processes': self.active_processes,
            'network_bandwidth_used': self.network_bandwidth_used,
        }

    def __repr__(self):
        memory_pct = (self.memory_used_mb / self.settings["total_memory_mb"]) * 100
        return f"ResourceManager(Memory: {memory_pct:.1f}%, CPU: {self.cpu_utilization*100:.1f}%)"
