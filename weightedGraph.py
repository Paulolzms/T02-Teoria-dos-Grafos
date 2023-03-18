class WeightedGraph:
    def __init__(self, node_count: int = 0, edge_count: int = 0, adj_list: list[list[tuple[int, int]]] = []) -> None:
        self.node_count = node_count
        self.edge_count = edge_count
        self.adj_list = adj_list
        if adj_list == []:
            for _ in range(self.node_count):
                self.adj_list.append([])

    def add_directed_edge(self, u: int, v: int, w: int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node_count - 1})")
        self.adj_list[u].append((v, w))
        self.edge_count += 1

    def add_undirected_edge(self, u: int, v: int, w: int):
        self.add_directed_edge(u, v, w)
        self.add_directed_edge(v, u, w)

    def max_dist_Q(self, Q, dist):
        max_dist = float("-inf")
        max_node = -1
        for node in Q:
            if dist[node] > max_dist:
                max_dist = dist[node]
                max_node = node
        return max_node

    def dijkstra(self, s):
        dist = [float("-inf")] * self.node_count
        pred = [-1] * self.node_count
        dist[s] = 0
        Q = [i for i in range(self.node_count)]
        while Q != []:
            u = self.max_dist_Q(Q, dist)
            Q.remove(u)
            for (v, w) in self.adj_list[u]:
                if dist[v] < dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
        return (dist, pred)