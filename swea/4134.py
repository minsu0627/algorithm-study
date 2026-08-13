def check(way):
    answer = 0
    for i in range(N):
        fly = True
        visited = [0] * N
        prev = way[i][0]
        continuous = 1
        for j in range(1, N):
            if abs(way[i][j] - prev) <= 1:
                if way[i][j] < prev:
                    part = way[i][j:j+X]
                    if len(part) == X and len(set(part)) == 1:
                        for k in range(j, j+X):
                            visited[k] = 1
                        continuous = 0
                    else:
                        fly = False
                        break
                elif way[i][j] > prev:
                    if continuous >= X:
                        visited[j] = 1
                        continuous = 0
                    else:
                        fly = False
                        break
                else:
                    if visited[j] == 0:
                        continuous += 1
                        visited[j] = 1
            else:
                fly = False
                break
            prev = way[i][j]
        if fly:
            answer += 1
    return answer

T = int(input())

for test_case in range(1, T+1):
    N, X = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    field_T = list(zip(*field))
    total = check(field) + check(field_T)
    print(f"#{test_case} {total}")

# 가로 순회, 세로 순회(전치로)
# 차이가 1인 경우에만o
# 낮아지는 건 됨 단, X개 이상 연속
# 높아지는 건 이전에 X개 이상 있었을 경우만 가능
# 끝에서 길이 가능한지 체크 필요