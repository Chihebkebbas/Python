# Demo CLI — utilisation rapide
    
### Créer un graphe non orienté

    python -m src.cli create --directed False
### Ajouter des villes
    python -m src.cli add-city --name A
    python -m src.cli add-city --name B
    python -m src.cli add-city --name C
### Ajouter des routes
    python -m src.cli add-road --from A --to B
    python -m src.cli add-road --from B --to C
### Afficher voisins
    python -m src.cli show-neighbors --name A
         => Neighbors of A: ['B']
### Lancer DFS (itératif) pour obtenir un chemin
    python -m src.cli dfs --start A --target C
        => DFS path: ['A','B','C']
### Lancer BFS pour obtenir le plus court chemin
    python -m src.cli bfs --start A --target C
        => BFS path: ['A','B','C']
    

    
## Commandes pour tester / démo

        pytest -q
### Utiliser le CLI (exemples) :
        python -m src.cli create --directed False
        python -m src.cli add-city --name A
        python -m src.cli add-city --name B
        python -m src.cli add-road --from A --to B
        python -m src.cli show-neighbors --name A
        python -m src.cli bfs --start A --target B