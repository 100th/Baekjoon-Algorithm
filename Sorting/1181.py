a = []
for k in range(int(input())):
    tmp = input()
    if tmp not in a:
        a.append(tmp)
a.sort()

def sorting(a):
    if len(a)>1:
        mid = len(a)//2
        left = sorting(a[:mid])
        right = sorting(a[mid:])

        i, j, k = 0, 0 ,0
        while i < len(left) and j < len(right):
            if len(left[i]) <= len(right[j]):
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
            k+=1
        while i <len(left):
            a[k] = left[i]
            i+=1
            k+=1
        while j <len(right):
            a[k] = right[j]
            j+=1
            k+=1
    return a

for i in sorting(a):
    print(i)
