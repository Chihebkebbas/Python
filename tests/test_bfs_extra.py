# tests/test_bfs_extra.py
import pytest
from src.city import City
from src.graph import Graph
from src.searches import bfs_path


def build_chain_graph():
    g = Graph(directed=False, cities={})
    for name in ["A", "B", "C"]:
        g.add_city(name)
    g.add_road("A", "B")
    g.add_road("B", "C")
    return g

def build_directed_graph():
    g = Graph(directed=True, cities={})
    for name in ["A", "B", "C"]:
        g.add_city(name)
    g.add_road("A", "B")  # A -> B
    return g

def build_two_paths_graph():
    g = Graph(directed=False, cities={})
    for name in ["A", "B", "C", "D"]:
        g.add_city(name)
    g.add_road("A", "B")
    g.add_road("B", "D")
    g.add_road("A", "C")
    g.add_road("C", "D")
    return g

def build_long_and_short_paths_graph():
    g = Graph(directed=False, cities={})
    # A - B - D  (short)
    # A - X - Y - D (long)
    for name in ["A", "B", "D", "X", "Y"]:
        g.add_city(name)
    g.add_road("A", "B")
    g.add_road("B", "D")
    g.add_road("A", "X")
    g.add_road("X", "Y")
    g.add_road("Y", "D")
    return g

def build_large_chain(n=100):
    g = Graph(directed=False, cities={})
    names = [f"N{i}" for i in range(n)]
    for name in names:
        g.add_city(name)
    for i in range(n - 1):
        g.add_road(names[i], names[i + 1])
    return g, names


# ---------- Tests ----------

def assert_path_is_valid(graph: Graph, path: list[str]):
    """Helper: vérifie que chaque arête consécutive existe dans le graphe."""
    if not path:
        return
    for u, v in zip(path, path[1:]):
        assert v in graph.neighbors(u), f"Arête manquante entre {u} et {v}"


def test_bfs_returns_correct_chain():
    g = build_chain_graph()
    path = bfs_path(g, g.cities["A"], g.cities["C"])
    assert path == ["A", "B", "C"]
    assert_path_is_valid(g, path)

def test_bfs_directed_respects_orientation():
    g = build_directed_graph()
    # A -> B reachable
    path_ab = bfs_path(g, g.cities["A"], g.cities["B"])
    assert path_ab == ["A", "B"]
    # B -> A not reachable in directed graph
    path_ba = bfs_path(g, g.cities["B"], g.cities["A"])
    assert path_ba == []

def test_bfs_two_equal_length_paths():
    g = build_two_paths_graph()
    path = bfs_path(g, g.cities["A"], g.cities["D"])
    assert len(path) == 3  # A -> ? -> D (2 edges, 3 nodes)
    assert path[0] == "A"
    assert path[-1] == "D"
    assert_path_is_valid(g, path)

def test_bfs_returns_shortest_path_when_other_longer_exists():
    g = build_long_and_short_paths_graph()
    path = bfs_path(g, g.cities["A"], g.cities["D"])
    # court chemin attendu : ["A","B","D"] (3 noeuds)
    assert len(path) == 3
    assert_path_is_valid(g, path)

def test_bfs_large_graph_chain():
    g, names = build_large_chain(n=100)
    start = g.cities[names[0]]
    end = g.cities[names[-1]]
    path = bfs_path(g, start, end)
    assert len(path) == 100
    assert path[0] == names[0]
    assert path[-1] == names[-1]
    assert_path_is_valid(g, path)

def test_bfs_unreachable_returns_empty():
    g = build_chain_graph()
    g.add_city("X")  # ville isolée
    path = bfs_path(g, g.cities["A"], g.cities["X"])
    assert path == []

def test_bfs_missing_city_raises():
    g = build_chain_graph()
    with pytest.raises(ValueError):
        bfs_path(g, City("Z", set()), g.cities["A"])
