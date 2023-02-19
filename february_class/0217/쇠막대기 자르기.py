import sys
sys.stdin=open('input.txt', 'r')

def cnt_pipe(str1):
    stk=[]
    cnt=0

    for i in range(len(str1)): #str을 뽑을 때, 양 옆이 (인지 파악하기 위해 원소가 아닌 인덱스로 접근
        if stk:
            if str1[i-1] == '(' and str1[i] == ')': #레이저라면 stk위에꺼 빼내고 stk길이 더하기
                stk.pop()
                cnt += len(stk)

            elif str1[i-1] == ')'and str1[i] == ')': #레이저가 아니라면, 막대기가 끝나므로, +1만 해주기
                stk.pop()
                cnt += 1
            else:                   # 막대가 시작인 경우, stk에 추가하기
                stk.append(str1[i])

        else: #stk이 없을 때 추가
            stk.append(str1[i])

    return cnt



T=int(input())
for test_case in range(1, T+1):
    str1=input()
    ans=cnt_pipe(str1)
    print(f"#{test_case} {ans}")
