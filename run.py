# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
ad = search.GPSProblem('A', 'D'
                       , search.romania)
de = search.GPSProblem('D', 'E'
                       , search.romania)
hc = search.GPSProblem('H', 'C'
                       , search.romania)
ot = search.GPSProblem('O', 'T'
                       , search.romania)

print("\n")
print("####################  Traza camino AB  #############################")

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.bab_first_graph_search(ab).path())
print(search.babsubestimation_first_graph_search(ab).path())

print("\n")
print("#################### Traza camino AD  #############################")

print(search.breadth_first_graph_search(ad).path())
print(search.depth_first_graph_search(ad).path())
print(search.bab_first_graph_search(ad).path())
print(search.babsubestimation_first_graph_search(ad).path())

print("\n")
print("####################  Traza camino DE  #############################")

print(search.breadth_first_graph_search(de).path())
print(search.depth_first_graph_search(de).path())
print(search.bab_first_graph_search(de).path())
print(search.babsubestimation_first_graph_search(de).path())

print("\n")
print("####################  Traza camino HC  #############################")

print(search.breadth_first_graph_search(hc).path())
print(search.depth_first_graph_search(hc).path())
print(search.bab_first_graph_search(hc).path())
print(search.babsubestimation_first_graph_search(hc).path())

print("\n")
print("####################  Traza camino OT  #############################")

print(search.breadth_first_graph_search(ot).path())
print(search.depth_first_graph_search(ot).path())
print(search.bab_first_graph_search(ot).path())
print(search.babsubestimation_first_graph_search(ot).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
