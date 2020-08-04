"""
双向链表
特点：可以两个方向遍历
"""


# 节点类
class Member(object):
    def __init__(self, no, pre, val, Next):
        self.no = no
        self.pre: Member = pre
        self.val = val
        self.next: Member = Next

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


# 链表类
class DoubleLinkedList(object):
    def __init__(self):
        # 头部节点
        self.head = Member(0, None, None, None)
        # 尾部节点
        self.foot = Member(-1, None, None, None)
        # 头尾相连，初始化完成
        self.head.next = self.foot
        self.foot.pre = self.head
        # 自增数
        self.count = 0

    # 标准输出，direction表示方向，true为正向，false为反向
    def print(self, direction: bool = True):
        if direction:
            temp = self.head
            while temp is not None:
                if temp.no != 0 and temp.no != -1:
                    print(temp)
                temp = temp.next
        else:
            temp = self.foot
            while temp is not None:
                if temp.no != 0 and temp.no != -1:
                    print(temp)
                temp = temp.pre

    # 在末尾添加
    def addAtFoot(self, val):
        self.count += 1
        newMember = Member(self.count, None, val, None)
        newMember.pre = self.foot.pre
        newMember.next = self.foot
        self.foot.pre.next = newMember
        self.foot.pre = newMember

    # 在头部添加
    def addAtHead(self, val):
        self.count += 1
        newMember = Member(self.count, None, val, None)
        newMember.next = self.foot.next
        newMember.pre = self.head
        self.head.next.pre = newMember
        self.head.next = newMember

    # 删除指定编号索引的节点
    def deleteByNO(self, no, direction: bool = True):
        if direction:
            temp = self.head
        else:
            temp = self.foot
        while temp is not None:
            if temp.no == no:
                temp.pre.next = temp.next
                temp.next.pre = temp.pre
                break
            if direction:
                temp = temp.next
            else:
                temp = temp.pre

    # 删除最后一个节点
    def deleteFoot(self):
        self.foot.pre.pre.next = self.foot
        self.foot.pre = self.foot.pre.pre

    # 删除第一个节点
    def deleteHead(self):
        self.head.next.next.pre = self.head
        self.head.next = self.head.next.next

    # 查找指定索引的值
    def getByNo(self, no, direction: bool = True):
        if direction:
            temp = self.head
        else:
            temp = self.foot
        while temp is not None:
            if temp.no == no:
                return temp.val
            if direction:
                temp = temp.next
            else:
                temp = temp.pre
        return None

    # 查找值所在的索引
    def getNoOf(self, val, direction: bool = True):
        temp: Member
        if direction:
            temp = self.head
        else:
            temp = self.foot
        while temp is not None:
            if temp.val == val:
                return temp.no
            if direction:
                temp = temp.next
            else:
                temp = temp.pre
        return None

    # 返回链表长度
    def size(self):
        size = 0
        temp = self.head
        while temp is not None:
            size += 1
            temp = temp.next
        return size - 2  # size里面包括了头结点和尾结点，要减去

    def change(self, no, val):
        temp: Member = self.head
        while temp is not None:
            if temp.no == no:
                temp.val = val
                break
            temp = temp.next
