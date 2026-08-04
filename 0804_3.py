T = int(input())
for test_case in range(1, T+1):
    memory = list(input())
    answer = 0
    prev = memory[0]
    if prev == '1':
        answer += 1
    for i in range(1, len(memory)):
        if memory[i] != prev:
            answer += 1
        prev = memory[i]
    print(f"#{test_case} {answer}")

# 시간 복잡도 : O(N)
