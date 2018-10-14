def bfs(start, mymap, N):
    visit = [[0] * N for _ in range(N)]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    arr = []
    for i in range(len(start)):
        arr.append(start[i])
        visit[start[i][0]][start[i][1]] = 0

    while arr:
        cur = arr.pop(0)
        x = cur[0]
        y = cur[1]

        now = visit[x][y]

        for i in range(4):
            wx = x + direction[i][0]
            wy = y + direction[i][1]
            if wx >= N or wy >= N or wx < 0 or wy < 0:
                continue
            if visit[wx][wy] == 0 and mymap[wx][wy] == 0:
                visit[wx][wy] = now + 1
                arr.append([wx, wy])

    return visit


def solution(N, bus_stop):
    mymap = []
    for i in range(N):
        mymap.append([0] * N)

    start = []
    for i in range(len(bus_stop)):
        start.append([bus_stop[i][0]-1, bus_stop[i][1]-1])
        mymap[start[i][0]][start[i][1]] = 1

    answer = bfs(start, mymap, N)
    return answer


solution(N, bus_stop)


N = 3
bus_stop = [[1,2], [3,3]]
