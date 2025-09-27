from src.city import City

from src.graph import Graph
from src.queue import Queue
from src.stack import Stack


def dfs_recursive(graph: Graph, start: City, target: City) -> bool:
    if not graph.has_city(start.name) or not graph.has_city(target.name):
        raise ValueError("Start or target city not found")

    if start.name == target.name:
        return True

    visited = set()

    def visite(city: str) -> bool:
        if city == target.name:
            return True
        visited.add(city)
        for neighbor in sorted(graph.neighbors(city)):
            if neighbor not in visited:
                if visite(neighbor):
                    return True
        return False

    return visite(start.name)

def dfs_iterative(graph: Graph, start: City, target: City) -> list[str] | None:
    if start.name not in graph.cities or target.name not in graph.cities:
        raise ValueError("Start or target city not in graph")

    if start.name == target.name:
        return [start.name]


    stack = Stack()
    stack.push(start.name)
    visited = set()
    parent = {start.name: None}  # pour reconstituer le chemin

    while not stack.is_empty():
        city = stack.pop()
        if city == target.name:
            path = []
            current = city
            while current is not None:
                path.append(current)
                current = parent.get(current)
            path.reverse()
            return path
        if city not in visited:
            visited.add(city)
            for neighbor in sorted(graph.neighbors(city)):
                if neighbor not in visited and neighbor not in stack.items:
                    stack.push(neighbor)
                    parent[neighbor] = city
    return []

def bfs_path(graph: Graph, start: City, target: City) -> list[str]:
    if start.name not in graph.cities or target.name not in graph.cities:
        raise ValueError("Start or taget city not found")

    if start.name == target.name:
        return [start.name]

    queue = Queue()
    visited = set()
    parent = {start.name: None} # child -> parent # Le premier élément Root n'as pas de parents None

    queue.enqueue(start.name)
    visited.add(start.name)

    while not queue.is_empty():
        city = queue.dequeue()
        for neighbor in sorted(graph.neighbors(city)):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = city
                if neighbor == target.name:
                    path = [neighbor]
                    while parent[path[-1]] is not None:
                        path.append(parent[path[-1]])
                    path.reverse()  # retourner du start au target
                    return path
                queue.enqueue(neighbor)
    return []
