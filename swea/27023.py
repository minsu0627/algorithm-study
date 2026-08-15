from collections import deque

T = int(input())
for test_case in range(1, T+1):
    M = int(input())
    operators = list(map(int, input().split()))
    queue = deque()
    answer = []
    num = 1
    for o in operators:
        if o == 1:
            queue.append(num)
            num += 1
        else:
            answer.append(queue.popleft())
    print(f"#{test_case}", *answer)
