def solution(people, tshirts):
    result = 0
    people.sort()
    tshirts.sort()
    for i in range(len(people)):
        for j in range(len(tshirts)):
            if people[i] <= tshirts[j]:
                result += 1
                tshirts[j] = 0
                break

    return result

people = [1, 2, 3]
tshirts = [1, 1]

solution(people, tshirts)
