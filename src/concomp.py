from collections import deque

def concomp0(graph):
    def dfs(node):
        for n in graph.edges[node]:
            if cc[n] is not None: continue

            cc[n] = i
            dfs(n)

    cc, i = {node : None for node in graph.edges}, 0

    for n in graph.edges:
        if cc[n] is not None: continue

        cc[n] = i
        dfs(n)

        i += 1

    return cc


def concomp1(graph):
    cc, i = {node : None for node in graph.edges}, 0
    nodes = deque(maxlen=len(graph.edges))

    for node in graph.edges:
        if cc[node] is not None: continue

        nodes.append(node)

        while nodes:
            node = nodes.popleft()

            cc[node] = i
            nodes.extend(
                [n for n in graph.edges[node] if cc[n] is None]
            )

        i += 1

    return cc

concomps = [concomp0, concomp1]
