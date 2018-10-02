class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.insert(0, item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)

def check(parentheses_string):
    s1 = Stack()
    i = 0
    still_balance = True
    while i<len(parentheses_string) and still_balance:
        if parentheses_string[i] == '(':
            s1.push(parentheses_string[i])
        else:
            if s1.is_empty():
                still_balance = False
            else:
                s1.pop()
        i = i + 1
    if still_balance and s1.is_empty():
        return True
    else:
        return False

#
# print(check('((()))'))
# print(check('(()'))

def match(before, behind):
    befores = ['(', '{', '[']
    behinds = [')', '}', ']']
    if befores.index(before) == behinds.index(behind):
        return True
    else:
        return False


def check_general(parentheses_string):
    s = Stack()
    i = 0
    still_balance = True
    while i < len(parentheses_string) and still_balance:
        if parentheses_string[i] in {'(', '{', '['}:
            s.push(parentheses_string[i])
        else:
            if s.is_empty():
                still_balance = False
            else:
                before = s.peek()
                behind = parentheses_string[i]
                if match(before, behind) is True:
                    s.pop()
                else:
                    still_balance = False

        i = i + 1
    if still_balance and s.is_empty():
        return True
    else:
        return False

# print(check_general('{{([][])}()}'))
# print(check_general('[{()]'))


def converting_decimal_to_binary(decimal):
    s = Stack()
    binary = ''
    done = False
    while done is False:
        left = decimal % 2
        decimal = decimal // 2
        s.push(left)
        if decimal == 0:
            done =True

    while s.is_empty() is False:
        binary = binary + str(s.pop())
    return int(binary)


def base_converter(dec_number, base):
    digits = "0123456789ABCDEFGHIJK"
    rem_stack = Stack()
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base
    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]
    return new_string

# print(base_converter(25, 3))
# print(base_converter(16, 17))

def convert_infix_postfix(infix_str):

    # define priority
    priority = {}
    priority['*'] = 3
    priority['/'] = 3
    priority['+'] = 2
    priority['-'] = 2
    priority['('] = 1

    # init operator stack
    op_stack = Stack()

    # post output
    post_output = []

    infix_str = infix_str.split(' ')
    print('The input list is:', infix_str)

    # conversion
    for token in infix_str:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            post_output.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_tocken = op_stack.pop()
            while top_tocken != '(':
                post_output.append(top_tocken)
                top_tocken = op_stack.pop()
        else:
            if (not op_stack.is_empty()) and (priority[op_stack.peek()] > priority[token]):
                post_output.append(op_stack.pop())
                op_stack.push(token)

            else:
                op_stack.push(token)

    # append the rest operator
    while not op_stack.is_empty():
        post_output.append(op_stack.pop())

    return ' '.join(post_output)


#print(convert_infix_postfix("( A * B + C ) * D"))

def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()
    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
            return operand_stack.pop()

def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
print(postfix_eval('7 8 + 3 2 + /'))