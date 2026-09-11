# 최소 스패닝 트리
import sys
sys.stdin = open('input.txt')

# 크루스칼
# def find(parent, x):
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]
#
# def union(parent, x, y):
#     root_x = find(parent, x)
#     root_y = find(parent, y)
#     if root_x != root_y:
#         parent[root_y] = root_x
#         return True
#     return False
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     edges = []
#     for _ in range(E):
#         a, b, c = map(int, input().split())
#         edges.append((c, a, b))
#     edges.sort()
#
#     parent = [i for i in range(V+1)]
#     total = 0
#     cnt = 0
#
#     for c, a, b in edges:
#         if union(parent, a, b):
#             total += c
#             cnt += 1
#             if cnt == V-1:
#                 break
#     print(f"#{tc} {total}")

# 프림
import heapq

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    heap = [(0, 1)]
    total = 0
    cnt = 0

    while heap:
        cost, node = heapq.heappop(heap)
        if visited[node]:
            continue

        visited[node] = True
        total += cost
        cnt += 1

        if cnt == V:
            break

        for nxt_cost, nxt_node in graph[node]:
            if not visited[nxt_node]:
                heapq.heappush(heap, (nxt_cost, nxt_node))

    print(f"#{tc} {total}")