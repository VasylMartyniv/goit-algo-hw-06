import heapq

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

stops = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(stops)

roads = [
    ("A", "B", 1),
    ("A", "C", 2),
    ("B", "D", 1),
    ("C", "D", 1),
    ("C", "E", 2),
    ("D", "E", 1),
    ("D", "F", 2),
    ("E", "F", 1)
]
G.add_weighted_edges_from(roads)

pos = nx.spring_layout(G)
edges = G.edges(data=True)
edge_labels = {(u, v): d['weight'] for u, v, d in edges}
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=12, font_color='black',
        font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Транспортна мережа міста з вагами ребер")
plt.show()


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


shortest_paths = {}
for node in G.nodes():
    shortest_paths[node] = dijkstra(G, node)

for start_node, distances in shortest_paths.items():
    print(f"Найкоротші шляхи від вершини {start_node}:")
    for end_node, distance in distances.items():
        print(f"  до вершини {end_node}: {distance}")
