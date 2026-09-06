from collections import deque

for _ in range(10):
    test_case = int(input())
    password = list(map(int, input().split()))
    queue = deque(password)
    while queue[-1] != 0:
        minus = 1
        for _ in range(5):
            temp = queue.popleft() - minus
            if temp < 0:
                temp = 0
            queue.append(temp)
            minus += 1
            if queue[-1] == 0:
                break
    print(queue)
