N = int(input())
quiz_list = []

for i in range(N):
    quiz_list.append(input())

for k in range(N):
    stack = []
    VPS = 'YES'

    if quiz_list[k][0] == ')':
        VPS = 'NO'
        print(VPS)
        continue

    for j in range(len(quiz_list[k])):
        if quiz_list[k][j] == '(':
            stack.append(1)
        else:
            if len(stack) == 0 and quiz_list[k][j] == ')':
                VPS = 'NO'
                break
            else:
                stack.pop()

    if len(stack) != 0:
        VPS = 'NO'

    print(VPS)
