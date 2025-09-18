def attach(ti, tj, sn, sm, stk):
    for si in range(sn):
        for sj in range(sm):
            if arr[ti + si][tj + sj] == 0:
                arr[ti + si][tj + sj] = stk[si][sj]
    #
    # print("붙입니다.")
    # pprint(arr)
    # print("--------")
    # print()
    return

def rotate(stk):
    # print("idx: ",s_index,  i, j, ", 돌릴 stk",stk)
    # 90도 시계 방향 회전
    new_sn, new_sm = len(stk[0]), len(stk)
    sn, sm = len(stk), len(stk[0])
    rot = [[0] * new_sm for _ in range(new_sn)]
    for ri in range(new_sn):
        for rj in range(new_sm):
            # print(ri, rj, " -> ", rj, new_sm -1 - ri)
            rot[ri][rj] = stk[sn - 1 - rj][ri]

    # print("돌린것:", rot)
    return rot



n, m, k = map(int,input().split())
arr = [[0] * m for _ in range(n)]
stickers = []
for _ in range(k):
    sn, sm = map(int, input().split())
    stk = [list(map(int, input().split())) for _ in range(sn)]
    stickers.append(stk)

for s_index in range(len(stickers)):
    stk = stickers[s_index]
    isAttach = False
    for _ in range(4):
        for i in range(n):
            if isAttach:  break
            for j in range(m):
                if isAttach:  break

                if isAttach:
                    break

                # 범위 안
                cnt = 0
                sn, sm = len(stk), len(stk[0])
                stk_sum = sum(1 for y in range(sn) for x in range(sm) if stk[y][x]== 1 )
                brk =  False
                for si in range(sn):
                    if brk: break
                    for sj in range(sm):
                        #  이미 범위 벗어난 건 걸렀음
                        ni, nj = i + si, j + sj

                        if 0 <= ni < n and 0 <= nj < m:
                            if arr[ni][nj] == 0 and stk[si][sj]:
                                cnt += 1

                        else:
                            brk = True
                            break

                if stk_sum == cnt:
                    # print("스티커,", stk)
                    attach(i, j, sn, sm, stk)
                    # pprint(arr)
                    isAttach=True

        if not isAttach:
            stk = rotate(stk)

# 정답 처리
print(sum(sum(row) for row in arr))