import sys
sys.stdin = open('input.txt')
import math
# input = sys.stdin.readline()
'''
축구를 하기 위해 모인 N명 <- 짝수
N//2 이루어진 스타트 vs 링크 팀 축구 시작

팀의 Aij Aji Bij Bji -> 차이가 가장 작은 것

N은4~20까지,

4명이면 2명을 고르고,
6명이면 3명을 골라야 함,

이 문제에서는 N명일 때 n//2를 무작위로 고르는 방법임
1000 * 1000 -> 100만 -> DFS가능하긴 할 듯
'''
# N//2 고르기
def dfs(cnt, index):
    global ans
    # print(cnt, index)
    # 종료 조건
    if cnt == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N): # 중복 허용 되지 왜냐하면, 0부터 N까지니까
                if visited[i] and visited[j]:
                    start += arr[i][j]

                elif not visited[i] and not visited[j]:
                    link += arr[j][i]
        # print('visited:',visited, 'start:',start, 'link:', link)
        ans = min(ans, abs(start-link))
        return

    for i in range(index, N):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt + 1, i + 1)
            visited[i] = 0

# input 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
ans = math.inf
dfs(0, 0)
print(ans)
