def zz(N, r, c):
    answer = 0
    size = 2 ** N
    while size > 1:
        size //= 2
        # 4등분된 영역 중 어디에 속하는지 확인
        if r < size and c < size:  # 1사분면
            pass  # 아무것도 안함 (첫 번째 방문)
        elif r < size and c >= size:  # 2사분면
            answer += size * size  # 첫 번째 영역의 크기만큼 더함
            c -= size  # 열의 위치 업데이트
        elif r >= size and c < size:  # 3사분면
            answer += size * size * 2  # 첫 번째, 두 번째 영역의 크기만큼 더함
            r -= size  # 행의 위치 업데이트
        else:  # 4사분면
            answer += size * size * 3  # 세 영역의 크기만큼 더함
            r -= size  # 행의 위치 업데이트
            c -= size  # 열의 위치 업데이트
    return answer


n, r, c = map(int, input().split())
print(zz(n, r, c))
