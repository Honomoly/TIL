from c_stack import *

def is_pair(text):
    pair_stack = Stack()
    pairs_num1 = {"(":0, "{":1, "[":2}
    pairs_num2 = {")":0, "}":1, "]":2}
    for i in text:
        if i in ["(", "{", "["]:
            pair_stack.push(pairs_num1[i])
        elif i in [")", "}", "]"]:
            if pair_stack.peek() == pairs_num2[i]:
                pair_stack.pop()
            else:
                return False
    if pair_stack.peek() is None:
        return True
    else:
        return False