from collections import defaultdict, deque


def build_graph(attempts):
    graph = defaultdict(set)
    for attempt in attempts:
        a, b, c = attempt
        graph[a].add(b)
        graph[b].add(c)
    return graph


def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    queue = deque([u for u in in_degree if in_degree[u] == 0])
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return topo_order


def read_attempts(file_path):
    with open(file_path, 'r') as file:
        attempts = [line.strip() for line in file]
    return attempts


def find_shortest_passcode(file_path):
    attempts = read_attempts(file_path)
    graph = build_graph(attempts)
    topo_order = topological_sort(graph)
    return ''.join(topo_order)


file_path = '0079_keylog.txt'
result = find_shortest_passcode(file_path)

print(f"The shortest possible secret passcode is: {result}")
