class Node {
	constructor(name,parent = null) {
    	this.name = name;
    	this.parent = parent;
    	this.g = 0;
    	this.h = 0;
    	this.f = 0;
	}
}

function astar(graph, heuristics, start, end) {
	let open_list = [];
	let closed_set = new Set();

	let start_node = new Node(start);
	let end_node = new Node(end);

	open_list.push(start_node);

	while(open_list.length > 0) { // Tant que la liste ouverte n'est pas vide n'est pas vide
    	// On trie la liste ouverte pour obtenir le noeud avec le plus petit f
    	open_list.sort((a,b) => a.f - b.f);
    	let current_node = open_list.pop(0);
    	closed_set.add(current_node.name);

    	if(current_node.name == end_node.name) {
        	let path = []
        	while(current_node != null) {
            	path.push(current_node.name);
            	current_node = current_node.parent;
        	}
        	path.reverse(); // On inverse le chemin trouvé
        	return path;
    	}

    	let neighbors = graph[current_node.name];
    	for(let key in neighbors) {
        	if (neighbors.hasOwnProperty(key)) {
            	if (closed_set.has(key)) {
                	continue;
            	}
        	}
        	let neighbor = new Node(key,current_node);
        	neighbor.g = current_node.g + neighbors[key];
        	neighbor.h = heuristics[key];
        	neighbor.f = neighbor.g + neighbor.h;

        	// On vérifie si le voisin est dans la liste ouverte et s'il a un meilleur g
        	let found_in_open_list = false;
        	for(let open_node in open_list) {
            	if(neighbor.name == open_node.name && neighbor.g >= open_node.g) {
                	found_in_open_list = true;
                	break;
            	}
            	if(!found_in_open_list) {
                	open_list.push(neighbor);
            	}
        	}
    	}
	}
	return null; // Si aucun chemin n'est possible
}

// Exemple d'utilisation avec le graphe d'Arthur
let graph = {
	'A': {'B': 2, 'C': 10, 'D': 3},
	'B': {'A': 2, 'E': 10},
	'C': {'A': 10, 'D': 2, 'G': 2},
	'D': {'A': 3, 'C': 2, 'F': 4},
	'E': {'B': 10, 'F': 5, 'H': 10},
	'F': {'E': 5, 'G': 5, 'D': 4},
	'G': {'F': 5, 'H': 1, 'C': 2},
	'H': {'E': 10, 'G': 1}
}

let heuristics = {
	'A': 9,
	'B': 3,
	'C': 5,
	'D': 6,
	'E': 8,
	'F': 4,
	'G': 2,
	'H': 0
}

let start = 'A'
let end = 'H'
let path = astar(graph, heuristics, start, end)
console.log("Chemin obtenu : ",path);
