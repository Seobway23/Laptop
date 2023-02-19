'''
# 문자열 패딩하는 방법
arr= ['.'*(N+2)]+list( input() for _ in range(N))+['.'*(N+2)]

'''

# 앞으로 이동하는 것 -> 델타검색 비슷함


import sys
sys.stdin=open('input.txt', 'r')

def find_OX(arr):
    #가능한 모든 기준 위치를 순회
    for si in range(1,N+1):
        for sj in range(1,N+1):
            #4방향, 뻗어가면서 확인
            for di,dj in ((-1,-1),(0, 1),(1, 1),(1, 0)):
                cnt=0
                for mul in range(5):
                    cnt +=1
                    ni, nj=si+di*mul, sj+dj*mul
                    if arr[ni][nj] != 'o':
                        break

                if cnt==5:
                    return 'YES'

    return 'NO'




T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr= ['.'*(N+2)]+list( input() for _ in range(N))+['.'*(N+2)]
    ## 숫자열과 문자열을 패딩하는 방법


    print(f"#{test_case} {find_OX(arr)}")