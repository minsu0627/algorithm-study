# 그룹 나누기
# import sys
# sys.stdin = open('input.txt', 'r')

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    root_x = find(parents, x)
    root_y = find(parents, y)
    if root_x != root_y:
        parents[root_y] = root_x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    submissions = list(map(int, input().split()))
    parents = [i for i in range(N+1)]
    for i in range(0, M*2, 2):
        a, b = submissions[i], submissions[i+1]
        union(parents, a, b)
    groups = 0
    for i in range(1, N+1):
        if find(parents, i) == i:
            groups += 1
    print(f"#{tc} {groups}")