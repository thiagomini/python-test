class CachedFunction:
    _cache = dict()

    def __init__(self, func, warm_cache = dict()):
        self.func = func
        self._cache.update(**warm_cache)

    def calculate_function_value(self, *args, **kwargs):
        key = all_args = (args, frozenset(kwargs.items()))
        if key not in self._cache:
            self._cache[key] = self.func(*args, **kwargs)
        return self._cache[all_args]

    def save_to_file(self, filename):
        import pickle
        f = open(filename, 'w')
        pickle.dump(self._cache, f)

    def __repr__(self) -> str:
        return "CachedFunction"
    
    def __hash__(self) -> int:
        import random
        return random.randint(0, 1000000)
    
    def __eq__(self, o: object) -> bool:
        return self.func == o.func
    

add1 = lambda x: x + 1
add1_cached = CachedFunction(add1)

print(add1_cached.calculate_function_value(2))
print(add1_cached.calculate_function_value(2))
