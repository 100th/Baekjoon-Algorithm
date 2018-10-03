num = int(input())

T = [1 for i in range(num)]
# T
arr = list(map(int, input().rstrip().split()))
# arr

for i in range(len(T)):
    T[i] = 1
    for j in range(i, -1, -1):
        # print('i : ', i)
        # print('j : ', j)
        # print('arr[i] : ', arr[i])
        # print('arr[j] : ', arr[j])
        # print('T[i] : ', T[i])
        # print('T[j] : ', T[j])
        if arr[j] < arr[i] and T[j] >= T[i]:
            T[i] = T[j] + 1
        #     print('+1됨')
        # print('---------------')

print(str(max(T)))
# T
