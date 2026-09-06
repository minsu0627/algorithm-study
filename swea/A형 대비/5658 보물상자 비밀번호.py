import io
import sys

sample_input = """
2
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
""".strip()

sys.stdin = io.StringIO(sample_input)

def making_password(words):
    for i in range(0, N, part):
        passwords.add(words[i:i+part])

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    nums = input()
    part = N // 4
    passwords = set()
    for _ in range(part):
        making_password(nums)
        nums = nums[-1] + nums[:-1]
    passwords = sorted(passwords, reverse=True)
    print(f"#{test_case} {int(passwords[K-1], 16)}")

# 16진수를 10진수로 변경하는 법
# 만약 str = "1F7"라면 answer = int(str, 16) -> 출력: 503

# 더 좋은 풀이 : 슬라이딩 윈도우
# T = int(input())

# for test_case in range(1, T + 1):
#     N, K = map(int, input().split())
#     nums = input()
#     part = N // 4
    
#     # 원형 탐색을 위해 문자열 끝에 앞부분(part-1 만큼)을 이어 붙임
#     # 예: nums = "1B3B3B81F75E", part = 3
#     # extended_nums = "1B3B3B81F75E" + "1B"
#     extended_nums = nums + nums[:part-1]
    
#     passwords = set()
    
#     # 0부터 N-1까지 1칸씩 이동하며 part 길이만큼 자름 (모든 경우의 수 커버)
#     for i in range(N):
#         # 자름과 동시에 10진수로 변환하여 set에 추가
#         num_str = extended_nums[i:i+part]
#         passwords.add(int(num_str, 16))
        
#     # set을 내림차순 정렬하여 리스트로 만든 후 K-1 번째 요소 출력
#     ans = sorted(passwords, reverse=True)[K-1]
    
#     print(f"#{test_case} {ans}")
