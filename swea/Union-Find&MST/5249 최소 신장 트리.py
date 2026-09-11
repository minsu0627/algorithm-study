# 최소 신장 트리
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
#         start, end, w = map(int, input().split())
#         edges.append((w, start, end))
#     edges.sort()
#
#     parent = [i for i in range(V+1)]
#     total = 0
#     edge_cnt = 0
#
#     for w, s, e in edges:
#         if union(parent, s, e):
#             total += w
#             edge_cnt += 1
#             if edge_cnt == V:
#                 break
#     print(f"#{tc} {total}")

# 프림
import heapq

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
        graph[e].append((w, s))

    visited = [False] * (V+1)
    heap = [(0, 0)]
    total = 0
    cnt = 0

    while heap:
        cost, n = heapq.heappop(heap)

        if visited[n]:
            continue

        visited[n] = True
        total += cost
        cnt += 1

        if cnt == V+1:
            break

        for nxt_cost, nxt_node in graph[n]:
            if not visited[nxt_node]:
                heapq.heappush(heap, (nxt_cost, nxt_node))

    print(f"#{tc} {total}")