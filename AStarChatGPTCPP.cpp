#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <limits>
#include <algorithm>

using namespace std;

typedef pair<int, string> pi;

// Classe pour représenter un graphe
class Graph {
    map<string, map<string, int>> adj; // graphe
    map<string, int> heuristics; // heuristiques

public:
    // Ajouter un chemin
    void addEdge(string start, string end, int cost) {
        adj[start][end] = cost;
    }

    // Définir les heuristiques
    void setHeuristics(map<string, int> h) {
        heuristics = h;
    }

    // Implémentation de l'algorithme A*
    vector<string> aStarAlgorithm(string start, string goal) {
        // Priority queue pour stocker le front de propagation
        priority_queue<pi, vector<pi>, greater<pi>> frontier;

        // Map pour garder une trace des coûts actuels jusqu'à chaque nœud
        map<string, int> cost_so_far;
        // Map pour reconstruire le chemin
        map<string, string> came_from;

        // Initialisation
        frontier.emplace(0, start);
        cost_so_far[start] = 0;
        came_from[start] = "";

        while (!frontier.empty()) {
            string current = frontier.top().second;
            frontier.pop();

            // Si le but est atteint
            if (current == goal) break;

            // Parcourir les voisins du nœud actuel
            for (auto& next : adj[current]) {
                int new_cost = cost_so_far[current] + next.second;
                if (!cost_so_far.count(next.first) || new_cost < cost_so_far[next.first]) {
                    cost_so_far[next.first] = new_cost;
                    int priority = new_cost + heuristics[next.first];
                    frontier.emplace(priority, next.first);
                    came_from[next.first] = current;
                }
            }
        }

        // Reconstruire le chemin
        vector<string> path;
        for (string at = goal; at != ""; at = came_from[at]) {
            path.push_back(at);
        }
        reverse(path.begin(), path.end());
        return path;
    }
};

int main() {
    // Création du graphe
    Graph g;
    g.addEdge("A", "B", 2);
    g.addEdge("A", "C", 10);
    g.addEdge("A", "D", 3);
    g.addEdge("B", "A", 2);
    g.addEdge("B", "E", 10);
    g.addEdge("C", "D", 2);
    g.addEdge("C", "G", 2);
    g.addEdge("C", "A", 10);
    g.addEdge("D", "A", 3);
    g.addEdge("D", "C", 2);
    g.addEdge("D", "F", 4);
    g.addEdge("E", "B", 8);
    g.addEdge("E", "H", 10);
    g.addEdge("E", "F", 5);
    g.addEdge("F", "E", 5);
    g.addEdge("F", "D", 4);
    g.addEdge("F", "G", 5);
    g.addEdge("G", "F", 5);
    g.addEdge("G", "H", 1);
    g.addEdge("G", "C", 2);
    g.addEdge("H", "E", 10);
    g.addEdge("H", "G", 1);
    
    // Définir les heuristiques
    map<string, int> heuristics = {{"A", 9}, {"B", 3}, {"C", 5}, {"D", 6}, {"E", 8}, {"F", 4}, {"G", 2}, {"H", 0}};
    g.setHeuristics(heuristics);

    // Trouver le chemin de A à H
    vector<string> path = g.aStarAlgorithm("A", "H");
    for (const string& node : path) {
        cout << node << " ";
    }
    return 0;
}