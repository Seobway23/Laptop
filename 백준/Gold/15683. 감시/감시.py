
def cal(tlst):
    v = [[0] * m for _ in range(n)]
    for k in range(len(tlst)):
        rot = tlst[k]
        si, sj = lst[k]
        cur_cctv = cctv[arr[si][sj]]

        for cur_dir in cur_cctv:
            next_dir = (cur_dir + rot) % 4

            ni, nj = si, sj
            while True:
                ni, nj = ni + dir[next_dir][0], nj + dir[next_dir][1]
                # 범위내
                if 0 <= ni < n and 0 <= nj < m:
                    if arr[ni][nj] == 6:
                        break
                    v[ni][nj] = 1

                else:
                    break


    ans = sum(1 for j in range(m) for i in range(n) if not arr[i][j] and not v[i][j])
    return ans

def dfs(index, tlst):
    global ans
    # 종료 조건
    if index == len(lst):
        ans = min(ans, cal(tlst))
        return

    # dfs
    dfs(index + 1, tlst + [0])  #   0도 회전
    dfs(index + 1, tlst + [1])  #  90도 회전
    dfs(index + 1, tlst + [2])  # 180도 회전
    dfs(index + 1, tlst + [3])  # 270도 회전

# input
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# init
ans = m * n
dir = ((-1, 0), (0, 1), (1, 0), (0, -1))    # 0상 1우 2하 3좌
cctv = [[], [1], [1, 3], [0, 1], [0, 1, 3], [0, 1, 2, 3]]
rot = [0, 1, 2, 3]  # 0도, 90도, 180도, 270도
lst = [(i, j ) for j in range(m) for i in range(n) if 0 < arr[i][j] < 6]

# main loop
dfs(0, [])  # index, temp_list
print(ans)