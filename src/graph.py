from typing import Dict, Set

from src.city import City


class Graph:
    def __init__(self, directed: bool, cities: Dict[str, City]):
        self.directed = directed
        self.cities: Dict[str, City] = cities

    def add_city(self, name: str) -> None:
        if name not in self.cities:
            self.cities[name] = City(name, set())

    def has_city(self, name: str) -> bool:
        return name in self.cities

    def remove_city(self, name: str) -> None:
        if name in self.cities:
            del self.cities[name]

    def add_road(self, from_city: str, to_city: str) -> None:
        if from_city in self.cities and to_city in self.cities:
            self.cities[from_city].add_neighbor(to_city)
            if not self.directed:
                self.cities[to_city].add_neighbor(from_city)

    def remove_road(self, from_city: str, to_city: str) -> None:
        if from_city in self.cities and to_city in self.cities:
            self.cities[from_city].remove_neighbor(to_city)
            if not self.directed:
                self.cities[to_city].remove_neighbor(from_city)

    def neighbors(self, name: str) -> Set[str]:
        return self.cities[name].neighbor

    def get_cities(self) -> Dict[str, City]:
        return self.cities

    def __repr__(self) -> str:
        return f"Graph(directed={self.directed}, cities={self.cities})"

