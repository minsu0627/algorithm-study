# 쉬운 거스름돈
# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    money = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}
    for k in money.keys():
        if N == 0:
            break
        money[k] = N // k
        N = N % k
    answer = []
    for k, v in money.items():
        answer.append(v)
    print(f"#{tc}")
    print(*answer)
