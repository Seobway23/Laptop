'''
cnt를 이용하여 재귀함수로 풀 것
cnt 1

'''
import sys
sys.stdin = open('input.txt', 'r')

def tree(s): #s는 index
    global lst, cnt
    if 0 < s <= N:
        #왼쪽 먼저 실행
        tree(s*2)
        lst[s] = cnt
        cnt += 1
        #그 다음 오른쪽
        tree(s*2 + 1)
    return


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    #초기 값 지정
    lst = [0]*(N+1) #0부터 N까지
    cnt = 1
    tree(1)
    print(f"#{test_case} {lst[1]} {lst[N//2]}")
