import sys
sys.stdin = open('input.txt', 'r')

def babygin(data):
    global ans
    cnt = 0
    A = data[0:3]
    B = data[3:6]

    # 가독성 구분을 쉽게, A와 B로 나눔

    if A[0] == A[1] == A[2]:
        cnt += 1
    elif A[0] +2 == A[1] +1 == A[2]:
        cnt += 1

    if B[0] == B[1] == B[2]:
        cnt += 1

    elif B[0] +2 == B[1] +1 == B[2]:
        cnt += 1

    if cnt == 2:
        #print(data)
        ans = 1


def permute(data, i, length):
    a = babygin(data)
    """
    data: 순열을 만들 숫자 리스트
    i: 현재 조합 중인 숫자의 인덱스
    length: 조합할 숫자의 개수
    """

    for j in range(i, length):
        # i번째 숫자와 j번째 숫자 교환
        data[i], data[j] = data[j], data[i]
        # i+1번째 숫자를 조합
        permute(data, i+1, length)
        # 다시 교환해서 원래대로 돌려놓기
        data[i], data[j] = data[j], data[i]



T = int(input())
for test_case in range(1, T+1):
    data = list(map(int, input()))
    ans = 0
    permute(data, 0, len(data))
    print(f"#{test_case} {ans}")

