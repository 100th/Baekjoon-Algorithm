
N = input()

a = []
for k in range(int(N)):
    word = input()
    if word not in a:
        a.append(word)

print(a)
a.sort(reverse=True)
a
