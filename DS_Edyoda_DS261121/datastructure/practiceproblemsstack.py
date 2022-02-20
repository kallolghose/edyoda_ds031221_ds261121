from datastructure.stacks import Stack


def infix_to_postfix(infix_str):
    stack = Stack()
    infix_data = infix_str.split()
    postfix_str = ""
    for data in infix_data:
        if is_operator(data):
            if stack.is_empty():
                stack.push(data)
                continue
            peeked_op = stack.peek()
            while get_precedence(peeked_op) >= get_precedence(data):
                postfix_str = postfix_str + ' ' + stack.pop()
                peeked_op = stack.peek()
            stack.push(data)
        else:
            if data == '(':
                stack.push("(")
            elif data == ')':
                while True:
                    popped_data = stack.pop()
                    if popped_data == '(':
                        break
                    postfix_str = postfix_str + ' ' + popped_data
            else:
                postfix_str = postfix_str + ' ' + data

    while not stack.is_empty():
        postfix_str = postfix_str + ' ' + stack.pop()

    return postfix_str


def is_operator(data):
    if data in ['+', '-', '*', '/', '%', '^']:
        return True
    return False


def get_precedence(data):
    if data == '+' or data == '-':
        return 1
    if data == '*' or data == '/' or data == '%':
        return 2
    if data == '^':
        return 3
    return -1


def validate_string_of_brackets(str):
    stack = Stack()
    for ch in str:
        if ch in ["(", "[", "{"]:
            stack.push(ch)
        else:
            if stack.is_empty():
                print("String NOT proper !!")
                return
            popped_ch = stack.pop()
            if not is_familial(ch, popped_ch):
                print("String NOT proper !!")
                return

    if not stack.is_empty():
        print("String NOT proper !!")
        return

    print("String is Proper !!")


def is_familial(current_ch, popped_ch):
    if popped_ch == '(' and current_ch == ')':
        return True
    if popped_ch == '[' and current_ch == ']':
        return True
    if popped_ch == '{' and current_ch == '}':
        return True
    return False


if __name__ == "__main__":
    my_str = input("Enter String : ")
    print(infix_to_postfix(my_str))