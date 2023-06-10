import sys
sys.stdin = open('input.txt')
'''
1. 포탑
배열은 모두 포탑, 0인 경우도 포탑으로 가정하고 -> 0이면 바로 부서짐 => 그냥 0이면 X

2. 하나의 턴
@ 공격자
1) 선정
- 가장 약한 포탑이 공격자로 선정/ 공격력 + (N + M)
- 선정 기준 : sorted (i + j , j)
    (행과 열이 가장 큰 포탑 -> 이마저도 같다면 열값이 가장 큰 포탑 j값)

2) 공격
- 자신을 제외한 가장 강한 포탑 공격
- 선정 기준: sorted(공격력, 공격한지 오래된 포탑, i + j , j)
    (포탑의 공격력, 공격오래된 포탑, 행+열, 열)

* 레이저 공격
- arr값이 0인 부분은 지날 수 없음
- 막히면 반대편으로 나옴
- 최단 경로 -> 우/ 하/ 좌/ 상 -> 먼저 발견하면 끝 경로값 작으면 갱신

    # 공격 받은 포탑의 공격력 감소
- 공격받은 포탑 -= 공격한 포탑의 공격력
- 경로에 있는 포탑 -= 공격력//2

* 포탄 공격
- 공격받은 포탑 -= 공격한 포탑의 공격력
- 주위 8방향 포탑 -= 공격력 // 2
- 가장자리라면 -> 반대 격자에 미치게 됨 -> '% 이용할 것'

3. 포탑 정비
- 공격에 무관한 포탑 += 1
포탑visited => 공격시작시 마다 갱신
공격 무관 0 이면 -> arr[i][j] += 1

<범위>
N, M 은 4 이상 10 이하
k 는 1000이하
공격력 5000 이하

* 출력
K 번 턴 후 종료된 남아있는 포탑 중 가장 강력한 포탑 공격력 출력
'''
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
atk_record = [[1] * M for _ in range(N)]

# 방향 우, 하, 좌, 상
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


# 1 공격 타워 선택
def select_tower(arr):
    atk= 5001
    atk_lst = []
    # 공격자 선택 기준, tower 낮은 순, i j 높은 순
    for i in range(N):
        for j in range(M):
            # not은 쓰지 않는다,
            if arr[i][j] <= atk and arr[i][j] != 0:
                # 0 공격력 오름, 1 최근기록 내림, 2 행 + 열, 3 행, 4 열
                atk_lst.append([arr[i][j], atk_record[i][j], i+j, i, j])

    atk_lst = sorted(atk_lst, key=lambda x: (x[0], -x[1], -x[2], -x[3]))
    print('atk_lst:',atk_lst)
    return atk_lst[0][3], atk_lst[0][4]


# bfs  ->
def laser(ai, aj, ei, ej):
    # bfs를 이용해서 타워의 레이저 범위 찾기/ 우, 하, 좌, 상
    flag = 0
    laser_path_lst = []
    idx, bfs_num = 0, 0 # idx 방향 인덱스, bfs_num 탈출 숫자
    while bfs_num <= N*M:
        ni, nj = ai + di[idx], aj + dj[idx]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] !=0:
            ai, aj = ni, nj
            laser_path_lst.append([ai, aj])
            idx = 0
            # 종료 조건
            if ai == ei and aj == ej:
                flag = 1
                break
        else:
            idx = (idx+1) % 4
            bfs_num += 1

    # 경로에 도달 하지 못하면, 리스트 비우기
    if flag == 0:
        laser_path_lst = []

    return laser_path_lst


# 2 타워 공격
def attack_tower(ai, aj, arr, atk_power):
    # *중요한 것 / 공격 하거나 맞으면 visited 방문 표시*

    # 2-1 공격할 타워 선정
    best_atk_tower = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                # 0 공격력 오름차순, 1 오름차순, 2 내림차순, 4 오름차순
                best_atk_tower.append([arr[i][j], atk_record[i][j], i+j, i, j])

    atk_tower_list = sorted(best_atk_tower, key=lambda x: (-x[0], x[1], -x[2], x[4]))
    # return 공격할 타워 좌표 ei, ej
    ei, ej = atk_tower_list[0][3], atk_tower_list[0][4]

    # 2-2 레이저 or 포탑
    laser_lst=laser(ai, aj, ei, ej)
    if len(laser_lst) != 0: # 레이저 공격 시작!!!!
        # 2-2-1 경로에 있는 타워 공격력 감소, 마지막 타워는 타겟 타워 이므로 제외
        for li, lj in laser_lst[:-1]:
            arr[li][lj] -= atk_power//2
            visited[li][lj] = 1
            if arr[li][lj] < 0:
                arr[li][lj] = 0

    else:   # 포탑 공격 시작!!!!
        '''
        * 포탄 공격
        - 공격받은 포탑 -= 공격한 포탑의 공격력
        - 주위 8방향 포탑 -= 공격력 // 2
        - 가장자리라면 -> 반대 격자에 미치게 됨 -> '% 이용할 것'
        '''

        ddi, ddj = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
        for idx in range(8):
            bi, bj = (ei + ddi[idx]) % N, (ej + ddj[idx]) % M
            if arr[bi][bj]:
                # print(idx+1,'번째','bi:', bi, 'bj:', bj, 'ei:',ei, 'ej:', ej)
                arr[bi][bj] -= atk_power//2
                visited[bi][bj] = 1

    print(arr)
    # 2-3 타겟 타워의 공격력 감소
    visited[ei][ej] = 1
    arr[ei][ej] -= atk_power
    return


# 3 포탑 정비
def visited_tower(arr, visited):
    for vi in range(N):
        for vj in range(M):
            if visited[vi][vj] == 0 and arr[vi][vj]!=0:
                arr[vi][vj] += 1


# K 번 움직임 시작
for kkkk in range(K):
    # visited 공격 참여 테이블
    visited = [[0] * M for _ in range(N)] # 턴이 시작할 때마다 갱신

    # 1 공격자 선정
    attack_i, attack_j = select_tower(arr)
    visited[attack_i][attack_j] = 1 # visited 방문 표시
    atk_record[attack_i][attack_j] += 1 # 공격 기록
    print('#1:', attack_i, '#2:', attack_j )
    # 1-1 공격자 공격력 증가
    arr[attack_i][attack_j] += (N + M)
    atk_power = arr[attack_i][attack_j]
    print( kkkk, '번쨰', atk_power)
    # 2 공격 ( 레이저, 포탄)
    attack_tower(attack_i, attack_j, arr, atk_power)

    # 3 포탑 정비
    visited_tower(arr, visited)

    print(arr)

# 4 K 턴 종료 후 남아 있는 포탑 중 가장 강한 포탑의 공격력
ans = 0
for i in arr:
    A = sorted(i, reverse=True)
    if A[0] > ans:
        ans = A[0]
print('ans:', ans)