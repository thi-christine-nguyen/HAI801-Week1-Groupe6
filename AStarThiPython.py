
from collections import deque

class Graph:
  
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        H = {
            'A': 9,
            'B': 3,
            'C': 5,
            'D': 6, 
            'E': 8, 
            'F': 4, 
            'G': 2, 
            'H': 0,
        }

        return H[n]

    def aStar(self, start, end):

        open_list = set([start])
        closed_list = set([])

        g = {}

        g[start] = 0
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None 


adjacency_list = {
    'A': [('B', 2), ('D',3), ('C' , 10)],
    'B': [('A', 2), ('E', 8)],
    'C': [('A', 10), ('D', 6), ('G',2)], 
    'D': [('A', 3), ('C', 2), ('F' , 4)], 
    'E': [('B', 8), ('H', 10), ('F' , 5)], 
    'F': [('E', 5), ('D', 4), ('G' , 5)], 
    'G': [('F', 5), ('H', 1), ('C' , 2)], 
    'H': [('E', 10), ('G', 1)]

}
graph1 = Graph(adjacency_list)
graph1.aStar('A', 'H')