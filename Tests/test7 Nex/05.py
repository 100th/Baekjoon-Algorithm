numbers = [1, 5]
k = 1

from copy import copy
new = copy(numbers)

new = list(set(new))

what = []
for i in range(len(new)):
    what.append([new[i], new[i] + k])

result = 0
for i in range(len(what)):
    left = False
    right = False
    if what[i][0] in numbers:
        left = True
    if what[i][1] in numbers:
        right = True
    if left == True and right == True:
        result += 1

print(result)
