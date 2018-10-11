avg = [1, 1, 1, 1, 0, 0, 0, 0]

from copy import copy
avg2 = copy(avg)

count1 = 0
for i in range(len(avg)-1):
    for j in range(len(avg)-1):
        if avg[j] > avg[j+1]:
            temp = avg[j+1]
            avg[j+1] = avg[j]
            avg[j] = temp
            count1 += 1

count2 = 0
for i in range(len(avg2)-1):
    for j in range(len(avg2)-1):
        if avg2[j] < avg2[j+1]:
            temp = avg2[j]
            avg2[j] = avg2[j+1]
            avg2[j+1] = temp
            count2 += 1

print(min(count1, count2))
count1
count2
