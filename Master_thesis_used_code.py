import Master_thesis_code_functions as MT
import math
import sympy
import numpy as np
import itertools
from matplotlib import pyplot as plt
import matplotlib
import networkx as nx
from matplotlib.patches import ConnectionPatch
import matplotlib.patches as mpatches
import gudhi
from scipy.spatial.distance import cdist
from ripser import ripser
from persim import plot_diagrams
import random


do_circle = False

if do_circle:
    for i in range(1):
        r = 5
        n = 10
        epsilon = 0.1
        circlePoints = [
            (r * math.cos(theta), r * math.sin(theta))
            for theta in (math.pi * 2 * i / n for i in range(n))]
        # circlePoints = [
        #    (r * math.cos(theta) + random.uniform(-epsilon, epsilon), r * math.sin(theta) + random.uniform(-epsilon, epsilon))
        #    for theta in (math.pi*2 * i/n for i in range(n))]
        dm = cdist(circlePoints, circlePoints)
        MT.point_cloud_to_graph(dm, max_filtration=12.0, max_noise=0.1, return_homology=False, decomp_type='elementary', graph_type='overlap')
        # MT.point_cloud_to_graph(dm, max_filtration=12.0, max_noise=0.2)
        # X = np.array(circlePoints)
        # dgms = ripser(X, maxdim=5)['dgms']
        # fig = plt.figure(figsize=(6, 6))
        # plot_diagrams(dgms, show=True)


# points=[[1, 1], [7, 0], [4, 6], [9, 6], [0, 14], [2, 19], [9, 17]]
# dm = cdist(points, points)
# MT.point_cloud_to_graph(dm)
# print(MT.point_cloud_to_graph(dm, return_homology=True))


# cpx000 = []
cpx00 = [[1, 1, 1, 1]]
cpx01 = [[1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1]]
cpx02 = [[0, 1, 0, 1], [1, 0, 1, 0]]

fwd_2 = [cpx00, cpx01, cpx02]

# MT.fill_simplextree(MT.create_tree_3(fwd_2, return_graph=True, decomp_type='elementary'))
# print(MT.fill_simplextree(MT.create_tree_3(fwd_2, return_graph=True, decomp_type='elementary'), return_homology=True))

# MT.get_persistence_of_tree(fwd_2)
# MT.create_tree_3(fwd_2, label=False, directed=True, all_ideals=True, decomp_type='elementary', return_graph=False)
# st = MT.turn_graph_to_simplextree(MT.create_tree_3(fwd_2, label=False, directed=True, all_ideals=True, decomp_type='elementary', return_graph=True))
# st.compute_persistence(persistence_dim_max=1)
# print(st.betti_numbers())


ideal21 = [[3, 7], [5, 4]]         # blue
ideal22 = [[1, 6], [2, 5], [4, 2]]   # orange
ideal23 = [[0, 4], [3, 1]]         # green
new_ideals = [ideal23, ideal22, ideal21]

my_cm = matplotlib.colors.ListedColormap(['tab:blue', 'tab:orange', 'indigo'])

MT.create_tree_3(new_ideals, label=False, directed=True, all_ideals=True, decomp_type='elementary', color_scheme=my_cm)
