phrases = 'happy-birthday'
second = 56

def solution(phrases, second):
    if second >= 29:
        second = second % 28

    mystring = '______________' + phrases + '______________'
    return mystring[second:second+14]

solution(phrases, second)
