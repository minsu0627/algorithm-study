# 1번
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    candidates = []
    for i in range(N-1):
        for j in range(i+1, N):
            temp = list(map(int, str(A[i] * A[j])))
            prev = temp[0]
            add = True
            for k in range(1, len(temp)):
                if temp[k] >= prev:
                    prev = temp[k]
                    continue
                else:
                    add = False
                    break
            if add:
                candidates.append(A[i] * A[j])
    candidates.sort()
    print(f"#{test_case} {candidates[-1]}")

# 1번 코드가 for k 구문 때문에 시간 터지는 것이라 생각하고 최적화 시도
# 이전 숫자와 하나하나 비교하는 방식에서 정렬해서 같은지 체크하는 방식 시도
# 2번
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    candidates = []
    for i in range(N-1): # Ai와 Aj를 곱해야하므로 마지막 수를 남기기 위해 N-1
        for j in range(i+1, N): # Ai의 인덱스가 0이라면 Aj의 인덱스는 1부터 시작해야하기 때문에 i+1부터 시작
            temp = list(map(int, str(A[i] * A[j])))
            if temp == sorted(temp): # temp가 단조 증가하는 수인지 확인하기 위해 오름차순 정렬된 것과 같은지 체크
                candidates.append(A[i] * A[j])
    if candidates:
        candidates.sort()
        print(f"#{test_case} {candidates[-1]}")
    else:
        print(f"#{test_case} -1")
        
# 2번 코드로 pass했지만 더 최적화할 수 있을 것 같아 gemini 통해 개선한 코드
# maximum을 -1로 잡아 최댓값으로 업데이트 안 된 경우 자연스레 -1 출력
# 후보 리스트에 가능한 값을 다 추가하는 것이 아닌 기존 최댓값보다 큰 경우만
# 정렬했을 때와 같은지 체크하고 같다면 최댓값 업데이트
# 3번
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    maximum = -1
    
    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] * A[j] > maximum:
                temp = list(map(int, str(A[i] * A[j])))
                if temp == sorted(temp):
                    maximum = A[i] * A[j]
                    
    print(f"#{test_case} {maximum}")
