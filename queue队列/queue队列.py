"""
队列
仅允许在列表的一端进行插入，另一端进行删除
进行插入的一段叫队尾（rear），插入动作称为进队或入队
进行删除的一端称为队头（front），删除动作称为出队
队列的性质：先进先出，定长（存在队满情况，不考虑python列表无限长）

队列实现方式：环形队列
假定队列定长为12，当队尾到达11号位时，再插入数据时队尾变为0号位置，故每次插入元素时，rear值变为rear=(rear+1)%12，即rear=(rear+1) % maxSize
队满条件：rear后面是front，即(rear+1) % maxSize == front
"""


class Queue:
    def __init__(self, length):
        self._queue = [0] * length
        self._rear = 0
        self._front = 0
        self._length = length

    def insert(self, element):
        if self.is_full():
            return "队列已满"
        self._queue[self._rear] = element
        self._rear = (self._rear + 1) % self._length

    def pop(self):
        if self.is_empty():
            return "队列空"
        res = self._queue[self._front]
        self._front = (self._front + 1) % self._length
        return res

    def is_full(self):
        return ((self._rear + 1) % self._length) == self._front

    def is_empty(self):
        return self._rear == self._front


queue = Queue(4)
queue.insert(1)
queue.insert(2)
queue.insert(3)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
