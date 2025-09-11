n, m, K = map(int, input().split())
fireballs = [list(map(int, input().split())) for _ in range(m)]
# r, c, m, s, d
# i, j, 질량, 방향, 속력
# r, c 가 지금 1,1 시작 이라 -1씩 해줘야 함
# 0 -> N과 연결 % n 하면 될 듯
# odd, even -> 방향을 기준으로
arr = [[[] for _ in range(n)] for _ in range(n)]

# dir
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for i, j, m, s, d in fireballs:
    arr[i-1][j-1].append([m, s, d])



time = 0
while time < K:
    # pprint(arr)
    # print("time:", time, ", k:", K)
    # 복사 배열
    new_arr = [[[] for _ in range(n)] for _ in range(n)]

    # print("현재")
    # pprint(arr)
    # 볼 이동
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                # 질량, 속력,  방향
                for m, s, d in arr[i][j]:
                    ni = (i + dir[d][0] * s + n) % n
                    nj = (j + dir[d][1] * s + n) % n


                    # 갱신
                    new_arr[ni][nj].append((m, s, d))

    # print("갱신")
    # pprint(new_arr)
    # 순회 돌면서 2개 이상 찾기
    for i in range(n):
        for j in range(n):
            if len(new_arr[i][j]) > 1: # 2 이상일 때
                even, odd = 0, 0
                odd_flag = 0

                # [0]: 질량, [1]: 속력, [2]: 방향
                for target in new_arr[i][j]:

                    # 방향을 기준
                    if  target[2] % 2 == 0:
                        even += 1
                    else:
                        odd += 1

                # even or odd 일 때
                if even == 0 or odd == 0:
                    odd_flag = 0

                else:
                    odd_flag = 1

                # m, s 갱신
                next_m, next_s = 0, 0
                for m, s, d in new_arr[i][j]:
                    next_m += m
                    next_s += s

                next_m = next_m // 5
                next_s = next_s // len(new_arr[i][j])

                # 초기화 후 next_m 이 0보다 크면 4개 쪼개서 넣기
                new_arr[i][j] = []

                if next_m > 0:
                    for k in range(4):                    # m, d, s
                        new_arr[i][j].append((next_m, next_s,  2 * k + odd_flag))


    # pprint(new_arr)

    # time + 1
    time += 1
    arr = new_arr


ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            for tar in arr[i][j]:
                ans += tar[0]

print(ans)