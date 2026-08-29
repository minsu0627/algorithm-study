T = int(input())
for test_case in range(1, T+1):
    N, code = input().split()
    output = []
    for c in code:
        output.append(format(int(c, 16), '04b'))
    print(''.join(output))