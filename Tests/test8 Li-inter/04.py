import sys

def bfs():
    visit = [[0] * M for _ in range(N)]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    jang_first = False
    arr = []
    arr.append([0, 0])
    visit[0][0] = 1
    while arr:
        cur = arr.pop(0)
        x = cur[0]
        y = cur[1]
        if cur == [N-1, M-1]:
            break
        now = visit[x][y]

        for i in range(4):
            wx = x + direction[i][0]
            wy = y + direction[i][1]
            if wx >= N or wy >= M or wx < 0 or wy < 0:
                continue
            if (visit[wx][wy] == 0 and map[wx][wy] == 'R') or (map[wx][wy] == 'H' and jang_first == False):
                if map[wx][wy] == 'H':
                    jang_first = True
                visit[wx][wy] = now + 1
                arr.append([wx, wy])

    print(visit[N-1][M-1]-1)

# line = input().strip().split(' ')
# N = int(line[0])
# M = int(line[1])
# map = [""] * N
# for y in range(N):
#     map[y] = input()
# bfs()



if __name__ == '__main__':
    line = sys.stdin.readline().strip().split(' ')
    N = int(line[0])
    M = int(line[1])
    map = [""] * N
    for y in range(N):
        map[y] = sys.stdin.readline()
    bfs()
