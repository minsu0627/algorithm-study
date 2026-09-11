# 하나로
# import sys
# sys.stdin = open('input.txt')

def find(arr, x):
    if arr[x] != x:
        arr[x] = find(arr, arr[x])
    return arr[x]

def union(arr, x, y):
    root_x = find(arr, x)
    root_y = find(arr, y)
    if root_x != root_y:
        arr[root_y] = root_x
        return True
    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    info = {i: [X[i], Y[i]] for i in range(N)}
    E = float(input())
    parents = [i for i in range(N)]
    distance = []

    for i in range(N-1):
        for j in range(i+1, N):
            dist = (info[i][0] - info[j][0]) ** 2 + (info[i][1] - info[j][1]) ** 2
            distance.append((dist, i, j))

    distance.sort()

    total = 0
    cnt = 0

    for cost, s, e in distance:
        if union(parents, s, e):
            total += cost
            cnt += 1
            if cnt == N-1:
                break

    print(f"#{tc} {round(total*E)}")

