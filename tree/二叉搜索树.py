"""
二叉搜索树满足：
    左子树小于根，右子树大于根
包括：查询、插入、删除
效率：o(logn)
最坏情况：每个节点的子节点都最多只有一个（变成了链表），从树形结构退化为线性结构。o(n)
解决：
    随机化插入
    AVL树
"""
from tree.二叉树 import *


class SelectTree(BinaryTree):
    def __init__(self, rootNode, baseList: list = None):
        self.__sort_list = []
        super().__init__(rootNode)
        if baseList:
            for item in baseList:
                self.insert(item)

    # 插入（递归方式遍历）
    def __insert(self, target, val):
        # 如果是叶子，则直接与根比较进行添加
        if not target.left and not target.right:
            if val < target.data:
                newNode = Node(val)
                target.left = newNode
                newNode.father = target
                return
            elif val > target.data:
                newNode = Node(val)
                target.right = newNode
                newNode.father = target
                return
        # 如果不是叶子，即left与right至少一个不是None
        while target.left or target.right:
            # 如果val小于根，且恰好left为None
            if val < target.data and (target.left is None):
                newNode = Node(val)
                target.left = newNode
                newNode.father = target
                return
            # 如果val大于根，且恰好right为None
            elif val > target.data and (target.right is None):
                newNode = Node(val)
                target.right = newNode
                newNode.father = target
                return
            # 如果left与right都不是None，则：
            else:
                # 如果值大于根，则递归right节点
                if val > target.data:
                    self.__insert(target.right, val)
                # 如果值小于根，则递归left节点
                elif val < target.data:
                    self.__insert(target.left, val)
            return

    # 非递归方式插入
    def __insert2(self, val):
        temp = self.root
        while temp.left or temp.left:
            if val < temp.data:
                if not temp.left:
                    newNode = Node(val)
                    temp.left = newNode
                    newNode.father = temp
                    return
                else:
                    temp = temp.left
            elif val > temp.data:
                if not temp.right:
                    newNode = Node(val)
                    temp.right = newNode
                    newNode.father = temp
                    return
                else:
                    temp = temp.right
        if not temp.left and not temp.right:
            if val < temp.data:
                newNode = Node(val)
                temp.left = newNode
                newNode.father = temp
            elif val > temp.data:
                newNode = Node(val)
                temp.right = newNode
                newNode.father = temp

    def insert(self, val, quick=True):
        if self.get(val):
            return False
        if quick:
            self.__insert2(val)
        else:
            self.__insert(self.root, val)
        return True

    # 判断值是否存在
    def get(self, val, returnRoot=False, target=None):
        if not target:
            temp = self.root
        else:
            temp = target
        while temp:
            if temp.data == val:
                if returnRoot:
                    return temp
                else:
                    return True
            elif val < temp.data:
                temp = temp.left
            elif val > temp.data:
                temp = temp.right
        return False

    # 删除
    def delete(self, val):
        if not self.get(val):
            return False
        temp: Node = self.get(val, returnRoot=True)
        # 获取节点性质
        nature = self.getItem(temp)
        position = nature["position"]
        # 如果是叶子
        if nature["child"] == [None, None]:
            if position == 0:
                temp.father.left = None
            elif position == 1:
                temp.father.right = None
        if not nature["father"]:
            # 如果是根节点
            return False
        else:
            # 如果只存在一个子节点
            if None in nature["child"]:
                nature["child"].remove(None)
                if position == 0:
                    temp.father.left = nature["child"][0]
                elif position == 1:
                    temp.father.right = nature["child"][0]
            else:
                # 如果左右节点都存在，找出当前节点右子树中的最小值节点，删除这个最小值节点，把当前节点的值变为这个最小节点的值，这个最小值节点一定是某左节点，一直遍历left即可
                right_tree: Node = temp.right
                # 遍历右子树中所有的左子节点，最小值为第一个左子节点为None的那个节点
                while right_tree.left:
                    right_tree = right_tree.left
                # 存值
                newData = right_tree.data
                # 删除这个最小值子节点
                right_tree_nature = self.getItem(right_tree)
                right_tree_position = right_tree_nature["position"]
                if right_tree_position == 0:
                    right_tree.father.left = right_tree.right
                elif right_tree_position == 1:
                    right_tree.father.right = right_tree.right
                # 目标节点赋值
                temp.data = newData

    # 有序输出，中序遍历，左根右为升序，右根左为降序
    def __sort(self, target: Node, reverse=False):
        if reverse:
            if target:
                self.__sort(target.right, reverse)
                print(target.data)
                self.__sort(target.left, reverse)
        else:
            self.look(2)

    def sort(self, reverse=False):
        self.__sort(self.root, reverse)

    # 返回节点的性质
    @staticmethod
    def getItem(target: Node):
        res = {"father": [], "child": [], "position": 0}
        # 父节点所有的子节点
        res["father"].append(target.father.left)
        res["father"].append(target.father.right)
        # 所有子节点
        res["child"].append(target.left)
        res["child"].append(target.right)
        # 父节点的相对位置，0为父节点的左子节点，1为父节点的右子节点
        if target.father.left == target:
            res["position"] = 0
        else:
            res["position"] = 1
        return res


if __name__ == "__main__":
    root = Node(17)
    x = SelectTree(root)
    li = [17, 5, 35, 2, 11, 29, 38, 9, 16, 7, 8]
    for i in li:
        x.insert(i, quick=False)
    # x.look(2)
    x.sort(reverse=True)
