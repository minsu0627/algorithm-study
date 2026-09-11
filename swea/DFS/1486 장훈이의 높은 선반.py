# 장훈이의 높은 선반
# 높이가 B인 선반
# N명의 점원, 점원들의 키는 Hi
# 직원들의 높이의 합으로 탑의 높이를 만드는데 탑의 높이가 B 이상인 것 중 최소 구하기
# 첫 줄 : N, B
# 두 번째 줄 : 직원들 키
# 가지치기 - 탑의 높이가 B와 같으면 끝
import sys
sys.stdin = open("input.txt", "r")

def dfs(idx, temp):
    if temp == B:
        answer[0] = temp
        return

    if temp > answer[0]:
        return

    if temp >= B:
        answer[0] = min(answer[0], temp)
        return

    for i in range(idx, N):
        dfs(i+1, temp + H[i])

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    answer = [200000]
    dfs(0, 0)
    print(f"#{tc} {abs(B - answer[0])}")



