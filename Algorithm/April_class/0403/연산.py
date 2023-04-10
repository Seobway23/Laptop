import sys
sys.stdin = open('input.txt', 'r')

'''
최소 3번이라면 BFS로 접근한다,
'''

from collections import deque
# double ended queue -> 복잡도를 줄이기 위해 deque 사용

def bfs(s,e):
    q = deque()
    v = [0] * 1000001   # 1~ 1000000 범위의 숫자만 가능

    # [2] q에 초기데이터 삽입(단위작업)
    q.append(s)
    v[s] = 1            # 정답 리턴시에는 -1 해서 리턴!

    while q:
        c = q.popleft()
        if c == e:
            return v[e]-1   # 연산 횟수 return

        # 네 방향, 범위내, 미방문, 조건(1~1000000) 맞으면 큐 삽입
        for n in ((c-1), (c+1), (c*2), (c-10)):
            if 1 <= n <= 1000000 and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

    return


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    ans = bfs(N, M)
    print(f"#{test_case} {ans}")