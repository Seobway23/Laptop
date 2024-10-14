def solution(participant, completion):
    # dict
    lift = dict()
    answer = ''

    for i in completion:
        # 있으면 1 추가
        if i in lift.keys():
            lift[i] += 1
        # 없으면 추가
        else:
            lift[i] = 1

    for i in participant:
        if i in lift.keys():
            lift[i] -= 1

            if lift[i] == 0:
                lift.pop(i)

        else:
            answer = i

    return answer