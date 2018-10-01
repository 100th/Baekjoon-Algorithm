a = int(input())

zero = [1,0,1]
one = [0,1,1]

def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[num],one[num]))

for i in range(a):
    k = int(input())
    cal(k)


# n = int(input())
#
# input_num = []
# for i in range(n):
#     input_num.append(int(input()))
#
# def fibonacci(num):
#     if num == 0:
#         one_zero[0] += 1
#     elif num == 1:
#         one_zero[1] += 1
#     else:
#         fibonacci(num-1)
#         fibonacci(num-2)
#
# for i in range(n):
#     one_zero = [0, 0]
#     fibonacci(input_num[i])
#     print(one_zero[0], one_zero[1])
