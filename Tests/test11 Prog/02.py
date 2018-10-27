dirs = 'ULURRDLLU'
dirs = 'LULLLLLLU'
# dirs = 'L'

def solution(dirs):
    now = [5, 5]
    mymap = []
    for i in range(11):
        mymap.append([0] * 11)

    mymap[5][5] = 1

    street = 0
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            if now[1] == 0:
                continue
            else:
                now[1] = now[1] + 1

        elif dirs[i] == 'D':
            if now[1] == 10:
                continue
            else:
                now[1] = now[1] - 1

        elif dirs[i] == 'R':
            if now[0] == 10:
                continue
            else:
                now[0] = now[0] + 1

        else:
            if now[0] == 0:
                continue
            else:
                now[0] = now[0] - 1

        if mymap[now[0]][now[1]] == 0:
            mymap[now[0]][now[1]] = 1
            street += 1

    return street

solution(dirs)
