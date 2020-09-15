
class ProxyDict:
    def __init__(self, wrap_dict: dict):
        self._dict = wrap_dict
    
    def __getitem__(self, key):
        return self._dict[key]

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict)

    def __repr__(self):
        return f"ProxyDict({self._dict})"
    
    def __eq__(self, other):
        if isinstance(other, dict):
            return self._dict == other
        elif isinstance(other, ProxyDict):
            return self._dict == other._dict
        else:
            return False
    
    def keys(self):
        return self._dict.keys()
    
    def values(self):
        return self._dict.values()
    
    def items(self):
        return self._dict.items()

    def get(self, key, default=None):
        return self._dict.get(key, default)