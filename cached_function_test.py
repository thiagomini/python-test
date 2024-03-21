from cached_function import CachedFunction


def test_cached_function_returns_value():
    add1 = lambda x: x + 1
    add1_cached = CachedFunction(add1)
    assert add1_cached.calculate_function_value(2) == 3

def test_cached_function_returns_cached_value():
    # Arrange
    def counter():
        if not hasattr(counter, "calls"):
            counter.calls = 0

        counter.calls += 1
        return counter.calls
    counter_cached = CachedFunction(counter)
    counter_cached.calculate_function_value()

    # Act
    times_executed = counter_cached.calculate_function_value()

    # Assert
    assert times_executed == 1
