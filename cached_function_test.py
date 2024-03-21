from cached_function import CachedFunction


def test_cached_function_returns_value():
    add1 = lambda x: x + 1
    add1_cached = CachedFunction(add1)
    assert add1_cached.calculate_function_value(2) == 3
    assert add1_cached.calculate_function_value(2) == 3