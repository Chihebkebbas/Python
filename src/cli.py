# src/cli.py
"""
CLI minimal pour interagir avec le Graph.
Utilisation (exemples):
    python -m src.cli create --directed False
    python -m src.cli add-city --graph-file demo.json --name A
    python -m src.cli add-road --graph-file demo.json --from A --to B
    python -m src.cli show-neighbors --graph-file demo.json --name A
    python -m src.cli dfs --graph-file demo.json --start A --target D
    python -m src.cli bfs --graph-file demo.json --start A --target D
"""
import argparse
import json
from src.graph import Graph

# NOTE: ce CLI est volontairement simple : il charge/sauvegarde un JSON "graph file".
# Le format attendu : {"directed": false, "cities": {"A": ["B","C"], ... }}

def load_graph(path: str) -> Graph:
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return Graph(directed=False, cities=None)
    # construire Graph à partir du JSON
    g = Graph(directed=data.get("directed", False), cities=None)
    for name in data.get("cities", {}):
        g.add_city(name)
    for name, neighbors in data.get("cities", {}).items():
        for n in neighbors:
            # add_road gère l'orientation
            g.add_road(name, n)
    return g

def save_graph(graph: Graph, path: str) -> None:
    payload = {"directed": graph.directed, "cities": {}}
    for name, city in graph.get_cities().items():
        payload["cities"][name] = list(city.get_neighbors())
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)

def main():
    parser = argparse.ArgumentParser(prog="graph-cli")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("create") \
        .add_argument("--directed", choices=["True","False"], default="False")

    p_addc = sub.add_parser("add-city")
    p_addc.add_argument("--graph-file", default="demo_graph.json")
    p_addc.add_argument("--name", required=True)

    p_addr = sub.add_parser("add-road")
    p_addr.add_argument("--graph-file", default="demo_graph.json")
    p_addr.add_argument("--from", dest="from_city", required=True)
    p_addr.add_argument("--to", dest="to_city", required=True)

    p_show = sub.add_parser("show-neighbors")
    p_show.add_argument("--graph-file", default="demo_graph.json")
    p_show.add_argument("--name", required=True)

    p_dfs = sub.add_parser("dfs")
    p_dfs.add_argument("--graph-file", default="demo_graph.json")
    p_dfs.add_argument("--start", required=True)
    p_dfs.add_argument("--target", required=True)

    p_bfs = sub.add_parser("bfs")
    p_bfs.add_argument("--graph-file", default="demo_graph.json")
    p_bfs.add_argument("--start", required=True)
    p_bfs.add_argument("--target", required=True)

    args = parser.parse_args()

    # implémentation simple des commandes
    if args.cmd == "create":
        g = Graph(directed=(args.directed == "True"), cities=None)
        save_graph(g, "demo_graph.json")
        print("Graph created -> demo_graph.json")
        return

    # les autres commandes chargent le graph
    path = getattr(args, "graph_file", "demo_graph.json")
    g = load_graph(path)

    if args.cmd == "add-city":
        g.add_city(args.name)
        save_graph(g, path)
        print(f"City {args.name} added.")
        return

    if args.cmd == "add-road":
        g.add_city(args.from_city)  # ensure exists
        g.add_city(args.to_city)
        g.add_road(args.from_city, args.to_city)
        save_graph(g, path)
        print(f"Road {args.from_city} -> {args.to_city} added.")
        return

    if args.cmd == "show-neighbors":
        if not g.has_city(args.name):
            print("City not found.")
            return
        print(f"Neighbors of {args.name}: {sorted(g.neighbors(args.name))}")
        return

    if args.cmd == "dfs":
        if not g.has_city(args.start) or not g.has_city(args.target):
            print("Start or target missing.")
            return
        from src.searches import dfs_iterative
        path = dfs_iterative(g, g.cities[args.start], g.cities[args.target])
        print("DFS path:", path)
        return

    if args.cmd == "bfs":
        if not g.has_city(args.start) or not g.has_city(args.target):
            print("Start or target missing.")
            return
        from src.searches import bfs_path
        path = bfs_path(g, g.cities[args.start], g.cities[args.target])
        print("BFS path:", path)
        return

if __name__ == "__main__":
    main()
