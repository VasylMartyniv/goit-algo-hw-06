import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

stops = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(stops)

roads = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E"), ("D", "F"), ("E", "F")]
G.add_edges_from(roads)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=12, font_color='black',
        font_weight='bold')
plt.title("Транспортна мережа міста")
plt.show()


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


start_node = "A"
end_node = "F"

dfs_result = list(dfs_paths(G, start_node, end_node))
bfs_result = list(bfs_paths(G, start_node, end_node))

print("Шляхи, знайдені за допомогою DFS:")
for path in dfs_result:
    print(" -> ".join(path))

print("\nШляхи, знайдені за допомогою BFS:")
for path in bfs_result:
    print(" -> ".join(path))

dfs_first_path = dfs_result[0] if dfs_result else []
bfs_first_path = bfs_result[0] if bfs_result else []

print("\nПерший шлях, знайдений за допомогою DFS:", " -> ".join(dfs_first_path))
print("Перший шлях, знайдений за допомогою BFS:", " -> ".join(bfs_first_path))
