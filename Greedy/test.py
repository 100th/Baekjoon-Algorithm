n = int(input())
p = list(map(int, input().rstrip().split(" ")))

def quicksort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array[0]
        print("pivot : ", pivot)
        greater = []
        lesser = []

        for element in range(1, length):
            if array[element] < pivot:
                print("lesser : ", array[element])
                lesser.append(array[element])
            else:
                print("greater : ", array[element])
                greater.append(array[element])

        return quicksort(lesser) + [pivot] + quicksort(greater)

new_p = quicksort(p)
print("new_p : ", new_p)
q = []

print("new_p[0]", new_p[0])
q.append(new_p[0])

for i in range(len(new_p)-1):
    print("q[i] + new_p[i+1]", q[i] + new_p[i+1])
    q.append(q[i] + new_p[i+1])

print("q : ", q)

# for i in range(1, len(new_p)):
#     print("q[i-1] : ", q[i-1])
#     print("new_p[i] : ", new_p[i])
#     q.append(q[i-1] + new_p[i])

sum = 0
for j in range(len(q)):
    sum += q[j]
    print("sum : ", sum)

print(sum)
