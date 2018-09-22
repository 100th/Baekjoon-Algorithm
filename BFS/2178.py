# arr : x, y 좌표 얼마나 이동했는지
# 좌표문제에서는 direction 설정한다
# 다시 돌아오는 경우 없이 그냥 계속 가서 끝점 찍으면 됨 -> 이게 BFS다.
def bfs():
    arr = []
    arr.append([0, 0])
    visit[0][0] = 1
    while arr:
        cur = arr.pop(0)
        x = cur[0]
        y = cur[1]
        if cur == [row-1, col-1]:
            print(visit[x][y])
            # print('final visit :', visit[x][y])
            break
        now = visit[x][y]

        for i in range(4):
            wx = x + direction[i][0]
            wy = y + direction[i][1]
            if wx >= row or wy >= col or wx < 0 or wy < 0:
                continue
            if visit[wx][wy] == 0 and map[wx][wy] == '1':
                visit[wx][wy] = now + 1
                arr.append([wx, wy])
        # print('arr :', arr)
        # print('visit :', visit)

row, col = map(int, input().split())
map = [""] * row
visit = [[0] * col for _ in range(row)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for i in range(row):
    map[i] = input()

# print(map)
bfs()
