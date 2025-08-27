n = int(input())
ans_lst = [i for i in range(1, n * n + 1)]
arr = [[0] * n for _ in range(n)]
likes = {}
for _ in range(n * n):
    idx, *lst = map(int, input().split())
    likes[idx] = sorted(lst)


def search(target):
    # 비어 있는 칸이 가장 많은 칸
    s_lst = []
    # [0]: 인접 갯수, [1]: 비어 있는 칸, [2]: i, [3]: j
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                # 4방향 탐색
                zero, cnt = 0, 0
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni, nj = i +di, j + dj
                    if n > ni >= 0  and 0 <= nj < n:
                        if  arr[ni][nj] == 0: # 0이라면 cnt ++
                            zero += 1
                        else:
                            if arr[ni][nj] in likes[target]:
                                cnt += 1

                s_lst.append((cnt, zero, i, j))
    s_lst.sort(key= lambda x: (-x[0], -x[1], x[2], x[3]))
    return s_lst[0]


# 정답 처리
def ans():
    ans_cnt = 0
    for i in range(n):
        for j in range(n):
            like_cnt = 0
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i + di, j + dj
                if n > ni >= 0 and 0 <= nj < n:
                    # 선호 라면 ?
                    if arr[ni][nj] in likes[arr[i][j]]:
                        like_cnt += 1

            current = 0 if like_cnt == 0 else 10 ** (like_cnt - 1)
            ans_cnt += current
    return ans_cnt

# 배치
for target in list(likes.keys()):
    # 후보 탐색
    cur_cnt, cur_zero, cur_i, cur_j = search(target)
    arr[cur_i][cur_j] = target


# 정답 처리
print(ans())


