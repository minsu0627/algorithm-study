T = int(input())
for test_case in range(1, T+1):
    row = input()
    braket_stack = []
    quote_stack = []
    button = True
    
    for r in row:
        if quote_stack:
            if r == quote_stack[-1]:
                quote_stack.pop()
            continue
        else:
            if r == "'" or r == '"':
                quote_stack.append(r)
                continue

        if r == '(' or r == '{':
            braket_stack.append(r)
        elif r == ')':
            if not braket_stack or braket_stack[-1] != '(':
                button = False
                break
            braket_stack.pop()
        elif r == '}':
            if not braket_stack or braket_stack[-1] != '{':
                button = False
                break
            braket_stack.pop()

    if button and not braket_stack:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")