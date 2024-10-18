def solution(array, commands):
    answer = []

    for i, j, k in commands:
        cmd_list = array[i - 1: j - 1 + 1]
        cmd_list.sort()
        answer.append(cmd_list[k-1])

    return answer
