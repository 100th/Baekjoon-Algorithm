import sys
from collections import Counter

nBox = []
sum, avg, mid, mod, ran = 0,0,0,0,0

def avgFinder(nBox):
    sum , avg = 0,0
    for i in range(0, len(nBox)):
        sum += nBox[i]
    avg = sum/len(nBox)
    return round(avg)

def midFinder(nBox):
    nBox.sort()
    mid = nBox[len(nBox)//2]
    return mid

def modFinder(nBox):
    cntDic = Counter(nBox)
    cntTpl = cntDic.most_common()
    # print(cntTpl)
    if len(nBox) > 1:
        if cntTpl[0][1] == cntTpl[1][1]:
            mod = cntTpl[1][0]
        else:
            mod = cntTpl[0][0]
    else:
        mod = cntTpl[0][0]

    return mod

def ranFinder(nBox):
    ran = nBox[len(nBox)-1] - nBox[0]
    return ran

n = int(sys.stdin.readline())

for i in range(0, n):
    inNum = int(sys.stdin.readline())
    nBox.append(inNum)

print(avgFinder(nBox))
print(midFinder(nBox))
print(modFinder(nBox))
print(ranFinder(nBox))
