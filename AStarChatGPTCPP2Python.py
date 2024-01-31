import heapq

class Graph:
    def __init__(self):
        self.adj = {}  # Graph
        self.heuristics = {}  # Heuristics

    def add_edge(self, start, end, cost):
        if start not in self.adj:
            self.adj[start] = {}
        self.adj[start][end] = cost

    def set_heuristics(self, heuristics):
        self.heuristics = heuristics

    def a_star_algorithm(self, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))

        cost_so_far = {start: 0}
        came_from = {start: None}

        while frontier:
            current_cost, current = heapq.heappop(frontier)

            if current == goal:
                break

            for next_node in self.adj.get(current, {}):
                new_cost = cost_so_far[current] + self.adj[current][next_node]
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristics.get(next_node, 0)
                    heapq.heappush(frontier, (priority, next_node))
                    came_from[next_node] = current

        path = []
        at = goal
        while at is not None:
            path.append(at)
            at = came_from[at]
        path.reverse()
        return path

# Main
if __name__ == "__main__":
    g = Graph()

    # Ajouter des chemins
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 10)
    g.add_edge("A", "D", 3)
    g.add_edge("B", "A", 2)
    g.add_edge("B", "E", 10)
    g.add_edge("C", "D", 2)
    g.add_edge("C", "G", 2)
    g.add_edge("C", "A", 10)
    g.add_edge("D", "A", 3)
    g.add_edge("D", "C", 2)
    g.add_edge("D", "F", 4)
    g.add_edge("E", "B", 8)
    g.add_edge("E", "H", 10)
    g.add_edge("E", "F", 5)
    g.add_edge("F", "E", 5)
    g.add_edge("F", "D", 4)
    g.add_edge("F", "G", 5)
    g.add_edge("G", "F", 5)
    g.add_edge("G", "H", 1)
    g.add_edge("G", "C", 2)
    g.add_edge("H", "E", 10)
    g.add_edge("H", "G", 1)

    # Définir les heuristiques
    heuristics = {"A": 9, "B": 3, "C": 5, "D": 6, "E": 8, "F": 4, "G": 2, "H": 0}
    g.set_heuristics(heuristics)

    # Trouver le chemin de A à H
    path = g.a_star_algorithm("A", "H")
    print(" ".join(path))