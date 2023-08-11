import psutil

class MemoryMonitor:
    def __init__(self):
        pass

    def get_memory_usage(self):
        memory_info = psutil.virtual_memory()
        return {
            'total': memory_info.total,
            'available': memory_info.available,
            'used': memory_info.used,
            'percent': memory_info.percent
        }
