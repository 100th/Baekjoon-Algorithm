# 몇개 받을껀지
N, Q = map(int, input().split())

# 체크포인트 설정
check = {}
for i in range(int(N)):
    X, Y = map(int, input().split())
    check[i] = X, Y

# 질의 설정
question = {}
for i in range(int(Q)):
    A, B, HP = map(int, input().split())
    question[i] = A, B, HP

# 부스터
def booster(x, y):
    for k in range(len(check)):
        if check[k][0] == x or check[k][1] == y:
            x_boost, y_boost = check[k]
        else:
            x_boost, y_boost = x, y
        return x_boost, y_boost

# 시작
for k in range(len(question)):
    start_check = question[k][0]
    goal_check = question[k][1]

    HP = question[k][2]
    x_start, y_start = check[start_check-1]
    x_goal, y_goal = check[goal_check-1]

    if (x_start, y_start) != (x_goal, y_goal):
        x, y = x_start, y_start
        if HP != 0:
            for i in range(HP): # x+1
                x = x + 1
                HP = HP - 1
                x_new, y_new = booster(x, y)
                if (x_new, y_new) != (x, y):
                    x, y = x_new, y_new
                    HP = HP + 1

            if (x, y) != (x_goal, y_goal):
                HP_org = HP
                for i in range(HP): # x-1
                    x = x - 1
                    HP = HP - 1
                    x_new, y_new = booster(x, y)
                    if (x_new, y_new) != (x, y):
                        x, y = x_new, y_new
                        HP = HP + 1
                        break
                HP = HP_org


                if (x, y) == (x_new, y_new):
                    for i in range(HP): # y+1
                        y = y + 1
                        HP = HP - 1
                        x_new, y_new = booster(x, y)
                        if (x_new, y_new) != (x, y):
                            x, y = x_new, y_new
                            HP = HP + 1

                    if (x, y) == (x_new, y_new):
                        for i in range(HP): # y-1
                            y = y - 1
                            HP = HP - 1
                            x_new, y_new = booster(x, y)
                            if (x_new, y_new) != (x, y):
                                x, y = x_new, y_new
                                HP = HP + 1

        else:
            while True:
                x_new, y_new = booster(x, y)
                if (x_new, y_new) == (x, y):
                    break

        if (x, y) == (x_goal, y_goal):
            print("YES")
        else:
            print("NO")
