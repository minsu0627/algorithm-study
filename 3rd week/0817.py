# [초기 아이디어]
# 맨 위는 무조건 흰색, 맨 아래는 무조건 빨간색
# 바로 앞이 흰색이면 흰 or 파
# 바로 앞이 파란색이면 파 or 흰
# dfs 형식으로 쭉 내려가서 흰, 파, 빨이 각각 최소 1개 이상이면서 교체 횟수가 적은 게 정답?

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    answer = 0
    color = ['' * N]
    # 맨 위 흰색, 맨 아래 빨간색으로 초기화
    for i in range(M):
        if flag[0][i] != 'W':
            flag[0][i] = 'W'
            answer += 1
        color[0] = 'W'

        if flag[N-1][i] != 'R':
            flag[N-1][i] = 'R'
            answer += 1
        color[N-1] = 'R'
    
    def dfs(idx):
        if idx == N-1:
            return

        if color[idx-1] == 'W':
            flag[idx].count('W')
            flag[idx].count('B')
        elif color[idx-1] == 'B':
            flag[idx].count('B')
            flag[idx].count('R')
    
    def check(answer, temp):
        if color.count('W') >= 1 and color.count('B') >= 1 and color.count('R') >= 1:
            answer = min(answer, temp)
            return answer

# ------------------------
# 구현 못해서 결국 ai한테 물어봄...
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    
    # 각 줄을 W(0), B(1), R(2)로 칠할 때 바꿔야 하는 칸 수를 미리 계산
    cost = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if flag[i][j] != 'W': cost[i][0] += 1
            if flag[i][j] != 'B': cost[i][1] += 1
            if flag[i][j] != 'R': cost[i][2] += 1

    # DFS 함수: idx 줄부터 끝까지 칠할 때 필요한 '최소 교체 횟수'를 반환
    def dfs(idx, prev_color):
        # [종료 조건] 마지막 줄에 도달했을 때
        if idx == N - 1:
            # 파란색을 한 번도 안 거쳤다면 불가능한 경우이므로 무한대 반환
            if prev_color == 0:
                return float('inf')
            # 마지막 줄은 무조건 빨간색(2)이어야 하므로, 해당 비용 반환
            return cost[N-1][2]
        
        # 현재 상태에서의 최솟값을 담을 변수
        min_cost = float('inf')
        
        # 이전 줄의 색상에 따라 뻗어나갈 수 있는 경우의 수 탐색
        if prev_color == 0:
            # 1. 계속 흰색 칠하기
            min_cost = min(min_cost, cost[idx][0] + dfs(idx + 1, 0))
            # 2. 파란색으로 넘어가기
            min_cost = min(min_cost, cost[idx][1] + dfs(idx + 1, 1))
            
        elif prev_color == 1:
            # 1. 계속 파란색 칠하기
            min_cost = min(min_cost, cost[idx][1] + dfs(idx + 1, 1))
            # 2. 빨간색으로 넘어가기
            min_cost = min(min_cost, cost[idx][2] + dfs(idx + 1, 2))
            
        elif prev_color == 2:
            # 1. 계속 빨간색 칠하기 (다른 색으로 넘어갈 수 없음)
            min_cost = min(min_cost, cost[idx][2] + dfs(idx + 1, 2))
            
        return min_cost

    # 0번 줄은 무조건 흰색이므로, 0번 줄을 흰색으로 칠하는 비용 + 1번 줄부터 탐색한 최소 비용
    answer = cost[0][0] + dfs(1, 0)
    
    print(f"#{test_case} {answer}")

#--------------------------------
# 브루트포스가 더 좋은 접근법이라고 함
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    
    # 각 줄을 W, B, R로 칠할 때 몇 칸을 바꿔야 하는지 미리 계산해두면 훨씬 빠르고 편합니다.
    # cost[r][0] = r번째 줄을 전부 흰색(W)으로 바꿀 때 칠해야 하는 횟수
    cost = [[0, 0, 0] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if flag[r][c] != 'W': cost[r][0] += 1
            if flag[r][c] != 'B': cost[r][1] += 1
            if flag[r][c] != 'R': cost[r][2] += 1

    answer = float('inf')
    
    # 파란색이 시작하는 곳과 빨간색이 시작하는 곳 경계만 결정하면 됨
    # i: 파란색이 시작하는 줄 번호 (최소 1부터 시작)
    # j: 빨간색이 시작하는 줄 번호 (최소 i+1부터 시작, N-1까지 가능)
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            
            changes = 0
            
            # 1. 흰색 영역 칠하기 비용 합산 (0 ~ i-1)
            for k in range(0, i):
                changes += cost[k][0]
                
            # 2. 파란색 영역 칠하기 비용 합산 (i ~ j-1)
            for k in range(i, j):
                changes += cost[k][1]
                
            # 3. 빨간색 영역 칠하기 비용 합산 (j ~ N-1)
            for k in range(j, N):
                changes += cost[k][2]
                
            # 최솟값 갱신
            if changes < answer:
                answer = changes
                
    print(f"#{test_case} {answer}")