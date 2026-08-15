# 문제 : 농작물 수확하기
# 아이디어
# 가운데 인덱스 계산해서 행 번호가 mid랑 같아질 때까지 왼쪽으로 -1, 오른쪽으로 +1 하면서 합
# mid보다 커지면 왼쪽은 +1, 오른쪽은 -1 하면서 합

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    field = [list(map(int, input())) for _ in range(N)]
    mid = N // 2
    gap = 0
    answer = 0
    for i in range(N):
        if i <= mid:
            gap += 1
            answer += sum(field[i][mid-gap+1:mid+gap])
        else:
            gap -= 1
            answer += sum(field[i][mid-gap+1:mid+gap])
    print(f"#{test_case} {answer}")
    
# 시간복잡도 : N 순회 -> O(N), sum과 슬라이싱 -> O(N) + O(N) = O(2N) -> O(N)
# O(N) * O(N) = O(N^2)

# 알고리즘에 큐로 분류되어 있는데 큐로 어떻게 접근해야할지 떠오르지 않아 gemini 통해 알아낸 방식
# (mid, mid)를 기준으로 상하좌우 탐색 -> 중앙과 거리가 mid보다 커지면 stop

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

    print(f"#{test_case} {answer}")