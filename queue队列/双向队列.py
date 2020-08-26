"""
队首与队尾都支持进出
主要了解内置deque双向队列模块
"""
from collections import deque
"""
创建deque对象，
参数：可迭代对象、最大长度
入队时，如果已经达到最大长度，则自动从另一端出队
"""
q = deque([])
# 队尾进队
q.append(1)
# 队首出队
q.popleft()

# 队首进队
q.appendleft(1)
# 队尾出队
q.pop()
