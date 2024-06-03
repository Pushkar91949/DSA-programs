def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}
    stack = []
    output = []

    for char in expression:
        if char.isalnum(): 
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() 
        else:  
            while (stack and stack[-1] != '(' and
                   (precedence[char] < precedence[stack[-1]] or
                    (precedence[char] == precedence[stack[-1]] and associativity[char] == 'L'))):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

expression = input("Enter an infix expression: ")
postfix = infix_to_postfix(expression)
# print(f"Infix: {expression}")
print(f"Postfix: {postfix}")

