# 쇠막대기 자르기

T = int(input())
for tc in range(1, T+1):
    sticks = input()
    stack = []
    prev = ''
    answer = 0
    for s in sticks:
        if s == '(':
            stack.append(s)
        else:
            if prev == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1
        prev = s
    print(f"#{tc} {answer}")



