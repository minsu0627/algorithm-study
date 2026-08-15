from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    field = [list(map(int, input())) for _ in range(N)]
    mid = N // 2
    visited = [[False]*N for _ in range(N)]
    
    queue = deque([(mid, mid, 0)])
    visited[mid][mid] = True
    answer = field[mid][mid]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0,- 1]

    while queue:
        x, y, dist = queue.popleft()

        if dist == mid:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                answer += field[nx][ny]
                queue.append((nx, ny, dist+1))

    print(answer)