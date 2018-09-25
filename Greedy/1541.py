"""
실패
"""

sentence = str(input())

sentence = sentence + 'Z'

solve = 0
start_number = True
for i in range(x, len(sentence)):
    if sentence[i] == '+':
        if start_number == True:
            next = int(sentence[:i])
            solve += next
            which = i
            start_number = False
            # print(solve, which, 'here1')

        else:
            next = int(sentence[which+1:i])
            solve += next
            which = i
            # print(solve, which, 'here2')


    if sentence[i] == '-':
        if start_number == True:
            next = int(sentence[:i])
            solve += next
            which = i
            start_number = False
            # print(solve, which, 'here3')
        else:
            next = int(sentence[which+1:i])
            solve -= next
            which = i
            # print(solve, which, 'here4')

        for j in range(i+1, len(sentence)):
            if sentence[j] == '+':
                next = int(sentence[which+1:j])
                solve -= next
                which = j
                i += j
                # print(solve, which, 'here5')

            if sentence[j] == '-' or sentence[j] == 'Z':
                next = int(sentence[which+1:j])
                solve -= next
                which = j
                i = j
                # print(solve, which, 'here6')
                break

    # if which == len(sentence):
        # print(solve, which, 'here7')
        # break

if start_number == True:
    print(int(sentence[:-1]))
else:
    print(solve)
