n = int(input())

input_list = []
for i in range(n):
    input_list.append(list(map(str, input().split())))
input_list
now = []
for i in range(n):
    now.append([0] * n)

def direction(past, present):
    if past[0] == 'F':
        if present[0] == 'F':
            future = 'F'
            return future
        elif present[0] == 'R':
            future = 'R'
            return future
        elif present[0] == 'L':
            future = 'L'
            return future
        elif present[0] == 'B':
            future = 'B'
            return future

    elif past[0] == 'R':
        if present[0] == 'F':
        elif present[0] == 'R':
        elif present[0] == 'L':
        elif present[0] == 'B':

    elif past[0] == 'L':
        if present[0] == 'F':
        elif present[0] == 'R':
        elif present[0] == 'L':
        elif present[0] == 'B':

    elif past[0] == 'B':
        if present[0] == 'F':
        elif present[0] == 'R':
        elif present[0] == 'L':
        elif present[0] == 'B':


def move(present, now):
    how_many = present[1]
    if present[0] == 'F':
        now[0] += how_many
    elif present[0] == 'R':
        now[0] += how_many
    elif present[0] == 'L':
        now[0] += how_many
    elif present[0] == 'B':
        now[0] -= how_many

count = 0
while True:
    if count == 0:
        past = 'F1'
        present = input_list[0][0]
        future = direction(past, present)
        how_many = present[1]
        if


    for i in range()

input_list[0][0][0]
