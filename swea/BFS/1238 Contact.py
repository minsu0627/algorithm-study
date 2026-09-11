# Contact
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N, start = map(int, input().split())
    network = [[] for _ in range(101)]
    visited = [False] * 101
    temp = list(map(int, input().split()))
    for i in range(0, N, 2):
        network[temp[i]].append(temp[i+1])

    max_node = start
    max_count = 0

    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        node, cnt = queue.popleft()

        if cnt > max_count:
            max_count = cnt
            max_node = node

        if cnt == max_count:
            if node > max_node:
                max_node = node

        for net in network[node]:
            if not visited[net]:
                visited[net] = True
                queue.append((net, cnt+1))

    print(f"#{tc} {max_node}")
