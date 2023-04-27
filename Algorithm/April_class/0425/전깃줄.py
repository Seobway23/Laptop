import sys
sys.stdin= open('input.txt', 'r')

'''
# 1 dp 배열 인덱스 판별
N = int(input())

# 필요한 배열 선언
lst = []
dp = [0]*(N+1)


# input 받기
for _ in range(N):
    A, B = map(int, input().split())
    lst.append((A, B))

# 오름차순 정렬
lst.sort()

# 2차원 배열 순회
for i in range(N):
    sm = 0
    # 지금 배열과 비교했을 때 크면 sm ++
    for j in range(i, N):
        if lst[i][1] < lst[j][1]:
            sm += 1
    # dp 배열 안에 넣기
    dp[i] = sm

print(N-max(dp))

틀렸음 이유는 모르겠음
'''

# 1 dp 배열 누적합
N = int(input())

# 필요한 배열 선언
lst = []
dp = [0]*(N)


# input 받기
for _ in range(N):
    A, B = map(int, input().split())
    lst.append((A, B))

# 정렬을 안해서 틀렸네 ...
lst.sort()

for j in range(N): # 큰 수
    for i in range(j): # 작은 수
        if lst[i][1] < lst[j][1] and dp[i] > dp[j]:
            dp[j] = dp[i]

    dp[j] += 1

print(N - max(dp))
