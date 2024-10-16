def solution(n, computers):
    answer = 0
    visit = [False] * n

    def dfs(i):
        visit[i] = True
        for j in range(n):  # 모든 컴퓨터와의 연결을 확인
            if computers[i][j] == 1 and not visit[j]:
                dfs(j)

    for i in range(n):
        if not visit[i]:
            dfs(i)
            answer += 1
    return answer
