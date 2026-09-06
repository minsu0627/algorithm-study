for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes = sorted(boxes, reverse=True)

    for _ in range(dump):
        if len(set(boxes)) == 1 or (len(set(boxes)) == 2 and (boxes[0] - boxes[-1] == 1)):
            break
        else:
            boxes[0] -= 1
            boxes[-1] += 1
            boxes = sorted(boxes, reverse=True)
    print(f"#{test_case} {boxes[0] - boxes[-1]}")
