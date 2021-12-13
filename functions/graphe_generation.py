import networkx as nx
import numpy as np
import pandas as pd
from fastdist import fastdist

def weight(depart, arrivee, df_nodes):
    """get weight between 2 nodes with their number"""
    return fastdist.euclidean(np.array(df_nodes.iloc[depart][['x','y']].to_list()), np.array(df_nodes.iloc[arrivee][['x','y']].to_list()))

def random_simple_graph(nb_nodes, radius):
    """Random Graph Generation"""
    G = nx.random_geometric_graph(n=nb_nodes, radius=radius)
    # for nodes :
    n = [i for i in range(nb_nodes)]
    x, y = [], []
    for i in range(nb_nodes):
        x.append(round(nx.get_node_attributes(G, "pos")[i][0]*100, 2))
        y.append(round(nx.get_node_attributes(G, "pos")[i][1]*100, 3))
    random_node_2D = pd.DataFrame(list(zip(n, x, y)), columns=['n', 'x', 'y'])
    # for edges :
    depart, arrivee, poids = [], [], []
    for edges in G.edges:
        depart.append(edges[0])
        arrivee.append(edges[1])
        poids.append(round(weight(depart=edges[0], arrivee=edges[1], df_nodes=random_node_2D), 3))
    random_edges_2D = pd.DataFrame(list(zip(depart, arrivee, poids)), columns=['depart', 'arrivee', 'poids'])

    return random_node_2D, random_edges_2D

def set_weights(edges, nodes):
    """set weights from nodes and edges dataframe"""
    poids = []
    for i in range(len(edges)):
        poids.append(round(weight(depart=int(edges.iloc[i]['depart']), arrivee=int(edges.iloc[i]['arrivee']), df_nodes=nodes), 3))
    edges["poids"]=pd.Series(poids)
    return edges, nodes