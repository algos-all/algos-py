from collections import deque


def concomp0(graph):
    def dfs(node):
        cc[node] = i

        for n in graph[node]:
            if cc[n] is not None: continue

            dfs(n)

    cc = {node: None for node in graph}

    for i, n in enumerate(graph):
        if cc[n] is not None: continue

        dfs(n)

    return cc


def concomp1(graph):
    cc, i = {node: None for node in graph}, 0

    nodes = deque(maxlen=len(graph))

    for node in graph:
        if cc[node] is not None: continue

        nodes.append(node)

        while nodes:
            node = nodes.popleft()

            cc[node] = i
            nodes.extend([n for n in graph[node] if cc[n] is None])

        i += 1

    return cc


def concomp2(graph):
    cc = {node: None for node in graph}

    for i, node in enumerate(graph):
        if cc[node] is not None: continue

        nodes = [node]

        while nodes:
            node = nodes.pop()

            cc[node] = i

            nodes.extend([n for n in graph[node] if cc[n] is None])

    return cc
