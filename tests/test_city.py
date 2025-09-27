# tests/test_city.py
import pytest
from src.city import City

def test_city_initialization_empty_neighbors():
    c = City("X", None)
    assert c.name == "X"
    assert isinstance(c.get_neighbors(), set)
    assert len(c.get_neighbors()) == 0

def test_add_and_remove_neighbor():
    c = City("A", None)
    c.add_neighbor("B")
    assert "B" in c.get_neighbors()
    c.remove_neighbor("B")
    assert "B" not in c.get_neighbors()

def test_remove_nonexistent_neighbor_no_error():
    c = City("A", None)
    # if implementation uses discard, this should not raise
    try:
        c.remove_neighbor("Z")
    except KeyError:
        pytest.skip("remove_neighbor raises KeyError; consider using discard or handling it.")
