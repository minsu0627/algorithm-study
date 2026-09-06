from collections import deque

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    subway = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        subway[a].append(b)
        subway[b].append(a)

    S, G = map(int, input().split())

    queue = deque([(S, 0)])
    visited = [False] * (V+1)
    visited[S] = True

    answer = 0

    while queue:
        cur, count = queue.popleft()

        if cur == G:
            answer = count
            break

        for nxt in subway[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, count+1))

    print(f"#{test_case} {answer}")



