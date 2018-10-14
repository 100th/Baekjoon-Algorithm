estimates = [1, 1, 9, 3, 7, 6, 5, 10]
k = 4

estimates = [1, 1, 5, 1, 1]
k = 1

def solution(estimates, k):
    # tmp_list = []
    max = 0
    for i in range(len(estimates)-k+1):
        if sum(estimates[i:i+k]) > max:
            max = sum(estimates[i:i+k])
        # tmp_list.append(sum(estimates[i:i+k]))

    return max


solution(estimates, k)
