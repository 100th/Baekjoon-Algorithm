def solution(N, stages):
    fail_list = []

    for i in range(1, len(stages) - 2):
        fail_count = stages.count(i)

        if stages.count(i) == 0:
            fail_ratio = 0
        else:
            challenge_count = len(stages) - stages.index(i)
            fail_ratio = fail_count/challenge_count

        fail_list.append(fail_ratio)

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
