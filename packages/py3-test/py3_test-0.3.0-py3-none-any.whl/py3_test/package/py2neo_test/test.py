from py2neo import Graph

test_graph = Graph(
    "http://10.9.30.47:7474/db/data/", username="neo4j", password="train"
)

print(test_graph.node_labels)
