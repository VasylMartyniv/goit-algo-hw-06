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

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")
