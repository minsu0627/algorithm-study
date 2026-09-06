from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    left = deque()
    right = deque()
    mid = (N + 1) // 2
    answer = []
    for i in range(N):
        if i < mid:
            left.append(cards[i])
        else:
            right.append(cards[i])
    print(left, right)
    while left:
        answer.append(left.popleft())
        if right:
            answer.append(right.popleft())
    print(answer)
