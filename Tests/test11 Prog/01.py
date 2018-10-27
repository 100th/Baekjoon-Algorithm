skill = 'CBD'
skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA']

def solution(skill, skill_trees):
    result = 0
    for j in range(len(skill_trees)):
        which = []
        for i in range(len(skill_trees[j])):
            if skill_trees[j][i] in skill:
                which.append(skill.index(skill_trees[j][i]))
        which2 = sorted(which)
        # print(which)
        if which == [] or which == [0]:
            result += 1
            # print('here', which2)
        elif which == which2 and which2[0] == 0:
            flag = True
            for k in range(1, len(which2)):
                if which2[k] != which2[k-1] + 1:
                    flag = False
            if flag == True:
                result += 1
    return result




result = 0
for j in range(len(skill_trees)):
    which = []
    for i in range(len(skill_trees[j])):
        if skill_trees[j][i] in skill:
            which.append(skill.index(skill_trees[j][i]))
    which2 = sorted(which)
    # print(which)
    if which == [] or which == [0]:
        result += 1
        # print('here', which2)
    elif which == which2 and which2[0] == 0:
        flag = True
        for k in range(1, len(which2)):
            if which2[k] != which2[k-1] + 1:
                flag = False
        if flag == True:
            result += 1
        # print('here2', which2)

print(result)
