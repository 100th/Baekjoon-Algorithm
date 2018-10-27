cookie = [1, 1, 2, 3]
# cookie = [1, 1]
cookie = [1, 2, 4, 5]

def solution(cookie):
    result_list = []
    for start in range(len(cookie)):
        for mid1 in range(start, len(cookie)):
            for mid2 in range(mid1, len(cookie)):
                for end in range(mid2, len(cookie)):
                    if sum(cookie[start:mid1+1]) == sum(cookie[mid2:end+1]):
                        result_list.append(sum(cookie[start:mid1+1]))

    if result_list == []:
        return 0
    else:
        return max(result_list)
        # print(result_list)

solution(cookie)
