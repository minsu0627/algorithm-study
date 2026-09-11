# 공평한 분배 2
# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pockets = list(map(int, input().split()))
    pockets.sort(reverse=True)
    answer = 10 ** 9 - 1
    for i in range(N-K+1):
        answer = min(answer, (pockets[i] - pockets[i+K-1]))
    print(f"#{tc} {answer}")
