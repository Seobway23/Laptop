def hanoi(n, start, via, end, ans):
    # 종료 조건
    if n == 1:
        ans.append(f"{start} {end}")
        return
    # dfs 돌리기


    hanoi(n-1, start, end , via, ans)
    ans.append(f"{start} {end}")
    hanoi(n-1, via, start, end, ans)
    return


n = int(input())
ans = []
hanoi(n, 1, 2, 3, ans)
print(len(ans))
print("\n".join(ans))