from cached_function import CachedFunction
import pickle

def create_counter():
  def counter():
    if not hasattr(counter, "calls"):
      counter.calls = 0
    counter.calls += 1
    return counter.calls
  return counter

def test_cached_function_returns_value():
    add1 = lambda x: x + 1
    add1_cached = CachedFunction(add1)
    assert add1_cached.calculate_function_value(2) == 3


def test_uses_warm_cache():
    # Arrange
    add1 = lambda x: x + 1
    add1_cached = CachedFunction(add1, warm_cache = {((2,), frozenset()): 3})

    # Act
    result = add1_cached.calculate_function_value(2)

    # Assert
    assert result == 3

def test_cached_function_returns_cached_value():
    # Arrange
    counter = create_counter()
    counter_cached = CachedFunction(counter)
    counter_cached.calculate_function_value()

    # Act
    times_executed = counter_cached.calculate_function_value()

    # Assert
    assert times_executed == 1

def test_saves_to_file():
    # Arrange
    add_1 = lambda x: x + 1
    add_1_cached = CachedFunction(add_1)
    add_1_cached.calculate_function_value(2)

    # Act
    add_1_cached.save_to_file("test_cache")

    # Assert
    with open("test_cache", "rb") as f:
        cache_restored = pickle.load(f)
        assert cache_restored == {((2,), frozenset()): 3}

def test_cached_function_equality():
    # Arrange
    add_1 = lambda x: x + 1
    add_1_cached = CachedFunction(add_1)
    add_1_cached_2 = CachedFunction(add_1)

    # Act
    are_equal = add_1_cached == add_1_cached_2

    # Assert
    assert are_equal == True

def test_hash_should_be_consistent():
    # Arrange
    add_1 = lambda x: x + 1
    add_1_cached = CachedFunction(add_1)

    # Act
    hash1 = hash(add_1_cached)
    hash2 = hash(add_1_cached)

    # Assert
    assert hash1 == hash2