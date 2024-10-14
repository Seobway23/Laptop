import collections 

def solution(participant, completion):
    answer = 0
    part = collections.Counter(participant)
    comp = collections.Counter(completion)
    answer = part - comp
    return list(answer.keys())[0]