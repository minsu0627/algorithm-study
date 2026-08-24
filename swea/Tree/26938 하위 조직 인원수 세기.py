T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    org = list(map(int, input().split()))
    entire = [[] for _ in range(E + 2)]
    for i in range(0, len(org), 2):
        boss, worker = org[i], org[i + 1]
        entire[boss].append(worker)
    answer = []

    def dfs(idx):
        answer.append(idx)
        if entire[idx]:
            for num in entire[idx]:
                dfs(num)
        return

    dfs(N)
    print(f"#{test_case} {len(answer)}")

