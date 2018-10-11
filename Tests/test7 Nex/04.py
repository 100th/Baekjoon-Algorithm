vertexList = []
for i in range(friends_nodes):
    vertexList.append(i)

edgeList = []
for i in range(friends_edges):
    edgeList.append((friends_from, friends_to))

vertexList = [1, 2, 3, 4, 5]
edgeList = [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 5]]

visitedList = []
adjacencyList = [[] for vertex in vertexList]

for j in range(len(vertexList)):
    for i in range(len(edgeList)):
        if edgeList[i][0] == vertexList[j]:
            adjacencyList[j].append(edgeList[i][1])
        if edgeList[i][1] == vertexList[j]:
            adjacencyList[j].append(edgeList[i][0])

stack = [1]
visitedVertex = []
while stack:
    current = stack.pop()
    print(current)
    for neighbor in adjacencyList[current-1]:
        if not neighbor in visitedVertex:
            stack.append(neighbor)
    visitedVertex.append(current)


visitedVertex.sort()
for i in range(len(visitedVertex)-1):
    if visitedVertex[i] == visitedVertex[i+1]:
        that = visitedVertex[i]
        break

that
friend = adjacencyList[that-1]

trio = []
for j in range(len(adjacencyList)):
    count = 0
    for k in range(len(friend)):
        for i in range(len(friend)):
            if friend[i] in adjacencyList[friend[k]-1]
                count += 1

        if count = 2:
            trio.append()

adjacencyList
