def solution(N, house):
    factory_point = []
    for a in range(len(house)):
        factory_point.append([])

    min_distance = 80000
    max_distance = 0
    for i in range(len(house)):
        for j in range(-100, 100):
            for k in range(-100, 100):
                factory = [j, k]
                distance = pow(factory[0]-house[0], 2) + pow(factory[1]-house[1], 2)
                if distance > max_distance:
                    max_distance = distance





    return answer


N = 1
house = [[0,0]]
N = 3
house = [[0,0], [1,0]]

solution(N, house)
