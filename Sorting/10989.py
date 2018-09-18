def sorting(N):
    num_list = []
    for k in range(N):
        num = int(input())
        num_list.append(num)

    # 카운팅 정렬
    if min(num_list) < 0:
        raise
    i = 0
    n = len(num_list)
    k = max(num_list) + 1
    C = [0] * k
    for j in range(n):
        C[num_list[j]] = C[num_list[j]] + 1
    for j in range(k):
        while C[j] > 0:
            (num_list[i], C[j], i) = (j, C[j]-1, i+1)

    for j in range(len(num_list)):
        print(num_list[j])

N = int(input())
sorting(N)




    # # 삽입 정렬
    # for i in range(1, len(num_list)):
    #     for j in range(i, 0, -1):
    #         if num_list[j] < num_list[j-1]:
    #             num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
    #         else:
    #             break
