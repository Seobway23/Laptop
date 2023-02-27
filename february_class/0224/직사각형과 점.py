import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
    x1, y1, x2, y2 = map(int,input().split())
    N = int(input())
    ans1 = 0 #직사각형 내부점의 개수
    ans2 = 0 #직사각형 변 위에 있는 점의 개수
    ans3 = 0 #외부에 있는 점의 개수



    for _ in range(N):
        x, y = map(int, input().split())

        if x1 <= x <= x2 and y1 <= y <= y2: #범위내라면
            if x1 < x < x2 and y1 < y < y2: #내부라면 ans2 증가
                ans1 += 1

            else: #내부가 아니면 모두 선 위에 있으므로
                ans2 += 1

        else:
            ans3 += 1

    print(f"#{test_case} {ans1} {ans2} {ans3}")