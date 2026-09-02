def dial(temp):
    if len(temp) == D and sum(temp) == S:
        answer[0] += 1
        return

    for n in range(10):
        temp.append(n)
        dial(temp)
        temp.pop()

T = int(input())
for test_case in range(1, T+1):
    D, S = map(int, input().split())
    answer = [0]
    dial([])

    print(f"#{test_case} {answer[0]}")