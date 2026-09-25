# Q4. Write a program to find the shortest path between two nodes in an unweighted graph using
# BFS.

from collections import deque
def shortest_path(graph, start, end):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None
graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"]}
print(shortest_path(graph, "A", "E"))