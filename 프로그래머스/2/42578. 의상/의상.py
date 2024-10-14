def solution(clothes):
    names = dict()
    ans = 1
    for cloth, name in clothes:
        # 있으면 추가
        if name in list(names.keys()):
            names[name].append(cloth)
        # 없으면 만들기
        else:
            names[name] = [cloth]

    for i in list(names.keys()):
        ans *= (len(names[i]) + 1)

    ans -= 1
    return ans