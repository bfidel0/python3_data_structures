
# Graph class for adjacency list
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        # just formats Adj list better
        "\n".join(["{}: {}".format(n, neighbors)
                  for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)

    discovered[root] = True

    queue.append(root)
    distance[root] = 0
    idx = 0

    while idx < len(queue):
        current = queue[idx]
        idx += 1
        # Check edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)
    return queue, distance, parent


def dfs(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []

    stack.append(root)

    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)

    return result


# Weighted and directed graph
class Graph_2:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self) -> str:
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, (nodes, weights) in enumerate(self.data):
                result += "{}: {}".format(i, nodes)
        return result


# Shortest Path weighted algo. If no weights then BFS should work
def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)

    # set nodes to infinity
    distance = [float('inf')] * len(graph.data)
    queue = []

    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1
        # Update distances of neighbors
        update_distance(graph, current, distance, parent)
        # fidn the first unvistsed ndoe with the smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)
        visited[current] = True
    return distance[target], parent


def update_distance(graph, current, distance, parent=None):
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current


def pick_next_node(distance, visited):
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node
