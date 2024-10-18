class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        result = ""
        cur_node = self.head
        while cur_node is not None:
            if cur_node.next is not None:    
                result += str(cur_node.val) + ", "
            else:
                result += str(cur_node.val)
            cur_node = cur_node.next
        return result

    def push(self, data):
        new_node = Node(data)
        if self.head != None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
        
    def pop(self):
        if self.head is not None:
            popped_value = self.head.val
            self.head = self.head.next
            return popped_value
        else:
            return f"Empty"       


def parseParenthesis(string):
    size = len(string)
    stack = Stack(size)

    for i in range(size):
        check = string[i]
        if check == '(':
            stack.push(1)
        elif check == ')':
            if stack.isEmpty():
                return False
            else:
                stack.pop()

    if stack.isEmpty():
        return True
    else:
        return False
