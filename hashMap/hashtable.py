from hashMap.hashset import HashSet
from linkList.SingleLinkedList import SingleLinkedList, Member


# 重写链表的两个方法，将链表节点的no属性作为key，原链表中no是自增值
class HashSingleList(SingleLinkedList):
    def __init__(self):
        super().__init__()

    def addKeyVal(self, key, val):
        """
        在最后新增节点
        :param key: key
        :param val: value
        :return:
        """
        self.count += 1
        new_member = Member(key, val, None)
        self.last.next = new_member
        self.last = new_member

    def val_if_exist(self, key):
        temp = self.head
        while temp is not None:
            if temp.no == key:
                return True
            temp = temp.next
        return False


class HashTable(HashSet):
    def __init__(self, size=100):
        super().__init__(size)
        self._T = [HashSingleList() for i in range(self._size)]

    def insert(self, key, val=None):
        if not self._find(key):
            h = self._h(key)
            self._T[h].addKeyVal(key, val)
        else:
            print("该值已存在")


if __name__ == "__main__":
    x = HashTable()
    x.insert(1, 2)
    x.insert(2, 2)
    x.insert(3, "my")
    x.insert(101, 2)
    x.insert(102, "2")
    x.insert(103, "jhs")
    x.print()
