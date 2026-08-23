# dfs로 다 돌면서 최댓값 업데이트
# 각 케이스의 분기들을 기준으로 백트레킹

def dfs(blocks, temp):
    maximum = 0
    if len(blocks) == 1:
            return temp + blocks[0]
    for i in range(len(blocks)):
        if i == 0:
            add = blocks[1]
        elif i == len(blocks) - 1:
            add = blocks[i-1]
        else:
            add = (blocks[i-1] * blocks[i+1])
        removed = blocks.pop(i)
        result = dfs(blocks, temp + add)
        maximum = max(maximum, result)
        blocks.insert(i, removed)
    return maximum

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    blocks = list(map(int, input().split()))
    answer = dfs(blocks, 0)
    print(f"#{test_case} {answer}")

# 기존에 if문에서 temp에 직접 더해줬는데 이러면 점수가 누적돼어 백트레킹이 어려워짐 -> 더해야할 값을 따로 구해서 다음 dfs에 넘겨주기
