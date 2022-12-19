from dataclasses import dataclass, field

from rich import print

import plotly.express as px

import networkx as nx
import matplotlib.pyplot as plt

@dataclass
class Grid():
   w: int
   h: int
   values: list[list[int]]= field(repr=False)
   start: tuple[int, int]
   end: tuple[int, int]

   def draw(self):
      fig = px.imshow(self.values, text_auto=True)

      fig.show()
   def height_difference(self, a: tuple[int, int],b: tuple[int,int]) -> int:
      height_a = self.values[a[1]][a[0]]
      height_b = self.values[b[1]][b[0]]
      return height_b - height_a
      
   def to_graph(self):
      G = nx.DiGraph()
      # add nodes
      for r, row in enumerate(self.values):
         for c, col in enumerate(row):
            G.add_node((c,r))
      # now add edges
      for r, row in enumerate(self.values):
         for c, col in enumerate(row):
            a = (c,r)
            # nach rechts
            if c < (self.w-1):
               b = (c+1, r)
               w = self.height_difference(a,b)
               if w < 2:
                  G.add_edge(a,b)
            # nach unten
            if r < (self.h-1):
               b = (c,r+1)
               w = self.height_difference(a,b)
               if w < 2:
                  G.add_edge(a,b)
            # nach links
            if c > 0:
               b = (c-1,r)
               w = self.height_difference(a,b)
               if w < 2:
                  G.add_edge(a,b)
            # nach oben
            if r > 0:
               b = (c,r-1)
               w = self.height_difference(a,b)
               if w < 2:
                  G.add_edge(a,b)
      return G

   def positions(self) -> dict:
      d = {}
      for r, row in enumerate(self.values):
         for c, col in enumerate(row):
            d.update(({(c,r): (c*10,-r*10)}))
      return d
   
   def heights(self) -> dict:
      d = {}
      for r, row in enumerate(self.values):
         for c, col in enumerate(row):
            d.update(({(c,r): self.values[r][c]}))
      return d

def parseInput(inp: str) -> Grid:
   
   def letter_to_value(c: str) -> int:
      '''
      returns the heightvalue from a given letter 
      '''
      return "abcdefghijklmnopqrstuvwxyz".index(c)
   
   lines = inp.splitlines()
   h = len(lines)
   w = len(lines[0])
   start = (0,0)
   end = (0,0)
   heights = []
   for row, line in enumerate(lines):
      height_row = []
      for col, char in enumerate(line):
         match char:
            case 'S':
               start = (col, row)
               height_row.append(letter_to_value('a'))
            case 'E':
               end = (col, row)
               height_row.append(letter_to_value('z'))
            case letter:
               height_row.append(letter_to_value(letter))
      heights.append(height_row)
   return Grid(w,h,heights,start,end)

   
               

if __name__ == "__main__":
   example = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
   """.strip()
   grid = parseInput(example) 
   print(grid)
   # grid.draw()
   G = grid.to_graph()
   print(G)
   shortest_path = nx.dijkstra_path(G,source=grid.start,target=grid.end)
   shortest_path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
   positions = grid.positions()
   heights = grid.heights()
   nx.draw(G, pos=positions, with_labels=True, labels=heights)
   nx.draw_networkx_nodes(G,nodelist=shortest_path,pos=positions, edgecolors='#ff00ff')
   nx.draw_networkx_nodes(G,nodelist=[grid.start, grid.end],pos=positions, edgecolors='#ffff00')
   nx.draw_networkx_edges(G,edgelist=shortest_path_edges,pos=positions, edge_color='#ff00ff', width=2)
   plt.show()
   print(shortest_path_edges)
   print(len(shortest_path_edges))

   starting_points = [(c,r) for r,row in enumerate(grid.values) for c,value in enumerate(row) if value==0]
   print(starting_points)
   minimum_hiking_distance = min([nx.shortest_path_length(G,source=s, target=grid.end) for s in starting_points])
   print(minimum_hiking_distance)
   with open("input.txt", "r", encoding="utf8") as f:
      my_input=f.read().strip()
   grid = parseInput(my_input)
   
   print(grid)
   G = grid.to_graph()
   shortest_path = nx.shortest_path(G,source=grid.start,target=grid.end)
   shortest_path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
   print(len(shortest_path_edges)) # part 1
   starting_points = [(c,r) for r,row in enumerate(grid.values) for c,value in enumerate(row) if value==0 and nx.has_path(G,(c,r), grid.end)]
   print(starting_points)
   minimum_hiking_distance = min([nx.shortest_path_length(G,source=s, target=grid.end) for s in starting_points])
   print(minimum_hiking_distance) # part 2
   positions = grid.positions()
   heights = grid.heights()
   # connected_to_end = nx.node_connected_component(G, grid.end)
   nx.draw(G, pos=positions, node_size=10)
   nx.draw_networkx_nodes(G,nodelist=[grid.start, grid.end],pos=positions, edgecolors='#ff0000',node_size=10)
   nx.draw_networkx_edges(G,edgelist=shortest_path_edges,pos=positions, edge_color='#ff00ff', width=2)
   plt.show()
   print(shortest_path_edges)

