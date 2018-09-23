from sys import*
setrecursionlimit(10**6)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

vertical,horizontal,unit = map(int,input().strip().split())

input_list = [[0]*horizontal for i in range(vertical)]

visit = [[True]*horizontal for i in range(vertical)]

for i in range(unit):
    x1,y1,x2,y2 = map(int,input().strip().split())
    for ver in range((vertical-y2),(vertical-y1),1):
        for hor in range(x1,x2,1):
            input_list[ver][hor]=1

def dfs(y,x):
    global val
    val+=1
    visit[y][x] = False     # 방문한다

    for i in range(4):
        dir_y = y + dy[i]
        dir_x = x + dx[i]
        if dir_x > -1 and dir_x < horizontal and dir_y > -1 and dir_y < vertical:
            if visit[dir_y][dir_x] == True and input_list[dir_y][dir_x] == 0: # 온적이 없다면
                dfs(dir_y,dir_x)            # DP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

result = []
for i in range(vertical):
    for j in range(horizontal):
        if visit[i][j] == True and input_list[i][j] == 0:  # 온적이 없다면
            val = 0
            dfs(i,j)
            result.append(val)

print(len(result))
for i in sorted(result):
    print(i,end=" ")



"""
M, N, K = map(int, input().split())
square_map = []
for _ in range(K):
    square_map.append([])

for a in range(K):
    start_x, start_y, end_x, end_y = map(int, input().split())
    square_map[a].append(start_x+1)
    square_map[a].append(start_y+1)
    square_map[a].append(end_x)
    square_map[a].append(end_y)

map_check = []
for i in range(len(square_map)):
    a = square_map[i][0]
    b = square_map[i][1]
    c = square_map[i][2]
    d = square_map[i][3]
    for j in range(c - a + 1):          # 4
        for k in range(d - b + 1):      # 2
            map_check.append([a + j, b + k])

question_map = []
for i in range(M):
    question_map.append([0] * N)

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for i in range(len(map_check)):
    x = int(map_check[i][0])
    y = int(map_check[i][1])
    len1 = len(question_map) # 5
    question_map[len1-y][x-1] = 1 # 2 1

def bfs():
    arr_count = []
    for i in range(N):
        for j in range(M):
            if question_map[j][i] == 1:
                continue
            else:
                arr = []
                arr.append([i, j])
                arr_area = 1
                arr_area2 = 0
                while arr:
                    cur = arr.pop(0)
                    x = cur[0]
                    y = cur[1]
                    if arr_area2 == arr_area:
                        arr_count.append(arr_area)
                        break

                    for i in range(4):
                        wx = x + direction[i][0]
                        wy = y + direction[i][1]

                        if wx >= N or wy >= M or wx < 0 or wy < 0:
                            continue

                        if question_map[wy][wx] == 0:
                            question_map[j][i] = 1
                            arr_area += 1
                            arr_area2 = arr_area
                            arr.append([wx, wy])

                        if question_map[j][i] == 0:
                            question_map[j][i] = 1
                            arr_area2 = arr_area
                            arr.append([i, j])

    print(arr_count)

bfs()

# question_map
"""
