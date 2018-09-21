N = int(input())
command = []
stack = []

for k in range(N):
    tmp = input()
    command.append(tmp)

for i in range(N):
    if command[i][:3] == 'pus':
        new_command = command[i].split()
        stack.append(new_command[1])

    elif command[i] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack.pop())

    elif command[i] == 'size':
        print(len(stack))

    elif command[i] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')

    elif command[i] == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[len(stack)-1])
