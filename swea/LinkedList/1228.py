for test_case in range(1, 11):
    N = int(input())
    original = list(map(int, input().split()))
    C = int(input())
    temp = input().split('I')
    commands = []
    for c in temp:
        if c == '':
            continue
        else:
            commands.append(list(map(int, c.split())))

    for i in range(C):
        start = commands[i][0]
        cnt = commands[i][1]
        nums = commands[i][2:]
        idx = 0
        for j in range(start, start+cnt):
            original.insert(j, nums[idx])
            idx += 1
    print(original[:10])

# class 방식
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

for test_case in range(1, 11):
    N = int(input())
    original = list(map(int, input().split()))

    head = Node(original[0])
    current = head

    for num in original[1:]:
        current.next = Node(num)
        current = current.next

    C = int(input())
    commands = input().split('I')

    for command in commands:
        if command == '':
            continue

        command = list(map(int, command.split()))
    
        x = command[0]
        cnt = command[1]
        nums = command[2:]

        current = head
        for _ in range(x-1):
            current = current.next
        
        for num in nums:
            new_node = Node(num)

            new_node.next = current.next
            current.next = new_node

            current = new_node

        answer = []
        current = head

        for _ in range(10):
            answer.append(current.data)
            current = current.next
        
        print(f"#{test_case}, *answer")