def solution(nums):
    answer = 0
    pokets = dict()
    for i in nums:
        # 만약 딕셔너리에 있다면 +1
        if i in pokets.keys():
            pokets[i] += 1
        # 없으면 추가
        else:
            pokets[i] = 1

    answer = min(int(len(nums) / 2), len(pokets.keys()))
    return answer
