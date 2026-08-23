class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(head, x, nums):
    if x == 0:
        new_head = Node(nums[0])
        cur = new_head

        for num in nums[1:]:
            new_node = Node(num)
            cur.next = new_node
            cur = new_node
        cur.next = head
        return new_head

    cur = head
    for _ in range(x-1):
        cur = cur.next

    for num in nums:
        new = Node(num)
        new.next = cur.next
        cur.next = new
        cur = new
    return head

def delete(head, x, y):
    if x == 0:
        for _ in range(y):
            head = head.next
        return head

    cur = head
    for _ in range(x-1):
        cur = cur.next
    temp = cur
    for _ in range(y):
        temp = temp.next
    cur.next = temp.next
    return head

def add(head, s):
    if head is None:
        head = Node(s[0])
        cur = head
        for num in s[1:]:
            cur.next = Node(num)
            cur = cur.next
        return head

    cur = head
    while cur.next is not None:
        cur = cur.next

    for num in s:
        cur.next = Node(num)
        cur = cur.next
    return head

for test_case in range(1, 11):
    N = int(input())
    originals = list(map(int, input().split()))

    head = Node(originals[0])
    current = head

    for num in originals[1:]:
        current.next = Node(num)
        current = current.next

    M = int(input())
    commands = input().split()

    i = 0
    for _ in range(M):
        temp = []
        if commands[i].isalpha():
            temp.append(commands[i])
            while True:
                i += 1
                if i < len(commands) and commands[i].isdigit():
                    temp.append(commands[i])
                else:
                    break

        cmd = temp[0]
        if cmd == 'I':
            x = int(temp[1])
            y = int(temp[2])
            nums = list(map(int, temp[3:]))
            head = insert(head, x, nums)
        elif cmd == 'D':
            x = int(temp[1])
            y = int(temp[2])
            head = delete(head, x, y)
        elif cmd == 'A':
            y = int(temp[1])
            s = list(map(int, temp[2:]))
            head = add(head, s)

    answer = []
    current = head
    for _ in range(10):
        answer.append(current.data)
        current = current.next
    print(f"#{test_case}", *answer)

# ======================================
for test_case in range(1, 11):
    N = int(input())
    # 원본 비밀번호 리스트
    pwd = list(map(int, input().split()))

    M = int(input())
    commands = input().split()

    # 리스트를 순차적으로 꺼내먹기 위해 이터레이터(iterator)로 변환
    it = iter(commands)

    try:
        while True:
            cmd = next(it)  # 명령어 알파벳 (I, D, A)

            if cmd == 'I':
                x = int(next(it))
                y = int(next(it))
                # y개의 숫자를 리스트로 묶음
                nums = [int(next(it)) for _ in range(y)]
                # 핵심! 리스트 슬라이싱을 이용한 삽입 (x번 인덱스에 nums 리스트 통째로 끼워넣기)
                pwd[x:x] = nums # [x:x]는 리스트 중간 삽입 문법으로 인덱스 x 위치에 새로운 데이터를 집어넣음

            elif cmd == 'D':
                x = int(next(it))
                y = int(next(it))
                # 핵심! 리스트 슬라이싱을 이용한 삭제 (x부터 x+y-1까지 지우기)
                del pwd[x:x + y]

            elif cmd == 'A':
                y = int(next(it))
                nums = [int(next(it)) for _ in range(y)]
                # 핵심! 리스트 맨 뒤에 이어 붙이기
                pwd.extend(nums)

    except StopIteration:
        # next(it)가 더 이상 꺼낼 명령어가 없으면 자동으로 여기로 넘어와 종료됨
        pass

    # 결과 출력 (처음 10개만 슬라이싱)
    print(f"#{test_case}", *pwd[:10])
