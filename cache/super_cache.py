# cache/super_cache.py
class SuperCache:
    def __init__(self):
        self.cache = {}

    def load_data(self, key, data):
        """Carga datos en caché bajo una clave específica."""
        self.cache[key] = data

    def get_data(self, key):
        """Obtiene datos desde la caché."""
        return self.cache.get(key, None)

    def clear_data(self, key=None):
        """Limpia datos específicos o toda la caché."""
        if key:
            self.cache.pop(key, None)
        else:
            self.cache.clear()


