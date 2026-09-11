# 창용 마을 무리의 개수
# import sys
# sys.stdin = open('input.txt', 'r')

def find(x):
    if parents[x] == x:
        return x
    return find(parents[x])

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parents[root_y] = root_x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    answer = set()
    for i in range(1, N+1):
        answer.add(find(i))
    print(f"#{tc} {len(answer)}")