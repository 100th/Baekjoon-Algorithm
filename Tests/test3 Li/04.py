def function(graph, query):
    count_list = []
    vertexList, edgeList = graph
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    for i in range(len(query)):
        start = query[i][0]
        end = query[i][1]

        count = 0
        count = loop(start, adjacencyList, end, count)
        count_list.append(count)

        return count_list

def loop(vertex, adjacencyList, end, count):
    adjacency = adjacencyList[vertex - 1]
    for i in range(len(adjacency)):
        new_vertex = adjacency[i]
        if end in adjacency:
            count += 1
            break

        loop(new_vertex, adjacencyList, end)

    return count

def solution(N, directory, query):
    vertexList = []
    for i in range(0, N-1):
        vertexList.append(i)

    new_query = []
    for j in range(len(query)):
        tmp1 = query[j][0] -1
        tmp2 = query[j][1] -1
        new_q = [tmp1, tmp2]
        new_query.append(new_q)

    edgeList = []
    for j in range(len(directory)):
        tmp1 = directory[j][0] -1
        tmp2 = directory[j][1] -1
        reverse = [tmp2, tmp1]
        edgeList.append(reverse)

        tmp3 = directory[j][0] -1
        tmp4 = directory[j][1] -1
        new = [tmp3, tmp4]
        edgeList.append(new)
    edgeList.sort()

    graph = (vertexList, edgeList)
    answer = function(graph, new_query)

    return answer


N = 5
directory = [ [1, 2], [1, 3], [2, 4], [2, 5] ]
query = [ [1, 5], [2, 5], [3, 5], [4, 5] ]
solution(N, directory, query)



# vertexList = ['0', '1', '2', '3', '4', '5', '6']
# edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
# graphs = (vertexList, edgeList)
