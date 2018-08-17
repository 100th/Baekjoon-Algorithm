n = int(input())
if n == 0:
    False
else:
    p = list(map(float, input().rstrip().split(" ")))

    def quicksort(array):
        length = len(array)
        if length <= 1:
            return array
        else:
            pivot = array[0]
            greater = []
            lesser = []

            for element in range(1, length):
                if array[element] < pivot:
                    lesser.append(array[element])
                else:
                    greater.append(array[element])

            return quicksort(lesser) + [pivot] + quicksort(greater)

    if n == 0 or 0 in p == True:
        False

    else:
        if n > 1:
            new_p = quicksort(p)
            q = []

            q.append(new_p[0])

            # for i in range(len(new_p)-1):
            #     q.append(q[i] + new_p[i+1])

            for i in range(1, len(new_p)):
                q.append(q[i-1] + new_p[i])

            sum = 0
            for j in range(len(q)):
                sum += q[j]

            print(sum)

        else:
            print(p[0])
