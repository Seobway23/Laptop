'''
1. 미로 N X N/ 위치(r,c) [i][j]
2. 미로의 각 칸
- 빈칸 -> 이동 가능
- 벽 : 이동 X
    회전할 때 1씩 깎임
    내구도가 0이되면 빈칸
- 출구 : 해당칸에 도달하면 즉시 탈출



3. 참가자
- 최단거리:  좌표의 차이
- 모든 참가자 동시에 이동
- 상하좌우 이동 가능, 벽 아닌 곳으로 이동
- 출구의 최단거리와 가까워야 함
- 상하 움직임 우선
- 참가자끼리 중복 가능

di = [-1, 1, 0, 0]
dj = [0,0, -1, 1]

4. 회전
- 한명 이상의 참가자와 출구를 포함한 가장 작은 배열 잡음
- 가장 잡은 배열이 2 이상이라면 -> r, c 순 가장 작은 것(위쪽, 왼쪽)
=> 출구와 참가자의 배열의 거리값이 됨
=> sorted( 리스트, labmda x: (x[0],x[1],x[2])) # 거리, row, culomn
'''
import sys
import copy
sys.stdin = open('input.txt')
# 방향 / 상 하 좌 우
di, dj = [-1, 1, 0, 0], [0,0, -1, 1]


# input
# N 배열 수, M 참가자 수, K 게임 시간
N, M, K = map(int, input().split())

#미로  0이면 빈칸, 1~9 내구도
arr = [list(map(int, input().split())) for _ in range(N)]
# print('arr:', arr)

# # 참가자 좌표 - 리스트로 받는 방법
# participate = []
# print(participate)
# for _ in range(M):
#     # A, B = map(int, input().split())
#     participate.append(list(map(int, input().split())))
# print(participate)

# 참가자 좌표 배열로 받기
part = [[0]*N for _ in range(N)]
for _ in range(M):
    pi, pj = map(int, input().split())
    # 0,0이 아닌 1,1이 시작이기 때문에
    part[pi-1][pj-1] = 1

exit_i, exit_j = map(int, input().split())
ei, ej = exit_i -1, exit_j -1

# 움직임 조건 -> 출구 방향으로 한칸씩 이동
# 최단거리는 출구와 위치의 최단 거리


def flag_func(part):
    for iii in range(N):
        for jjj in range(N):
            if part[iii][jjj]:
                flag = True
                return flag

def move(si, sj):
    global ei, ej, ans
    # 초기값  이동할 distance, dir
    distance = 10000
    dir = 10

    # 1.거리재기
    for idx in range(4):
        ni, nj = si + di[idx], sj + dj[idx]
        # 범위내
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                dist = abs(ei-ni) + abs(ej-nj)

                # 자연스럽게 상하좌우 순
                if dist < distance:
                    distance = dist
                    dir = idx

    # 2 이동 거리 반환
    next_i, next_j = si + di[dir], sj + dj[dir]
    ans += 1
    return distance, next_i, next_j


def square(ri, rj):
    global ei, ej
    # 변이니까 +1 해야 함
    side_len = max(abs(ri-ei)+1, abs(rj-ej)+1)
    squre_arr = [[0]*side_len for _ in range(side_len)]
    # deepcopy를 쓰거나, 새로 만들어준다,
    part_arr = [[0]*side_len for _ in range(side_len)]

    # print('side_len:', side_len)
    # print('squre_arr:', squre_arr)
    # print('part_arr:', part_arr)

    for i in range(N):
        for j in range(N):
            # 가장 위, 가장 왼쪽에 있는 정사각형 찾기
            dot_cnt = 0
            # print('side_len:', side_len)
            for ki in range(i, i + side_len):
                for kj in range(j, j + side_len):
                    # print('ki:', ki, 'kj:', kj, 'ri:', ri, 'rj:', rj)

                    d= i; dd = j; ddd=ki; dddd=kj
                    if ki == ri and kj == rj:
                        dot_cnt += 1

                    elif ki == ei and kj == ej:
                        dot_cnt += 1

                    if dot_cnt == 2:
                        for ni in range(i,ki+1):
                            for nj in range(j, kj + 1):
                                print('ni:', ni, 'nj:', nj)
                                part_arr[ni][nj] = part[ni][nj]
                                squre_arr[ni][nj] = arr[ni][nj]

                        return squre_arr, part_arr, i, ki, j, kj


def rotate(squre_arr, part_arr):
    global zi, ni, zj, nj
    # print('squre:', squre_arr,'part:',part_arr)
    num = len(squre_arr)
    # print('len_i:', len_i, 'len_j:', len_j)

    dummy_arr = [[0] * (num) for _ in range(num)]
    dummy_part= [[0] * (num) for _ in range(num)]
    print(dummy_arr,'&&&',dummy_part)


    # 회전하기 -> 덮어쓰기
    for i in range(num):
        for j in range(num):
            # 만약 벽이 있다면,
            if squre_arr[i][j]:
                squre_arr[i][j] -= 1

            dummy_part[j][num - 1 - i] = part_arr[i][j]
            dummy_arr[j][num - 1 - i] = squre_arr[i][j]

    # print(squre_arr)
    # print(part_arr)
    # print(dummy_arr)
    # print(dummy_part)
    for i in range(zi, zi + num):
        for j in range(zj, zj + num):
            part[i][j] = dummy_part[i-zi][j-zj]
            arr[i][j] = dummy_arr[i-zi][j-zj]

    print(part)




# top_down 시작

ans = 0
flag = True
while flag:
    flag = False
    # 1. 참가자 이동 시작
    part_move = []
    for i in range(N):
        for j in range(N):
            if part[i][j]:
                part_move.append([i, j])

    next_position = []
    for ii, jj in part_move:
        dist, ni, nj = move(ii, jj)

        # 탈출 조건
        if ni == ei and nj == ej:
            continue

        # 움직임 갱신
        part[ii][jj] -= 1
        part[ni][nj] += 1

        # dist, next_i, next_j 파악
        next_position.append([dist, ni, nj])

    # 가장 가까운 참가자 찾기
    next_position.sort(key=lambda x: (x[0], x[1], x[2]))
    ri, rj = next_position[0][1:]

    # print('part:', part)
    # 2. 회전 시작
    # 회전을 위한 최소 정사각형을 구해야 함// part, arr를 따로 둠
    squre_arr, part_arr, zi, ni, zj, nj = square(ri, rj)
    rotate(squre_arr, part_arr)

    # print(next_position)

    # rotate 함수 / 이동을 했으니 회전 해야 함
    flag = flag_func(part)




