T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time = sorted(list(map(int, input().split())))
    calc = [0] * N

    for i in range(1, N):
        calc[i] = calc[i - 1] + time[i - 1]
    print(f"#{tc} {sum(calc)}")