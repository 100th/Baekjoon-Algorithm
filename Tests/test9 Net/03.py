s1 = 'a'
s2 = 'b'

def solution(s1, s2):
    tmp_list = []
    for i in range(len(s2)):
        if s2[-(i+1):] == s1[:i+1]:
            tmp_list.append(i+1)
    if len(tmp_list) == 0:
        new_len = len(s1) + len(s2)
    else:
        new_len = len(s1) + len(s2) - max(tmp_list)


    tmp_list2 = []
    for j in range(len(s1)):
        if s1[-(j+1):] == s2[:j+1]:
            tmp_list2.append(j+1)
    if len(tmp_list) == 0:
        new_len2 = len(s1) + len(s2)
    else:
        new_len2 = len(s1) + len(s2) - max(tmp_list2)

    return min(new_len, new_len2)

solution(s1, s2)
