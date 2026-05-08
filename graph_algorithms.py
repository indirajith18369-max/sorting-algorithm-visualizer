from heapq import heappush, heappop

# BFS — O(V+E) time, O(V) space
def bfs(graph, start):
    visited, queue = set(), [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb); queue.append(nb)

# DFS — O(V+E) time, O(V) space
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for nb in graph[node]: stack.append(nb)

# Dijkstra — O((V+E) log V) time, O(V) space
def dijkstra(graph, start):
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, u = heappop(heap)
        if d > dist.get(u, float('inf')): continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd; heappush(heap, (nd, v))
    return dist
