class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

def astar(graph, heuristics, start, end):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    end_node = Node(end)
    
    open_list.append(start_node)

    while open_list: # Tant que la liste ouverte n'est pas vide n'est pas vide
        # On trie la liste ouverte pour obtenir le noeud avec le plus petit f
        open_list.sort(key=lambda node: node.f)
        current_node = open_list.pop(0)  # On prend le premier noeud (le plus petit f)
        closed_set.add(current_node.name)

        if current_node.name == end_node.name:
            path = []
            while current_node is not None:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # On inverse le chemin

        neighbors = graph[current_node.name]
        for key, value in neighbors.items():
            if key in closed_set:
                continue
            neighbor = Node(key, current_node)
            neighbor.g = current_node.g + value
            neighbor.h = heuristics[key]
            neighbor.f = neighbor.g + neighbor.h

            # On vérifie si le voisin est dans la liste ouverte et s'il a un meilleur g
            found_in_open_list = False
            for open_node in open_list:
                if neighbor.name == open_node.name and neighbor.g >= open_node.g:
                    found_in_open_list = True
                    break
            if not found_in_open_list:
                open_list.append(neighbor)

    return None # Si aucun chemin n'est possible

# Exemple d'utilisation avec le graphe d'Arthur
graph = {
    'A': {'B': 2, 'C': 10, 'D': 3},
    'B': {'A': 2, 'E': 10},
    'C': {'A': 10, 'D': 2, 'G': 2},
    'D': {'A': 3, 'C': 2, 'F': 4},
    'E': {'B': 10, 'F': 5, 'H': 10},
    'F': {'E': 5, 'G': 5, 'D': 4},
    'G': {'F': 5, 'H': 1, 'C': 2},
    'H': {'E': 10, 'G': 1}
}

heuristics = {
    'A': 9,
    'B': 3,
    'C': 5,
    'D': 6,
    'E': 8,
    'F': 4,
    'G': 2,
    'H': 0
}

start = 'A'
end = 'H'
path = astar(graph, heuristics, start, end)
print(path)