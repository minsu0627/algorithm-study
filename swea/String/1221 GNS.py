T = int(input())
for _ in range(T):
    test_case, length = input().split()
    nums = input().split()
    planet_num = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0,
             "SVN":0, "EGT":0, "NIN":0}
    for i in range(int(length)):
        planet_num[nums[i]] += 1

    answer = []
    for k, v in planet_num.items():
        for _ in range(v):
            answer.append(k)
    print(f"{test_case}", *answer)