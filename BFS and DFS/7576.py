# from sys import*
# setrecursionlimit(10**6)

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

N = int(input())
input_list = []
for i in range(N):
    input_list.append(str(input()))

visit_list = []
for i in range(N):
    visit_list.append([False] * N)

def DFS(y,x):
    global value
    value += 1
    visit_list[y][x] = True     # 방문한다

    for i in range(4):
        dir_y = y + direction[i][1]
        dir_x = x + direction[i][0]
        if dir_x > -1 and dir_x < N and dir_y > -1 and dir_y < N:
            if visit_list[dir_y][dir_x] == False and input_list[dir_y][dir_x] == '1': # 온적이 없다면
                DFS(dir_y,dir_x)            # DP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

result = []
for i in range(N):
    for j in range(N):
        if visit_list[i][j] == False and input_list[i][j] == '1':  # 온적이 없다면
            value = 0
            DFS(i,j)
            result.append(value)

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])
