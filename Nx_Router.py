# Enter your Python code here
# -*- coding: utf-8 -*-
#Created on Thu Mar 27 00:24:41 2021
#Tracy Groller for Klayout Routing
#Basic Implmentation of  Shortest Path Routing
#Using the networkx package
#NetworkX is a Python package for the creation, manipulation,
#and study of the structure, dynamics, and functions of complex networks.

from warnings import warn
import heapq
import networkx as nx
import time
import multiprocessing
# Enter your Python code here
#Nxgraph Shortest Path
def nxRoute(matrix,loc1,loc2):
  #starttime = time.time()
  rows = len(matrix)
  cols = len(matrix[0])
  starttime = time.time()
  start = (loc1[0], loc1[1])
  end = (loc2[0], loc2[1])
  G = nx.grid_2d_graph(rows,cols)
  pos = {(x,y):(y,-x) for x,y in G.nodes()}
  crds =  nx.bidirectional_shortest_path(G, source=start, target=end)
  #crds = astar_path(G, source=start, target=end)
  #print('That took {} seconds'.format(time.time() - starttime))
  #print(crds)
  #print("Stop")
  return crds
