def bfs(start, end, board, c):
    M = len(board[0])
    N = len(board)
    visit = [[0] * M for _ in range(N)]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    arr = []
    arr.append(start)
    visit[start[0]][start[1]] = 0

    while arr:
        cur = arr.pop(0)
        x = cur[0]
        y = cur[1]
        now = visit[x][y]

        for i in range(4):
            wx = x + direction[i][0]
            wy = y + direction[i][1]
            if wx >= N or wy >= M or wx < 0 or wy < 0:
                continue

            if board[wx][wy] == 0 or board[wx][wy] == 3:   # 장애물 없는
                if visit[wx][wy] == 0 or visit[wx][wy] > now + 1:
                    visit[wx][wy] = now + 1
                    arr.append([wx, wy])
                else:
                    continue

            elif board[wx][wy] == 1:   # 장애물 있는
                if visit[wx][wy] == 0 or visit[wx][wy] > now + 1 + c:
                    visit[wx][wy] = now + 1 + c
                    arr.append([wx, wy])
                else:
                    continue

        # if cur == end:
        #     break

    return visit[end[0]][end[1]]
    # return visit


def solution(board, c):
    # 시작 위치
    for i in range(len(board)):
        if 2 in board[i]:
            start = [i, board[i].index(2)]
            break

    # 도착 위치
    for j in range(len(board)):
        if 3 in board[j]:
            end = [j, board[j].index(3)]
            break

    answer = bfs(start, end, board, c)
    return answer


solution(board, c)


board = [[0,0,0,0,2,0,0,0,0,0],
        [0,0,1,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,0,1,0],
        [0,0,1,1,1,1,1,0,0,0],
        [0,0,0,0,3,0,0,0,1,0]]

c = 2
