vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

while True:
    words = input()
    ans = 0

    # 종료 조건
    if words == "#":
        break

    for i in words:
        if i in vowel:
            ans += 1

    print(ans)
