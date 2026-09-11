# 서로소 집합
# 초기 집합 n개
# 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지 확인하는 연산
# import sys
# sys.stdin = open('input.txt', 'r')

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parents[root_y] = root_x

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    parents = [i for i in range(n+1)]
    answer = ''
    for _ in range(m):
        cmd, a, b = map(int, input().split())
        if cmd == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                answer += '1'
            else:
                answer += '0'
    print(f"#{tc} {answer}")