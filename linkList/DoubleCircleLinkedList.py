"""
双向环形链表
"""


class DoubleCircleMember(object):

    def __init__(self, no, val):
        self.next: DoubleCircleMember = self
        self.pre: DoubleCircleMember = self
        self.no = no
        self.val = val

    def __str__(self):
        nextStr: str
        preStr: str
        if self.next is None:
            nextStr = "None"
        else:
            nextStr = str(self.next.__hash__())
        if self.pre is None:
            preStr = "None"
        else:
            preStr = str(self.pre.__hash__())
        return f"Hash={self.__hash__()}\tno={self.no}\tpre={preStr}\tval={self.val}\tNext={nextStr}"


class DoubleCircleLinkedList(object):
    def __init__(self, no, val):
        self.start: DoubleCircleMember = DoubleCircleMember(no, val)
        self.count = 0

    # 添加
    def add(self, target, val, location):
        # 0为目标前面，1为目标后面
        temp = self.start
        while True:
            if temp.no == target:
                self.count += 1
                newMember = DoubleCircleMember(self.count, val)
                if location == 0:
                    newMember.next = temp
                    newMember.pre = temp.pre
                    temp.pre.next = newMember
                    temp.pre = newMember
                elif location == 1:
                    newMember.next = temp.next
                    newMember.pre = temp
                    temp.next.pre = newMember
                    temp.next = newMember
            temp = temp.next
            if temp == self.start:
                break

    def print(self):
        temp = self.start
        while True:
            print(temp)
            temp = temp.next
            if temp == self.start:
                break
