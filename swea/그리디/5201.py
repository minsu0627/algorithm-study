# 컨테이너 운반
# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    t = 0
    answer = 0
    for c in containers:
        if t < len(trucks):
            if trucks[t] >= c:
                answer += c
                t += 1
    print(f"#{tc} {answer}")