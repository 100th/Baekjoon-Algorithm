# 조합 계산을 위한 팩토리얼 정의
def facto(n):
    a = 1
    for i in range(n):
        a = a * (i+1)
    return(a)

T = int(input())

for i in range(T):
    d, e  = map(int,input().split(' '))

    # 입력된 두 수 중 하나라도 0이 되면 0을 리턴
    if e == 0 :
        print(0)
    # 아닐 경우 조합(eCd)를 계산
    else:
        e_fact = int(facto(e))
        d_fact = int(facto(d))
        e_d_fact = int(facto(e-d))

        # 나눗셈에 /이 아닌 //을 사용!!!
        print(int(e_fact // d_fact // e_d_fact))
