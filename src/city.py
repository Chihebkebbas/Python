from typing import Set

class City:
     def __init__(self, name: str, neighbors: Set[str] = None):
         self.name = name
         self.neighbors: Set[str] = neighbors if neighbors is not None else set()

     def __repr__(self) -> str:
         return f"City name: {self.name}, neighbors: {self.neighbors}"

     def add_neighbor(self, neighbor: str):
         self.neighbors.add(neighbor)

     def remove_neighbor(self, neighbor: str):
         self.neighbors.discard(neighbor) # discard est une variante de remove, elle supprime juste si l'élément existe sinon elle fait rien

     def get_neighbors(self) -> Set[str]:
         return set(self.neighbors) # Renvoier une copie

     