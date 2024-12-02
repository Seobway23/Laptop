def rotate(si, sj):
    new_lst = []
    v = [[0] * n  for _ in range(n)]

    # 나선 구조 순회
    s_dir = ((0, -1), (1, 0), (0, 1), (-1, 0)) # 방향
    # sd: 인덱스, s_num: 나선 크기, flag : 나선+ 플래그
    sd, s_num, flag = 0, 0, -1
    while True:
        flag += 1
        # 종료 조건
        if si < 0 or sj < 0:
            break

        if flag % 2 == 0:
            s_num += 1

        for k in range(1, s_num + 1):
            ni, nj = si + s_dir[sd][0] * k, sj + s_dir[sd][1] * k
            if 0 <= ni < n and 0 <= nj < n:
                new_lst.append((ni, nj))
                v[ni][nj] = s_num

        # 방향 추가
        sd = (sd + 1 ) % 4
        # 현재 상태 갱신
        si, sj = ni, nj
    return new_lst

def bomb(lst):
    global ans
    new_lst = []
    i = 0

    # 터치는거 보이면 -> 처음부터 다시 시작
    while i  < len(lst):
        num = lst[i]

        # 4개 이상일 때
        cnt = [1 for row in lst[i: i + 4] if row == num]
        if num != 0 and len(cnt) == 4:
            ans += (num * 3)
            i += 3
            # 4개 이상 처리
            while i  < len(lst):
                if num == lst[i]:
                    i += 1
                    ans += num

                else:
                    break
        else:
            new_lst.append(lst[i])
            i += 1
    return new_lst

def changes(lst):
    new_lst = []
    i = 0
    while i < len(lst)-1:
        if lst[i] == lst[i+1]:
            # 몇개가 같은 지 확인
            num, cnt = lst[i], 1
            while True:
                if lst[i] == lst[i + 1]:
                    cnt += 1
                    i += 1
                else:
                    i += 1
                    break

            # new_lst Add
            new_lst.append(cnt)
            new_lst.append(num)

        else:
            num, cnt = lst[i], 1
            # new_lst Add
            new_lst.append(cnt)
            new_lst.append(num)
            i += 1

    return new_lst

# init
n, m = map(int, input().split())
ci, cj = n //2, n//2
arr = [list(map(int, input().split())) for _ in range(n)]
blizards = [list(map(int, input().split())) for _ in range(m)]
# [1]: 원점, [1]: ↑, [2]: ↓, [3]: ←, [4]: →
dir = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
spiral_lst = rotate(ci, cj)
ans = 0

# 마법 실행, M 번 동안
for d, s in blizards:
    # 1. 블리자드 마법
    for k in range(1, s + 1):
        ni, nj = ci + dir[d][0] * k, cj + dir[d][1] * k
        arr[ni][nj] = 0

    # 나선 구조 리스트 갱신 => 0
    new_lst = []
    for i, j in spiral_lst:
        if arr[i][j] > 0:
            new_lst.append(arr[i][j])

    # 폭발 처리
    bomb_lst = bomb(new_lst)

    # 폭발 재귀 처리
    while True:
        flag = 0
        for i in range(len(bomb_lst)):
            cnt = [1 for row in bomb_lst[i: i + 4] if row == bomb_lst[i]]
            if len(cnt) == 4:
                flag = 1
                bomb_lst = bomb(bomb_lst)
                break

        if flag == 0:
            break
    # print("전: ", bomb_lst)

    # A, B 그룹 변하기
    cng_lst = changes(bomb_lst + [0])

    # arr 에 매칭하기
    new_arr = [[0] * n  for _ in range(n)]
    for k in range(len(cng_lst)):
        if k < n ** 2 - 1:
            i, j = spiral_lst[k][0], spiral_lst[k][1]
            new_arr[i][j] = cng_lst[k]

    arr = new_arr
    # print("후: ", cng_lst)

print(ans)