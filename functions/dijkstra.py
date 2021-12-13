from queue import PriorityQueue
import pandas as pd


def dijkstra(G, start, goal):
    """ Uniform-cost search / dijkstra """
    visited = set()
    cost = {start: 0}
    parent = {start: None}
    todo = PriorityQueue()

    todo.put((0, start))
    while todo:
        while not todo.empty():
            _, vertex = todo.get()  # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited:
                break
        else:  # if todo ran out
            break  # quit main loop
        visited.add(vertex)
        if vertex == goal:
            break
        if vertex in G.keys():
            for neighbor, distance in G[vertex]:
                if neighbor in visited:
                    continue  # skip these to save time
                old_cost = cost.get(neighbor, float('inf'))  # default to infinity
                new_cost = cost[vertex] + distance
                if new_cost < old_cost:
                    todo.put((new_cost, neighbor))
                    cost[neighbor] = new_cost
                    parent[neighbor] = vertex
    return parent


def make_path(parent, goal):
    if goal not in parent:
        return None
    v = goal
    path = []
    while v is not None:  # root has null parent
        path.append(v)
        v = parent[v]
    return path[::-1]


def graphe(edges):
    """Create adjacency list"""
    G = {}
    for index, row in edges.iterrows():
        # print(row['depart'], row['arrivee'])
        if row['depart'] not in G.keys():
            G[int(row['depart'])] = {(int(row['arrivee']), row['poids'])}
        else:
            G[int(row['depart'])].add((int(row['arrivee']), row['poids']))
    return G
