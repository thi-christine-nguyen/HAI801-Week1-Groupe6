import matplotlib.pyplot as plt

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

    while open_list:
        open_list.sort(key=lambda node: node.f)
        current_node = open_list.pop(0)
        closed_set.add(current_node.name)

        if current_node.name == end_node.name:
            path = []
            while current_node is not None:
                path.append(current_node.name)
                current_node = current_node.parent
            draw_a_star_step(graph, heuristics, start, end, open_list, closed_set, current_node, path)
            return path[::-1]

        neighbors = graph[current_node.name]
        for key, value in neighbors.items():
            if key in closed_set:
                continue
            neighbor = Node(key, current_node)
            neighbor.g = current_node.g + value
            neighbor.h = heuristics[key]
            neighbor.f = neighbor.g + neighbor.h

            found_in_open_list = False
            for open_node in open_list:
                if neighbor.name == open_node.name and neighbor.g >= open_node.g:
                    found_in_open_list = True
                    break
            if not found_in_open_list:
                open_list.append(neighbor)

        draw_a_star_step(graph, heuristics, start, end, open_list, closed_set, current_node)

    draw_a_star_step(graph, heuristics, start, end, open_list, closed_set, None)
    return None

def draw_a_star_step(graph, heuristics, start, end, open_list, closed_set, current_node, final_path=None):

    # Ajuster les positions des nœuds (si nécessaire)
    node_positions = {
        'A': (0, 0), 
        'B': (-1, -1), 
        'C': (1, -1),
        'D': (2, -1),
        'E': (-2, -2), 
        'F': (0, -2),
        'G': (1, -3), 
        'H': (-1, -3)
    }

    # Dessiner les arêtes
    edges = [(node, neighbor, weight) for node, neighbors in graph.items() for neighbor, weight in neighbors.items()]
    for edge in edges:
        color = 'black'
        if current_node and (edge[0] == current_node.name or edge[1] == current_node.name):
            color = 'orange'
        elif edge[0] in closed_set and edge[1] in closed_set:
            color = 'gray'

        plt.plot([node_positions[edge[0]][0], node_positions[edge[1]][0]],
                 [node_positions[edge[0]][1], node_positions[edge[1]][1]], marker='o', markersize=8, color=color, lw=2)
        plt.text((node_positions[edge[0]][0] + node_positions[edge[1]][0]) / 2,
                 (node_positions[edge[0]][1] + node_positions[edge[1]][1]) / 2 + 0.1,
                 str(edge[2]), ha='center', va='center', color='red', fontsize=10)

    # Dessiner les noeuds
    for node, (x, y) in node_positions.items():
        plt.text(x, y - 0.2, node, ha='center', va='center', fontweight='bold', fontsize=12, color='blue')

    # Mettre en évidence le chemin final
    if final_path:
        for i in range(len(final_path) - 1):
            plt.plot([node_positions[final_path[i]][0], node_positions[final_path[i + 1]][0]],
                     [node_positions[final_path[i]][1], node_positions[final_path[i + 1]][1]], marker='o', markersize=8, color='blue', lw=2)

    # Titre du graphe
    if current_node:
        plt.title(f"A* Algorithm - Current Node: {current_node.name}", fontsize=14)
    else:
        plt.title("A* Algorithm - Path Found", fontsize=14)

    plt.axis('off')
    plt.show()

# Modifier le graphe et les heuristiques pour utiliser des lettres
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
print("Chemin trouvé :", path)