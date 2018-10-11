A = [1, -1]

result = [A[0]]
i = 0
while True:
    next = A[i]
    if next == -1:
        break
    result.append(A[next])
    i = next

print(result)
print(len(result))
