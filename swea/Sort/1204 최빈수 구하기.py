T = int(input())
for _ in range(T):
    test_case = int(input())
    scores = list(map(int, input().split()))
    score_count = {}
    for s in scores:
        score_count[s] = score_count.get(s, 0) + 1
    sorted_count = sorted(score_count.items(), key=lambda x:(x[1], x[0]), reverse=True)
    print(sorted_count)