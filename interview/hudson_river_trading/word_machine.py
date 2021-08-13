def solution(S: str) -> int:
    ERROR = -1
    MIN_INT = 0
    MAX_INT = 20 ** 20 - 1
    OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
    }
    ACTIONS = {
        'POP': lambda s: s.pop(),
        'DUP': lambda s: s.append(s[-1]),
    }

    stack = []
    operations = S.split()
    for operation in operations:
        if operation in OPERATORS:
            if len(stack) < 2:
                return ERROR
            else:
                x = stack.pop()
                y = stack.pop()
                z = OPERATORS[operation](x, y)
                if MIN_INT <= z <= MAX_INT:
                    stack.append(z)
                else:
                    return ERROR
        elif operation in ACTIONS:
            if len(stack) < 1:
                return ERROR
            else:
                ACTIONS[operation](stack)
        else:
            stack.append(int(operation))

    if len(stack) < 1:
        return ERROR
    else:
        return stack.pop()
