def solution(healths, items):
    answer = []
    for j in range(len(healths)):
        for i in range(len(items)):
            if (healths[j] - items[i][1]) >= 100:
                answer.append(i + 1)
                answer = list(set(answer))

    return answer

# healths = [200,120,150]
# items = [[30,100],[500,30],[100,400]]

healths = [300,200,500]
items = [[1000, 600], [400, 500], [300, 100]]

solution(healths, items)
