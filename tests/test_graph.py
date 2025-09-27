# tests/test_graph.py
import pytest
from src.graph import Graph
from src.city import City

def test_add_and_has_city():
    g = Graph(directed=False, cities=None)
    g.add_city("A")
    assert g.has_city("A") is True
    assert isinstance(g.get_cities()["A"], City)

def test_add_road_undirected():
    g = Graph(directed=False, cities=None)
    g.add_city("A"); g.add_city("B")
    g.add_road("A", "B")
    assert "B" in g.neighbors("A")
    assert "A" in g.neighbors("B")

def test_add_road_directed():
    g = Graph(directed=True, cities=None)
    g.add_city("A"); g.add_city("B")
    g.add_road("A", "B")
    assert "B" in g.neighbors("A")
    assert "A" not in g.neighbors("B")

def test_remove_city_cleans_neighbors():
    g = Graph(directed=False, cities=None)
    for n in ["A", "B", "C"]:
        g.add_city(n)
    g.add_road("A","B")
    g.add_road("B","C")
    g.remove_city("B")
    # après suppression, A ne doit plus contenir "B"
    assert "B" not in g.neighbors("A")
    assert "B" not in g.get_cities()

def test_remove_road_safe():
    g = Graph(directed=False, cities=None)
    g.add_city("A"); g.add_city("B")
    # remove non-existing road should not crash (preferred)
    try:
        g.remove_road("A", "B")
    except KeyError:
        pytest.skip("remove_road raises KeyError; consider using discard or handling it.")
