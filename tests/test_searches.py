# tests/test_searches.py
import pytest
from src.graph import Graph
from src.city import City
from src.searches import dfs_recursive, dfs_iterative, bfs_path

def make_chain():
    g = Graph(directed=False, cities=None)
    for n in ["A","B","C"]:
        g.add_city(n)
    g.add_road("A","B"); g.add_road("B","C")
    return g

def test_dfs_recursive_basic():
    g = make_chain()
    assert dfs_recursive(g, g.cities["A"], g.cities["C"]) is True

def test_dfs_iterative_returns_path():
    g = make_chain()
    path = dfs_iterative(g, g.cities["A"], g.cities["C"])
    assert path[0] == "A" and path[-1] == "C"

def test_bfs_path_chain():
    g = make_chain()
    assert bfs_path(g, g.cities["A"], g.cities["C"]) == ["A","B","C"]

def test_missing_city_raises():
    g = make_chain()
    with pytest.raises(ValueError):
        dfs_recursive(g, City("Z", set()), g.cities["A"])
