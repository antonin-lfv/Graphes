#  ____    _____
# |___ \  |  __ \
#   __) | | |  | |
#  |__ <  | |  | |
#  ___) | | |__| |
# |____/  |_____/

# Dans aretes_3D.csv : (graphe non orienté)
# depart -> noeud d'origine
# arrivee -> noeud d'arrivée

# Dans noeuds.csv :
# n -> numéro du noeud
# x,y,z -> coordonnées du noeud


import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd


def graphe_3d(nodes, edges):
    """Plot graph"""
    edge_x_temp, edge_y_temp, edge_z_temp = [], [], []
    edge_x, edge_y, edge_z = [], [], []
    for row in range(len(edges)):
        edge_x_temp.append(int(nodes[nodes['n'] == int(edges.loc[row][['depart']])]['x']))
        edge_x_temp.append(int(nodes[nodes['n'] == int(edges.loc[row][['arrivee']])]['x']))
        edge_y_temp.append(int(nodes[nodes['n'] == int(edges.loc[row][['depart']])]['y']))
        edge_y_temp.append(int(nodes[nodes['n'] == int(edges.loc[row][['arrivee']])]['y']))
        edge_z_temp.append(int(nodes[nodes['n'] == int(edges.loc[row][['depart']])]['z']))
        edge_z_temp.append(int(nodes[nodes['n'] == int(edges.loc[row][['arrivee']])]['z']))

    for i in range(len(edge_x_temp)):
        if i == 0:
            edge_x.append(edge_x_temp[i])
            edge_y.append(edge_y_temp[i])
            edge_z.append(edge_z_temp[i])
        elif i % 2 == 0:
            edge_x.append(None)
            edge_y.append(None)
            edge_z.append(None)
            edge_x.append(edge_x_temp[i])
            edge_y.append(edge_y_temp[i])
            edge_z.append(edge_z_temp[i])
        else:
            edge_x.append(edge_x_temp[i])
            edge_y.append(edge_y_temp[i])
            edge_z.append(edge_z_temp[i])

    edge_trace = go.Scatter3d(
        x=edge_x, y=edge_y, z=edge_z,
        line=dict(width=2, color='#000000'),
        hoverinfo='none',
        mode='lines')

    # traçage des noeuds ####

    node_x, node_y, node_z = nodes['x'].to_list(), nodes['y'].to_list(), nodes['z'].to_list()

    node_trace = go.Scatter3d(
        x=node_x, y=node_y, z=node_z,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            color='blue',
            size=8,
            line_width=1.5))

    # affichage
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                    )
                    )
    return fig
