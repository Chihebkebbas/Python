from typing import Set

class City:
     def __init__(self, name: str, neighbors: Set[str]):
         self.name = name
         self.neighbor: Set[str] = neighbors

     def __repr__(self) -> str:
         return f"City name: {self.name}, neighbors: {self.neighbor}"

     def add_neighbor(self, neighbor: str):
         self.neighbor.add(neighbor)

     def remove_neighbor(self, neighbor: str):
         self.neighbor.remove(neighbor)

     def get_neighbors(self) -> Set[str]:
         return self.neighbor

     