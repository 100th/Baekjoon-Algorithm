import sys
sys.setrecursionlimit(100000)

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

N = int(input())

# ★★★★★★★★★★★★★★★★★★★★★★ 2차원 리스트를 숫자로 받는 방법
height_list = []
for i in range(N):
    height_list.append([int(x) for x in input().split()])
# ★★★★★★★★★★★★★★★★★★★★★★

min_max_list = []
for i in range(N):
    for j in range(N):
        min_max_list.append(height_list[i][j])
max_height = max(min_max_list)
min_height = min(min_max_list)

def DFS(y,x):
    visit_list[y][x] = True

    for i in range(4):
        dir_y = y + direction[i][1]
        dir_x = x + direction[i][0]
        if dir_x > -1 and dir_x < N and dir_y > -1 and dir_y < N:
            if visit_list[dir_y][dir_x] == False and input_list[dir_y][dir_x] == 0:
                DFS(dir_y, dir_x)

result = []
for k in range(min_height, max_height):
    input_list = []
    for i in range(N):
        input_list.append([0] * N)

    visit_list = []
    for i in range(N):
        visit_list.append([False] * N)

    for a in range(N):
        for b in range(N):
            if height_list[a][b] <= k:
                input_list[a][b] = 1

    value = 0
    for i in range(N):
        for j in range(N):
            if visit_list[i][j] == False and input_list[i][j] == 0:
                value += 1
                DFS(i, j)
    result.append(value)

if len(result) == 0:
    print(1)
else:
    print(max(result))
