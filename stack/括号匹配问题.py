"""
给一个字符串，其中包含小括号、中括号、大括号，求该字符串中是否匹配
"""
from stack import _stack


def check(string: str):
    left = {"(": ")", "[": "]", "{": "}"}
    st = _stack.Stack()
    for i in string:
        if i in left.keys():
            st.push(i)
        elif i in left.values():
            pop = st.pop()
            if left[pop] == i:
                continue
            else:
                return False
        else:
            continue
    return True


x = "{}[]({)"
print(check(x))
