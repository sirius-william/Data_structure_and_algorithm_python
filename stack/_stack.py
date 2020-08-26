# 栈
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, element):
        self._stack.append(element)

    def pop(self):
        return self._stack.pop()

    def get_top(self):
        if len(self._stack) < 1:
            return None
        else:
            return self._stack[-1]

    def is_empty(self):
        return len(self._stack) == 0

    def is_contain(self, val):
        return val in self._stack

    def as_list(self):
        return self._stack
