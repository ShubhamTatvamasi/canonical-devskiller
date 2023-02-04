from typing import List

def solve(input: str) -> List[int]:
    lines = input.strip().split("\n")
    n, m = map(int, lines[0].strip().split())
    graph = {i: [] for i in range(1, n+1)}
    for line in lines[1:]:
        a, b = map(int, line.strip().split())
        graph[a].append(b)
        graph[b].append(a)

    colors = {}
    for node in range(1, n+1):
        if node not in colors:
            colors[node] = 0
            stack = [node]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in colors:
                        colors[neighbor] = 1 - colors[node]
                        stack.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return []
    return [node for node, color in colors.items() if color == 0]
