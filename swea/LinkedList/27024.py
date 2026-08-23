from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    queue = deque()
    for _ in range(N):
        c, num = map(int, input().split())
        if c == 1:
            queue.appendleft(num)
        else:
            queue.append(num)
    print(queue)