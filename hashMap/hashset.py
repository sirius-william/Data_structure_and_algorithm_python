"""
哈希表
通过一个哈希函数来计算数据存储位置。
是线性表存储结构。哈希表由一个直接寻址表和一个哈希函数组成。哈希函数h(k)将元素关键字k作为自变量，返回元素的存储下标。
假设一个长度为7的哈希表，哈希函数h(k) = k % 7.元素集合{14, 22, 3, 5}的存储方式为：
    k       22           3       5
    下标      0   1   2   3   4   5
由于哈希表的大小是有限的，而要存储的值的总数量是无限的，因此对于任何哈希函数，都会出现两个不同元素映射到同一个位置的情况，叫哈希冲突。
*********************************
解决哈希冲突——开放寻址法：
    如果哈希函数返回的位置已经有值，则可以向后探查新的位置来存储这个值。
        线型探查：如果位置i被占用，则探查i+1，i+2...
        二次探查：通过位置i被占用，则探查i+1^2，i-1^2，i+2^2，i-2^2...
        二度哈希：有n个哈希函数，当使用第1个哈希函数h1时发生冲突，则尝试h2，h3，h4...
*********************************
解决哈希冲突——拉链法：
    哈希表每个位置都连接一个链表，发生冲突时，冲突的元素加到链表后面
*********************************
直接寻址表：
    当关键字的全域U比较小时，直接寻址是一种简单而有效的方法
    缺点：
        当域U很大时，需要消耗大量内存，很不实际
        如果域U很大而实际出现的key很少，则大量空间被浪费
        无法处理关键字不是数字的情况
改进直接寻址表：哈希
    构建大小为m的寻址表T
    key为k的元素放到h(k)的位置上
    h(k)是一个函数，其将域U映射到表T[0, 1, 2, ..., m-1]
"""

# 使用项目下的单链表SingleLinkedList
from linkList.SingleLinkedList import SingleLinkedList, Member


# 哈希集合
class HashSet(object):
    def __init__(self, size=100):
        self._size = size
        # 寻址表
        self._T = [SingleLinkedList() for i in range(self._size)]
        self.available_size = size

    def _h(self, k):
        return k % self._size

    def _find(self, k):
        i = self._h(k)
        res = self._T[i].val_if_exist(k)
        return res

    def insert(self, k):
        i = self._h(k)
        if not self._find(k):
            self._T[i].add(k)
            self.available_size -= 1
        else:
            raise Exception("该值已存在")

    def print(self):
        for i, j in enumerate(self._T):
            if self._T[i].is_empty():
                continue
            print(f"====={i}=====")
            j.print()
        print(f"total size:{self._size}\tavailable size:{self.available_size}")


if __name__ == "__main__":
    x = HashSet()
    x.insert(1)
    x.insert(2)
    x.insert(101)
    x.insert(102)
    x.print()
