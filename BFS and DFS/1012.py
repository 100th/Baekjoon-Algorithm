import sys
sys.setrecursionlimit(100000)

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    baechu = []
    for i in range(K):
        x, y = map(int, input().split())
        baechu.append([x, y])

    visit_list = []
    for i in range(N):
        visit_list.append([False] * M)

    input_list = []
    for i in range(N):
        input_list.append([0] * M)

    for i in range(len(baechu)):
        [x, y] = baechu[i]
        input_list[y][x] = 1


    def DFS(y,x):
        global value
        value += 1
        visit_list[y][x] = True

        for i in range(4):
            dir_y = y + direction[i][1]
            dir_x = x + direction[i][0]
            if dir_x > -1 and dir_x < M and dir_y > -1 and dir_y < N:
                if visit_list[dir_y][dir_x] == False and input_list[dir_y][dir_x] == 1:
                    DFS(dir_y,dir_x)


    result = []
    for i in range(N):
        for j in range(M):
            if visit_list[i][j] == False and input_list[i][j] == 1:
                value = 0
                DFS(i,j)
                result.append(value)

    print(len(result))
