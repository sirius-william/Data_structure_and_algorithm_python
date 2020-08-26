"""
在堆排序中，二叉树为顺序存储，各节点存储在一个列表内，这种方式适合完全二叉树
二叉树的链式存储：将二叉树的节点定义为一个对象，节点之间类似链表的连接方式
遍历方式：前序、后序、中序、层次遍历。单独给一种遍历方式无法反推出树
"""
from collections import deque


class Node(object):
    def __init__(self, data, left=None, right=None, father=None):
        self.data = data
        self.left: Node = left
        self.right: Node = right
        self.father: Node = father

    def __str__(self):
        return f"{self.data}\t{self.left.__hash__()}\t{self.right.__hash__()}"


# 普通基本的用于遍历的二叉树，不定义节点的父节点
class BinaryTree(object):
    """
    二叉树的基本，是后面所有二叉树的基类，这个类只定义了四种遍历方法和基本输出
    """
    def __init__(self, rootNode):
        self.root: Node = rootNode

    # 遍历方式一：前序遍历，根——左——右（递归）
    def __pre_order(self, target: Node):
        if target:
            print(target.data)
            self.__pre_order(target.left)
            self.__pre_order(target.right)

    # 遍历方式二：中序遍历，左——根——右（递归）
    def __middle_order(self, target: Node):
        if target:
            self.__middle_order(target.left)
            print(target.data)
            self.__middle_order(target.right)

    # 遍历方式三：后序遍历，左——右——根（递归）
    def __behind_order(self, target: Node):
        if target:
            self.__behind_order(target.left)
            self.__behind_order(target.right)
            print(target.data)

    # 层次遍历：使用队列
    def __floor_order(self):
        q = deque()
        q.append(self.root)
        item: Node
        # 只要队内不都是None
        while q:
            # 左出队
            item: Node = q.popleft()
            # 如果不是None
            if item:
                # 打印自己
                print(item.data)
                # 把自己的孩子放到队尾
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)

    def look(self, method=1):
        """
        :param method: 遍历方式。1：前序；2：中序；3：后序；4：层次遍历
        :return:
        """
        if method == 1:
            self.__pre_order(self.root)
        elif method == 2:
            self.__middle_order(self.root)
        elif method == 3:
            self.__behind_order(self.root)
        elif method == 4:
            self.__floor_order()


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    e.left = a
    e.right = g
    a.right = c
    c.left = b
    c.right = d
    g.right = f
    tree = BinaryTree(e)
    tree.look()
