words = ['may', 'with', 'may', 'you', 'you']
words = ['one', 'one', 'two', 'one']

def solution(words):
    result = []
    for i in range(len(words)):
        result.append(words.index(words[i])+1)
    return result

solution(words)
