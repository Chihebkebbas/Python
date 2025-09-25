# Mini-projet — Réseau de villes (POO, pile/file, DFS & BFS)

## Bref énoncé
Construire un petit programme Python qui modélise un réseau de villes reliées par des routes et permet de :
- représenter les villes et les connexions (**POO**),
- manipuler explicitement une **pile** et une **file**,
- implémenter **DFS** (profondeur) et **BFS** (largeur) pour savoir si une ville A est atteignable depuis B, et *(optionnel)* retourner le chemin.

---

## Objectifs pédagogiques
- Pratiquer la **programmation orientée objet** (classes, méthodes, encapsulation).
- Comprendre et implémenter les **structures de données fondamentales** : pile / file.
- Comprendre les **algorithmes de parcours de graphe (DFS, BFS)** — récursif et itératif.
- Écrire des **tests unitaires** et documenter un mini-projet pour **GitHub**.

---

## Prérequis
- **Python (3.8+)** — notions de classes, listes, dictionnaires, sets.

---

## Livrables attendus (pour le repo)
- `src/` : code source (**City, Graph, Stack, Queue, algos**).
- `tests/` : tests unitaires (**pytest** ou **unittest**).
- `examples/` : exemples de graphes et commandes d’exécution.
- `README.md` : énoncé + instructions d’installation + usage.
- `requirements.txt` (optionnel) et `.gitignore`.

---

## Arborescence suggérée
    /mon-reseau-villes
    ├── README.md
    ├── src/
    │   ├── city.py
    │   ├── graph.py
    │   ├── stack.py
    │   ├── queue.py
    │   └── searches.py   # dfs / bfs (interfaces)
    ├── tests/
    │   ├── test_graph.py
    │   └── test_searches.py
    ├── examples/
    │   └── demo_cli.md
    └── requirements.txt
