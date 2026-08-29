decoding = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    def find():
        temp = ''
        for i in range(N):
            for j in range(M - 1, -1, -1):
                if matrix[i][j] == '1':
                    for k in range(56):
                        temp += matrix[i][j - k]
                    return temp

    password = find()[::-1]
    result = []
    for p in range(0, 56, 7):
        result.append(int(decoding[password[p:p+7]]))
    odd = 0
    even = 0
    for r in range(8):
        if r % 2 != 0:
            even += result[r]
        else:
            odd += result[r]
    if (odd * 3 + even) % 10 == 0:
        print(f"#{test_case} {odd + even}")
    else:
        print(f"#{test_case} 0")