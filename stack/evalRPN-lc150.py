def evalRPN(self, tokens: list[str]) -> int:
    # explanation on RPN: http://en.wikipedia.org/wiki/Reverse_Polish_notation
    # TC: O(n)
    # SC: O(n)
    # Using the stack data structure, whenever we encounter an operator,
    # apply it on two previous values(order does matter for '-' and '/')
    # Use int() function for rounding towards zero
    stack = []

    for t in tokens:
        if t == '+':
            second, first = stack.pop(), stack.pop()
            res = first + second
            stack.append(res)
        elif t == '-':
            second, first = stack.pop(), stack.pop()
            res = first - second
            stack.append(res)
        elif t == '*':
            second, first = stack.pop(), stack.pop()
            res = first * second
            stack.append(res)
        elif t == '/':
            second, first = stack.pop(), stack.pop()
            res = int(first / second) # round towards zero
            stack.append(res)
        else:
            stack.append(int(t))

    return stack[0]