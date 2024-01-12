from collections import deque

while True:
    words = input()
    if words == ".":
        break

    first = deque()
    ans = "yes"

    for i in words:
        if i == "(":
            first.append("(")

        if i == "[":
            first.append("[")

        if i == ")":
            if first and first[-1] == "(":
                first.pop()

            else:
                ans = "no"
                break

        if i == "]":
            if first and first[-1] == "[":
                first.pop()

            else:
                ans = "no"
                break

    if first:
        ans = "no"
    print(ans)