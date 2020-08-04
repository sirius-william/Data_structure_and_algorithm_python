"""
单向链表
特点：单向；无序；非线性
"""


# 节点类
class Member(object):
    def __init__(self, No, Val, Next):
        # no为自增值
        self.no = No
        self.val = Val
        self.next: Member = Next

    def __str__(self):
        nextStr: str
        if self.next is None:
            nextStr = "None"
        else:
            nextStr = str(self.next.__hash__())
        return f"Hash={self.__hash__()}\tno={self.no}\tval={self.val}\tNext={nextStr}"


class SingleLinkedList(object):
    def __init__(self):
        # 头部节点
        self.head = Member(0, None, None)
        # 最后一个节点
        self.last = self.head
        # 自增编号，这个自增不可变，与MySQL的自增主键相同
        self.count = 0
        # 翻转链表的头部
        self.reverseHead = Member(0, None, None)

    # 在末尾添加节点
    def add(self, val: object):
        self.count += 1
        new = Member(self.count, val, None)
        # 将先前的最后一个的next设置为新建节点
        self.last.next = new
        # 将新建节点设置为头部节点
        self.last = new

    # 在头部添加节点
    def addToHead(self, val):
        self.count += 1
        new = Member(self.count, val, None)
        new.next = self.head.next
        self.head.next = new

    # 在指定位置添加元素，before是决定是在目标前面加还是后面加，False为在目标后面加，为私有方法，是一个添加元素的通用方法，根据需求传入参数，None表示没有这个索引
    def __addByPositionDefault(self, no, val: object, before=False):
        # 如果是在0的位置上即头部节点添加，要保证必须是在头部节点后面添加
        if no == 0 and before:
            return False
        # 自增+1
        self.count += 1
        new = Member(self.count, val, None)
        # 如果发现恰好是在头部添加节点，则直接执行头部添加节点的方法
        if (self.head.next.no == no and before) or (no == 0 and not before):
            self.addToHead(val)
            return
        # 如果发现是在结尾添加元素，则直接执行
        if self.last.no == no and before is False:
            self.add(val)
            return
            # 如果在中间添加节点，则执行下面的过程
        temp = self.head
        while temp.next is not None:
            if not before:
                if temp.no == no:
                    new.next = temp.next
                    temp.next = new
                    break
            else:
                if temp.next.no == no:
                    new.next = temp.next
                    temp.next = new
                    break
            temp = temp.next
        return temp

    # 指定编号节点后面添加
    def addBefore(self, no, val):
        self.__addByPositionDefault(no, val, True)

    # 指定编号节点前面添加
    def addAfter(self, no, val):
        self.__addByPositionDefault(no, val, False)

    # 通过自增索引查找节点，None表示没有这个索引
    def getByNo(self, no):
        temp = self.head
        while temp.next is not None:
            if temp.next.no == no:
                # 以返回值方式输出
                return temp.next
            temp = temp.next
        return None

    # 清空链表
    def clear(self):
        self.head.next = None

    # 删除指定位置的元素，None表示没有这个索引
    def deleteByNo(self, no):
        temp = self.head
        while temp is not None:
            if temp.no == no:
                if temp.next.next is None:
                    temp.next = None
                    self.last = temp
                    return
                temp.next = temp.next.next
                return
            temp = temp.next
        return temp

    # 删除第一个节点
    def deleteFirst(self):
        self.head.next = self.head.next.next

    # 删除最后一个节点
    def deleteLast(self):
        temp = self.head
        while temp is not None:
            if temp.next.next is None:
                temp.next = None
                self.last = temp
                break
            temp = temp.next

    # 查找指定值的索引
    def getVal(self, val):
        temp = self.head
        while temp is not None:
            if temp.val == val:
                return temp.no
            temp = temp.next
        if temp is None:
            return None

    # 查找正数第n个节点
    def getFromHead(self, n):
        if n > self.size():
            return None
        temp = self.head
        myCount = 0
        while temp.next is not None:
            myCount += 1
            if myCount == n:
                return temp.next
            temp = temp.next

    # 查找倒数第n个节点
    def getFromBehind(self, n):
        if n == 1:
            return self.last
        a = self.size() - n + 1
        return self.getFromHead(a)

    # 标准输出
    def print(self):
        temp = self.head
        while temp is not None:
            if temp.no != 0:
                print(temp)
            temp = temp.next

    @staticmethod
    def printLinkedList(user: Member):
        headNo = user.no
        while user is not None:
            if user.no != headNo:
                print(user)
            user = user.next

    # 翻转链表，replace：是否覆盖原链表，true为覆盖
    # 思路：新建一个空链表，每次从原链表中拿出一个元素放到新链表头部
    def reverse(self, replace=False):
        # 新的链表的头部
        newLink = Member(0, None, None)
        temp = self.head
        while temp is not None:
            """
            <方式一>这种方式创建了新对象，会改变原链表内节点的内存地址
            newMember = Member(temp.no, temp.val, None)
            newMember.next = newLink.next
            newLink.next = newMember
            temp = temp.next
            """
            # <方式二>下面这种方式不会改变内存地址
            # 先把当前遍历节点的下一个节点存起来，这样使当前节点的next与原链表脱离关系，即使next变了，也可以通过myNext变量赋值回来
            myNext: Member = temp.next
            # 把新链表的第一个节点赋值给当前遍历节点的next
            temp.next = newLink.next
            # 新链表的第一个节点设置成当前遍历节点
            newLink.next = temp
            # 因为temp的next发生了改变，不在指向原链表，使用把之前存储起来的当前遍历节点的next重新赋值给temp
            temp = myNext
        if replace:
            # 如果替换原链表
            self.head = self.reverseHead
            self.reverseHead = None
        return newLink

    # 返回链表长度
    def size(self):
        size = 0
        temp = self.head
        while temp.next is not None:
            size += 1
            temp = temp.next
        return size

    def change(self, no, val):
        temp: Member = self.head
        while temp.next is not None:
            if temp.no == no:
                temp.val = val
                break
            temp = temp.next
