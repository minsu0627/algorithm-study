# 진용이네 주차타워

import sys
sys.stdin = open('input.txt', 'r')
import heapq
from collections import deque

def calc(car_num):
    global answer
    space_num = heapq.heappop(space)
    using_space[car_num] = space_num
    answer += parking_fee[space_num] * car_weight[car_num]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    space = [i for i in range(1, n+1)]
    heapq.heapify(space)
    using_space = [0] * (m+1)
    parking_fee = [0]
    car_weight = [0]
    queue = deque()
    answer = 0

    for _ in range(n):
        parking_fee.append(int(input()))
    for _ in range(m):
        car_weight.append(int(input()))

    for _ in range(m*2):
        move = int(input())
        if move > 0:
            if space:
                calc(move)
            else:
                queue.append(move)
        else:
            heapq.heappush(space, using_space[-move])
            using_space[-move] = 0
            if queue:
                car = queue.popleft()
                calc(car)

    print(f"#{tc} {answer}")