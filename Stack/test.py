sequence=[]
stack=[]
plus_minus=['+']
N = int(input())

for i in range(1, N + 1):
    sequence.append(int(input()))    # sequence = [4, 3, 6, 8, 7, 5, 2, 1]
    stack.append(i)                  # stack = [1, 2, 3, 4, 5, 6, 7, 8]

sequence.append('end')      # sequence = [4, 3, 6, 8, 7, 5, 2, 1, end]
stack.append('fin')         # stack = [1, 2, 3, 4, 5, 6, 7, 8, fin]
stack.append('dummy')       # stack = [1, 2, 3, 4, 5, 6, 7, 8, fin, dummy]

i=0
j=0

while True:
    if sequence[i] == stack[j]:
        plus_minus.append('-')
        stack.pop(j)
        i+=1
        j-=1
        if sequence[i]=='end':break
    else :
        j += 1
        if stack[j]=='fin':break
        plus_minus.append('+')
        
if len(stack)==2:
    for k in plus_minus:
        print(k)
else:
    print('NO')
