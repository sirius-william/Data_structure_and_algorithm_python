"""
单向环形链表
"""


# 节点类
class Member(object):
    def __init__(self, no, val, Next, start: bool = False):
        self.no = no
        self.val = val
        if start:
            # 如果定义为起始节点，则连接到自己
            self.next: Member = self
        else:
            self.next: Member = Next

    def __str__(self):
        nextStr: str
        if self.next is None:
            nextStr = "None"
        else:
            nextStr = str(self.next.__hash__())
        return f"Hash={self.__hash__()}\tno={self.no}\tval={self.val}\tNext={nextStr}"


class SingleCircleLinkedList(object):
    def __init__(self, val):
        self.start: Member = Member(0, val, None, True)
        self.count = 0

    # 标准输出
    def print(self):
        temp: Member = self.start
        while temp is not None:
            print(temp)
            temp = temp.next
            if temp == self.start:
                break

    # 在末尾（起始节点前面）添加元素
    def add(self, val):
        self.count += 1
        temp: Member = self.start
        newMember = Member(self.count, val, None)
        newMember.next = self.start
        while True:
            if temp.next == self.start:
                temp.next = newMember
                break
            temp = temp.next
            if temp == self.start:
                break

    # 在指定索引添加元素，默认为目标节点后，为私有方法，通法，类内根据需求调用
    def __addByNoDefault(self, no, val, before: bool = False):
        self.count += 1
        temp = self.start
        newMember = Member(self.count, val, None)
        if before:
            while True:
                if temp.next.no == no:
                    newMember.next = temp.next
                    temp.next = newMember
                    break
                temp = temp.next
                if temp == self.start:
                    break
        else:
            while True:
                if temp.no == no:
                    newMember.next = temp.next
                    temp.next = newMember
                    break
                temp = temp.next
                if temp == self.start:
                    break

    def addBeforeNo(self, no, val):
        self.__addByNoDefault(no, val, before=True)

    def addAfterNo(self, no, val):
        self.__addByNoDefault(no, val, before=False)

    def deleteLast(self):
        temp: Member = self.start
        while True:
            if temp.next.next == self.start:
                temp.next = self.start
                break
            temp = temp.next
            if temp == self.start:
                break

    def deleteFirst(self):
        self.start.next = self.start.next.next

    def deleteByNo(self, no, before: bool = True):
        temp: Member = self.start
        if before:
            while True:
                if temp.next.next.no == no:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                if temp == self.start:
                    break
        else:
            while True:
                if temp.next.no == no:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                if temp == self.start:
                    break

    def change(self, no, val):
        temp: Member = self.start
        while True:
            if temp.no == no:
                temp.val = val
                break
            temp = temp.next
            if temp == self.start:
                break
