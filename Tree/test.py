vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
adjacencyList = [[] for vertex in vertexList]
print(adjacencyList)

edgeList = [(0,1), (0,2), (1,3), (3,4), (4,5), (1,6)]

for edge in edgeList:
    adjacencyList[edge[0]].append(edge[1])


print(adjacencyList)
