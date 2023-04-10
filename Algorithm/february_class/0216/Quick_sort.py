import sys
sys.stdin=open('input.txt', 'r')

def qsort(lst):

    # 0 종료 조건: 정렬할 요소가 1개라면 종료!
    if len(lst)<2:
        return lst #return 뒤에 lst를 안놔서

    p=lst.pop()
    left=[]
    right=[]
    #1 단위 작업, p를 기준으로 좌/우로 분리!
    for i in lst:
        if i < p:
            left.append(i)

        else:
            right.append(i)

    # 2 왼쪽 정렬한 결과 + p + 오른 쪽 정렬한 결과
    return qsort(left) + [p] + qsort(right)



T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    alst=qsort(lst)
    ans=alst[N//2]
    print(f"#{test_case} {ans}")