T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    points = list(input())
    cnt_list = {i: 0 for i in range(10)}
    answer_num = 0
    answer_cnt = cnt_list[0]

    for p in points:
        cnt_list[int(p)] += 1

    for i in range(1, 10):
        if cnt_list[i] >= answer_cnt:
            answer_num = i
            answer_cnt = cnt_list[i]
    print(answer_num, answer_cnt)
