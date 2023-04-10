import sys
sys.stdin= open('input.txt', 'r')

def electric_station(index, charge, cnt):
    global N, lst, ans
    print('cnt:', cnt, 'index:', index, 'charge:', charge)
    #종료 조건
    if index > N:
        return

    #return 조건
    if index + charge >= N-2:
        ans += cnt
        return

    #그러면 charge 범위내에서 가장 큰 거 고르면 될 듯
    v = []
    for i in range(1, charge+1):
        v.append((lst[index+i],index + i))

    v.sort()

    electric_station(v[-1][1], v[-1][0], cnt + 1)


T= int(input())
for test_case in range(1, T+1):
    N, *lst = map(int, input().split())
    ans = 0
    electric_station(0, lst[0], 0)
    print(f"#{test_case} {ans}")