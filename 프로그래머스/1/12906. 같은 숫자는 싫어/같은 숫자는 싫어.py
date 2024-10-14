def solution(arr):
    answer = []
    
    pre_num = -1
    for i in arr:
        
        if pre_num == i:
            continue;
        

        answer.append(i)
        # 마지막에 prenum 추가
        pre_num = i 
        

    return answer