import networkx as nx

filename = "day6_data.txt"
data = []
with open(filename) as file:
    for line in file.readlines():
        data.append(line.strip().split(')'))

galaxy = nx.DiGraph()
galaxy.add_edges_from(data)
orb_checksum = sum([len(nx.ancestors(galaxy, planet)) for planet in galaxy.nodes()])
you_san = nx.shortest_path_length(galaxy.to_undirected(), "SAN", "YOU")-2
print("Task 1: %d" % orb_checksum)
print("Task 2: %d" % you_san)