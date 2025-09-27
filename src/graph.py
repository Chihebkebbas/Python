from typing import Dict, Set

from src.city import City


class Graph:
    def __init__(self, directed: bool, cities: Dict[str, City] = None): # = None veut dire que cities c'est pas un argument obligatoire
        self.directed = directed
        self.cities: Dict[str, City] = cities if cities is not None else {}

    def add_city(self, name: str) -> None:
        if name not in self.cities:
            self.cities[name] = City(name, set())

    def has_city(self, name: str) -> bool:
        return name in self.cities

    def remove_city(self, name: str) -> None:
        if name in self.cities:
            for city in self.cities.values():
                city.remove_neighbor(name)
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
        if name not in self.cities:
            ValueError(f"City '{name}' not found")
        return self.cities[name].neighbors


    def get_cities(self) -> Dict[str, City]:
        return dict(self.cities)

    def __repr__(self) -> str:
        return f"Graph(directed={self.directed}, cities={self.cities})"

