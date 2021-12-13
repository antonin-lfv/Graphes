if __name__ == '__main__':
    from functions.graphe_3D import *
    from functions.graphe_2D import *
    from functions.graphe_generation import *
    from functions.dijkstra import *

    from plotly.offline import plot
    import pandas as pd
    import networkx as nx

    # pour graphe avec poids Dijkstra :
    # https://networkx.org/documentation/stable/auto_examples/drawing/plot_knuth_miles.html
    # pour des graphes réels :
    # https://networkx.org/documentation/stable/auto_examples/index.html#geospatial

    print("""
      __  __                        
     |  \/  |                       \t\t(1) ► Affichage graphe 3D depuis csv
     | \  / |   ___   _ __    _   _ \t\t(2) ► Affichage graphe 2D depuis csv
     | |\/| |  / _ \ | '_ \  | | | |\t\t(3) ► Affichage graphe random 2D
     | |  | | |  __/ | | | | | |_| |\t\t(4) ► Dijkstra graphe 2D depuis csv
     |_|  |_|  \___| |_| |_|  \__,_|\t\t(5) ► Dijkstra graphe random 2D                        
    \n""")

    choix = '0'
    while choix not in ['1', '2', '3', '4', '5']:
        choix = input("\tVotre choix : ")

    if choix == '1':
        # Données
        node_csv_3D = pd.read_csv('data/neouds_3D.csv', sep=';')
        edge_csv_3D = pd.read_csv('data/aretes_3D.csv', sep=';')
        # Affichage
        fig_3D = graphe_3d(nodes=node_csv_3D, edges=edge_csv_3D)
        plot(fig_3D)

    elif choix == '2':
        # Données
        node_csv_2d = pd.read_csv('data/noeuds_2D.csv', sep=';')
        edge_csv_2d = pd.read_csv('data/aretes_2D.csv', sep=';')
        # Affichage
        fig_2D = graphe_2d(nodes=node_csv_2d, edges=edge_csv_2d, dijkstra_path=None, titre=None)
        plot(fig_2D)

    elif choix == '3':
        # Données
        random_node_2D, random_edges_2D = random_simple_graph(nb_nodes=25, radius=0.45)
        # Affichage
        fig_2D_random = graphe_2d(nodes=random_node_2D, edges=random_edges_2D, dijkstra_path=None,
                                  titre=None)  # Random Graphe 2D
        plot(fig_2D_random)

    elif choix == '4':
        # Données
        node_csv_2d = pd.read_csv('data/noeuds_2D.csv', sep=';')
        edge_csv_2d = pd.read_csv('data/aretes_2D.csv', sep=';')
        # Dijkstra
        dijkstra_edges, dijkstra_nodes = set_weights(edge_csv_2d, node_csv_2d)
        G = graphe(dijkstra_edges)
        sommet_depart, sommet_arrivee = min(G.keys()), max(G.keys())
        dijkstra_resultat = make_path(parent=dijkstra(G=G, start=sommet_depart, goal=sommet_arrivee),
                                      goal=sommet_arrivee)
        print("\tChemin le plus court du sommet " + str(sommet_depart) + " jusqu'au sommet " + str(sommet_arrivee) + " : "
              + str(dijkstra_resultat))
        if dijkstra_resultat is None:
            titre = "Il n'y a pas de chemin reliant les sommets " + str(sommet_depart) + " et " + str(sommet_arrivee)
        else:
            titre = "Chemin le plus court du sommet " + str(sommet_depart) + " jusqu'au sommet " + str(
                sommet_arrivee) + ": " + str(dijkstra_resultat)
        plot(graphe_2d(nodes=dijkstra_nodes, edges=dijkstra_edges, dijkstra_path=dijkstra_resultat, titre=titre))

    elif choix == '5':
        # Données
        random_node_2D, random_edges_2D = random_simple_graph(nb_nodes=50, radius=0.2)
        # Dijkstra
        dijkstra_edges, dijkstra_nodes = set_weights(random_edges_2D,random_node_2D)
        G = graphe(dijkstra_edges)
        sommet_depart, sommet_arrivee = min(G.keys()), max(G.keys())-5
        dijkstra_resultat = make_path(parent=dijkstra(G=G, start=sommet_depart, goal=sommet_arrivee),
                                      goal=sommet_arrivee)
        print("\tChemin le plus court du sommet " + str(sommet_depart) + " jusqu'au sommet " + str(sommet_arrivee) + " : "
              + str(dijkstra_resultat))
        if dijkstra_resultat is None:
            titre = "Il n'y a pas de chemin reliant les sommets " + str(sommet_depart) + " et " + str(sommet_arrivee)
        else:
            titre = "Chemin le plus court du sommet " + str(sommet_depart) + " jusqu'au sommet " + str(
                sommet_arrivee) + ": " + str(dijkstra_resultat)
        plot(graphe_2d(nodes=dijkstra_nodes, edges=dijkstra_edges, dijkstra_path=dijkstra_resultat, titre=titre))


"""
    # Random graphes
    random_node_2D, random_edges_2D = random_simple_graph(nb_nodes=25, radius=0.45)

    # Données
    node_csv_3D = pd.read_csv('data/neouds_3D.csv', sep=';')
    edge_csv_3D = pd.read_csv('data/aretes_3D.csv', sep=';')
    node_csv_2d = pd.read_csv('data/noeuds_2D.csv', sep=';')
    edge_csv_2d = pd.read_csv('data/aretes_2D.csv', sep=';')

    # Affichage
    fig_3D = graphe_3d(nodes=node_csv_3D, edges=edge_csv_3D)
    # plot(fig_3D)
    fig_2D = graphe_2d(nodes=node_csv_2d, edges=edge_csv_2d, dijkstra_path=None, titre=None)  # Graphe 2D
    # plot(fig_2D)
    fig_2D_random = graphe_2d(nodes=random_node_2D, edges=random_edges_2D, dijkstra_path=None, titre=None) # Random Graphe 2D
    # plot(fig_2D_random)

    # Dijkstra
    dijkstra_edges, dijkstra_nodes = set_weights(edge_csv_2d, node_csv_2d)
    G = graphe(dijkstra_edges)
    sommet_depart, sommet_arrivee = 5, 10
    dijkstra_resultat = make_path(parent=dijkstra(G=G, start=sommet_depart, goal=sommet_arrivee), goal=sommet_arrivee)

    print("Chemin le plus court du sommet " + str(sommet_depart) + " jusqu'au sommet " + str(sommet_arrivee) + " : "
          + str(dijkstra_resultat))
    if dijkstra_resultat is None:
        titre = "Il n'y a pas de chemin reliant les sommets " + str(sommet_depart) + " et " + str(sommet_arrivee)
     else:
         titre = "Chemin le plus court du sommet " + str(sommet_depart) + " jusqu'au sommet " + str(
             sommet_arrivee) + ": " + str(dijkstra_resultat)

    plot(graphe_2d(nodes=dijkstra_nodes, edges=dijkstra_edges, dijkstra_path=dijkstra_resultat, titre=titre))
"""