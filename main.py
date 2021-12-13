from functions.graphe_3D import *
from functions.graphe_2D import *
from functions.graphe_generation import *
from functions.dijkstra import *

from plotly.offline import plot
import pandas as pd
import networkx as nx

import streamlit as st

####### html/css config ########
st.set_page_config(layout="wide")
st.markdown("""
<style>
.first_titre {
    font-size:75px !important;
    font-weight: bold;
    box-sizing: border-box;
    text-align: center;
    width: 100%;
}
.intro{
    text-align: justify;
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

choix = st.sidebar.selectbox(label="Menu", options=["Accueil",
                                                    "Affichage graphe 3D depuis csv",
                                                    "Affichage graphe 2D depuis csv",
                                                    "Affichage graphe random 2D",
                                                    "Dijkstra graphe 2D depuis csv",
                                                    "Dijkstra graphe random 2D "])
st.sidebar.write("##")

if choix == "Accueil":
    st.markdown('<p class="first_titre">Graphes</p>', unsafe_allow_html=True)
    st.write("---")
    c1, c2 = st.columns((2, 2))
    with c2:
        st.write("##")
        st.write("##")
        st.image("logo/background.png")
    st.write("##")
    with c1:
        st.write("##")
        st.markdown(
            '<p class="intro">Cette application web vous permet de visualiser des graphes 2D et 3D avec plotly et networkx, '
            'et d\'appliquer l\'algorithme de Dijkstra sur ceux en 2D. '
            'Cette algorithme fait partie des Algorithmes de recherche de plus court chemin en théorie des graphes.</p>',
            unsafe_allow_html=True)
    c1, _, _, _, _, _ = st.columns(6)
    with c1:
        st.subheader("Liens")
        st.write("• [Mon profil GitHub](https://github.com/antonin-lfv)")
        st.write("• [Mon site](https://antonin-lfv.github.io)")

elif choix == "Affichage graphe 3D depuis csv":
    # Données
    node_csv_3D = pd.read_csv('data/neouds_3D.csv', sep=';')
    edge_csv_3D = pd.read_csv('data/aretes_3D.csv', sep=';')
    # Affichage
    st.write("##")
    if st.sidebar.button(label="Générer le graphe"):
        fig_3D = graphe_3d(nodes=node_csv_3D, edges=edge_csv_3D)
        st.plotly_chart(fig_3D)

elif choix == "Affichage graphe 2D depuis csv":
    # Données
    node_csv_2d = pd.read_csv('data/noeuds_2D.csv', sep=';')
    edge_csv_2d = pd.read_csv('data/aretes_2D.csv', sep=';')
    # Affichage
    st.write("##")
    if st.sidebar.button("Générer le graphe"):
        fig_2D = graphe_2d(nodes=node_csv_2d, edges=edge_csv_2d, dijkstra_path=None, titre=None)
        st.plotly_chart(fig_2D)

elif choix == "Affichage graphe random 2D":
    nb_nodes = st.sidebar.slider(label="nombre de noeuds", min_value=0, max_value=60, value=30, step=1)
    if nb_nodes < 30:
        radius = 0.45
    else:
        radius = 0.30
    st.write("##")
    if st.sidebar.button("Générer le graphe"):
    # Données
        random_node_2D, random_edges_2D = random_simple_graph(nb_nodes=nb_nodes, radius=radius)
    # Affichage
        fig_2D_random = graphe_2d(nodes=random_node_2D, edges=random_edges_2D, dijkstra_path=None,
                              titre=None)  # Random Graphe 2D
        st.plotly_chart(fig_2D_random)

elif choix == "Dijkstra graphe 2D depuis csv":
    # Données
    node_csv_2d = pd.read_csv('data/noeuds_2D.csv', sep=';')
    edge_csv_2d = pd.read_csv('data/aretes_2D.csv', sep=';')
    # Dijkstra
    dijkstra_edges, dijkstra_nodes = set_weights(edge_csv_2d, node_csv_2d)
    G = graphe(dijkstra_edges)
    sommet_depart = st.sidebar.slider(label="sommet de départ", min_value=min(G.keys()),
                                              max_value=max(G.keys()), step=1)
    sommet_arrivee = st.sidebar.slider(
        label="sommet d'arrivée", min_value=min(G.keys()), max_value=max(G.keys()), step=1)
    st.write("##")
    if st.sidebar.button("Générer le graphe"):
        dijkstra_resultat = make_path(parent=dijkstra(G=G, start=sommet_depart, goal=sommet_arrivee),
                                      goal=sommet_arrivee)
        st.sidebar.success(
            "\tChemin le plus court du sommet " + str(sommet_depart) + " jusqu'au sommet " + str(sommet_arrivee) + " : "
            + str(dijkstra_resultat))
        st.plotly_chart(
                graphe_2d(nodes=dijkstra_nodes, edges=dijkstra_edges, dijkstra_path=dijkstra_resultat, titre=""))

elif choix == "Dijkstra graphe random 2D ":
    nb_nodes = st.sidebar.slider(label="nombre de noeuds", min_value=0, max_value=60, value=30, step=1)
    if nb_nodes < 30:
        radius = 0.45
    else:
        radius = 0.30
    # Données
    random_node_2D, random_edges_2D = random_simple_graph(nb_nodes=nb_nodes, radius=radius)
    # Dijkstra
    dijkstra_edges, dijkstra_nodes = set_weights(random_edges_2D, random_node_2D)
    G = graphe(dijkstra_edges)
    sommet_depart = st.sidebar.slider(label="sommet de départ", min_value=min(G.keys()),
                                              max_value=max(G.keys()), step=1)
    sommet_arrivee = st.sidebar.slider(
        label="sommet d'arrivée", min_value=min(G.keys()), max_value=max(G.keys()), step=1)
    st.write("##")
    if st.sidebar.button("Générer le graphe"):
        dijkstra_resultat = make_path(parent=dijkstra(G=G, start=sommet_depart, goal=sommet_arrivee),
                                      goal=sommet_arrivee)
        st.sidebar.success("\tChemin le plus court du sommet " + str(sommet_depart) + " jusqu'au sommet " + str(
            sommet_arrivee) + " : " + str(dijkstra_resultat))
        st.plotly_chart(
                graphe_2d(nodes=dijkstra_nodes, edges=dijkstra_edges, dijkstra_path=dijkstra_resultat, titre=""))

