import sys
sys.setrecursionlimit(100000)

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

n = int(input())
input_list = []
for i in range(n):
    input_list.append(list(map(int, input().split())))

visit_list = []
for i in range(n):
    visit_list.append([False] * n)

def DFS(y,x):
    global value
    value += 1
    visit_list[y][x] = True     # 방문한다

    for i in range(4):
        dir_y = y + direction[i][1]
        dir_x = x + direction[i][0]
        if dir_x > -1 and dir_x < n and dir_y > -1 and dir_y < n:
            if visit_list[dir_y][dir_x] == False and input_list[dir_y][dir_x] == 1:
                DFS(dir_y,dir_x)

result = []
for i in range(n):
    for j in range(n):
        if visit_list[i][j] == False and input_list[i][j] == 1:
            value = 0
            DFS(i,j)
            result.append(value)

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])
