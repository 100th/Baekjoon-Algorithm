# stats = [5, 3, 4, 6, 2, 1]
stats = [6, 2, 3, 4, 1, 5]
# stats = [1, 2, 3, 4, 5, 6, 7, 8]

def solution(stats):
    group = [[stats[0]]]
    for i in range(1, len(stats)):
        flag_enter = False
        for j in range(len(group)):
            if stats[i] > max(group[j]): # 하나라도 작은게 있다면
                flag_enter = True       # 들어간다
                group[j].append(stats[i])   # 그 그룹으로
                break

        if flag_enter == False:         # 전부 다 크면
            group.append([stats[i]])    # 새로 만든다

    return len(group)

solution(stats)
