from collections import deque


def concomp0(graph):
    """
    Performs depth-first search to find connected components of a given graph

    Args:
        graph: an undirected graph (a forest of connected components).

    Returns:
        a dictionary {node: integer} where the integer is the same for
        those nodes which belong to the same connected component.
    """

    def dfs(node):
        cc[node] = i

        for n in graph[node]:
            if cc[n] is not None:
                continue

            dfs(n)

    cc = {node: None for node in graph}

    for i, n in enumerate(graph):
        if cc[n] is not None:
            continue

        dfs(n)

    return cc


def concomp1(graph):
    """
    Performs breadth-first search to find connected components of a given graph

    Args:
        graph: an undirected graph (a forest of connected components).

    Returns:
        a dictionary {node: integer} where the integer is the same for
        those nodes which belong to the same connected component.
    """

    cc, i = {node: None for node in graph}, 0

    nodes = deque(maxlen=len(graph))

    for node in graph:
        if cc[node] is not None:
            continue

        nodes.append(node)

        while nodes:
            src = nodes.popleft()

            cc[src] = i

            nodes.extend([dst for dst in graph[src] if cc[dst] is None])

        i += 1

    return cc


def concomp2(graph):
    """
    Find connected components in undirected graphs breadth-first.

    Args:
        graph: an undirected graph (a forest of connected components).

    Returns:
        a dictionary {node: integer} where the integer is the same for
        those nodes whose connected component is the same.
    """
    cc = {node: None for node in graph}

    for i, node in enumerate(graph):
        if cc[node] is not None:
            continue

        nodes = [node]

        while nodes:
            src = nodes.pop()

            cc[src] = i

            nodes.extend([dst for dst in graph[src] if cc[dst] is None])

    return cc
