T = int(input())
for test_case in range(1, T+1):
    sticks = list(input())
    answer = 0
    stack = []
    prev = ''
    for s in sticks:
        if s == "(":
            stack.append(s)
        else:
            stack.pop()
            if prev == "(":
                answer += len(stack)
            else:
                answer += 1
        prev = s
    print(f"#{test_case} {answer}")