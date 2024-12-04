import matplotlib.pyplot as plt
from time import time

from primcode import Graph
from kruskalcode import kruskal_mst
from sample import graphs

def get_data():
    vertices = [1000, 1000, 
                10000, 10000]
    prim_time, kruskal_time = [], []
    
    for  i, graph in enumerate(graphs):
         
        #prim
        start_prim = time()
        prim_compute(graph, vertices[i])
        end_prim = time()
        prim_time.append(end_prim - start_prim)
        
        print(f"{i + 1} Prim: { end_prim - start_prim}")

        #kruskal
        start_kruskal = time()
        kruskal_compute(graph, vertices[i])
        end_kruskal= time()
        print(f"{i + 1} Kruskal: { end_kruskal - start_kruskal}")
    
        kruskal_time.append(end_kruskal - start_kruskal)

    return prim_time, kruskal_time
        
    
def prim_compute(edges, vertices):

    g = Graph(vertices)
    for u, v, w in edges:
        g.add_edge(u, v, w)    
    g.MST_PRIM(0)

def kruskal_compute(edges, vertices):
    kruskal_mst(edges, vertices)
    
    
def plot_data(vertices, kruskal, prim):
  
    plt.plot(vertices, kruskal, label = 'Kruskal')
    plt.plot(vertices, prim, label = 'Prim')
    plt.xlabel('# Vertices & Edges')
    plt.ylabel('Time (s)')
    plt.title('Compare Time complexity')
    plt.xticks(rotation=90)  # Rotate x-axis labels for readability
    plt.tight_layout()
    plt.legend()
    plt.show()


def main():
    x =  ["1000V 2000E", "1000V 499500E", 
     "10000V 15000E", "10000V ~49995000E"]

    prim, kruskal = get_data()
    plot_data(x, kruskal, prim)
    
main()