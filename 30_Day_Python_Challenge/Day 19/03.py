# Q3. Write a program to detect a cycle in a directed graph using DFS.

def has_cycle(graph):
    visited = set()
    rec_stack = set()
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
print(has_cycle(graph))