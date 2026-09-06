# 출근 카풀 그룹 나누기
import sys
sys.stdin = open("input.txt", "r")

def check(node):
    visited[node] = True

    for n in graph[node]:
        if not visited[n]:
            check(n)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    submit = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]

    for i in range(0, M*2, 2):
        a, b = submit[i], submit[i+1]
        graph[a].append(b)
        graph[b].append(a)

    answer = 0
    visited = [False] * (N+1)

    for g in range(1, N+1):
        if not graph[g]:
            answer += 1
            continue

        if not visited[g]:
            check(g)
            answer += 1
    print(f"#{tc} {answer}")
