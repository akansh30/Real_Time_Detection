class ObjectMonitor:
    def __init__(self):
        self.active_ids = set()

    def update(self, current_ids):
        # Handle edge cases where IDs can reset
        missing = self.active_ids - current_ids
        new = current_ids - self.active_ids
        self.active_ids = current_ids.copy()
        return missing, new