# (1,1)에서 (N-1.N-1) 탐색하면서 1이 나오면 상하좌우 연결하면서 가능한지 확인
# 맨 처음에 발견한 코어의 상하좌우 중 하나가 연결되면 그걸 기준으로 또 다른 1을 탐색해서 그 코어도 가능한 선을 연결
# dfs 방식으로 쭉 내려가서 우선 연결 다 가능한 것들 연결하고 연결된 코어 수, 전선 길이 업데이트
# 백트레킹 형식으로 초기화하면서 가능한 모든 경우의 수를 체크해서 연결된 코어 수가 가장 많으면서,
# 전선 길이가 가장 짧은 경우를 정답으로 도출

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    processor = [list(map(int, input().split())) for _ in range(N)]
    connected = 0
    length = 0
    for i in range(N):
        for j in range(N):
            if i in (0, N-1) or j in (0, N-1):
                if processor[i][j] == 1:
                    processor[i][j] += 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(1, N-1):
        for j in range(1, N-1):
            if processor[i][j] == 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    while 0 <= nx < N and 0 <= ny < N:
                        if processor[nx][ny] != 0:
                            break
                        else:
                            processor[nx][ny] = -1
                            nx += dx[k]
                            ny += dy[k]

# ============================
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    processor = [list(map(int, input().split())) for _ in range(N)]

    cores = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if processor[i][j] == 1:
                cores.append((i, j))

    result = [0, float('inf')] # 리스트, 딕셔너리는 함수에 인자로 전달하지 않아도 수정이 가능함(global 안 써도 됨)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def dfs(idx, core_cnt, length):
        if core_cnt + (len(cores) - idx) < result[0]: # 가지치기
            return

        if idx == len(cores):
            if core_cnt > result[0]:
                result[0] = core_cnt
                result[1] = length
            elif core_cnt == result[0]:
                if length < result[1]:
                    result[1] = length
            return

        x, y = cores[idx]

        for k in range(4):
            nx, ny = x, y
            possible = True
            count = 0

            while True:
                nx += dx[k]
                ny += dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                if processor[nx][ny] != 0:
                    possible = False
                    break
                count += 1

            if possible:
                # 전선 설치
                nx, ny = x, y
                for _ in range(count):
                    nx += dx[k]
                    ny += dy[k]
                    processor[nx][ny] = 2

                dfs(idx + 1, core_cnt + 1, length + count)
                # 초기화
                nx, ny = x, y
                for _ in range(count):
                    nx += dx[k]
                    ny += dy[k]
                    processor[nx][ny] = 0

        dfs(idx + 1, core_cnt, length)

    dfs(0, 0, 0)

    print(f"#{test_case} {result[1]}")


