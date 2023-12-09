def solution(ci, cj, cd):
    global ans
    while True:
        # 현재 위치 방문, 표시
        arr[ci][cj] = 2
        ans += 1

        not_exit = True
        t = 0
        while not_exit:
            t += 1
            # 반시계 -1 씩 감소
            for k in ((cd + 4 - 1) % 4, (cd + 4 - 2) % 4, (cd + 4 - 3) % 4, (cd + 4 - 4) % 4):
                bd = k
                # print("t번째:", t, " ,방향:", bd, " ,k:", k, ", cd:", cd)
                ni, nj = ci + di[bd], cj + dj[bd]

                # 만약 청소 X 라면
                if arr[ni][nj] == 0:
                    ci, cj, cd = ni, nj, k
                    # pprint(arr)
                    not_exit = False
                    break

            # 청소를 했다면 back
            else:
                # 반시계 방향으로 90도 회전
                bi, bj = ci - di[cd], cj - dj[cd]

                # 벽이라면 return
                if arr[bi][bj] == 1:
                    return

                # 벽이 아니라면
                else:
                    ci, cj = bi, bj



# [0]:북, [1]: 동, [2]: 남, [3]: 서
di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

# input 받기
n, m = map(int, input().split())
si, sj, dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 필요 자료 구조
ans = 0


solution(si, sj, dr)
print(ans)