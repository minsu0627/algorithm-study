T = int(input())
for test_case in range(1, T+1):
    field = input()
    stack = []
    prev = ''
    answer = 0
    for f in field:
        if f == '(':
            stack.append(f)
        elif f == ')':
            if prev == '(':
                stack.pop()
                answer += 1
            else:
                answer += 1
        prev = f
    answer += len(stack)
    print(f"#{test_case} {answer}")