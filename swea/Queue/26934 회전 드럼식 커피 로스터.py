from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    baskets = list(map(int, input().split()))
    spaces = deque([[i, baskets[i-1]]for i in range(1, N+1)])
    lefts = deque([[i, baskets[i-1]]for i in range(N+1, M+1)])
    
    while True:
        temp = spaces.popleft()
        temp[1] = int(temp[1] / 2)
        if temp[1] == 0:
            if lefts:
                spaces.append(lefts.popleft())
        else:
            spaces.append(temp)

        if len(spaces) == 1:
            break
    print(spaces[0][0])