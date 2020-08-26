"""
归并排序
递归
分解：将列表越分越小，直至分成一个元素
终止条件：一个元素是有序的
合并：将两个有序列表合并，列表越来越大

时间复杂度：o(nlogn)
空间复杂度：o(n)   创建了临时列表
"""

# 归并
"""
思路：
    两段有序列表，分别有个头部指针，头部指针后移，每次移动一个指针，取出两个数最大的那个，并把被取出元素的那段指针后移，另一个指针不动
必须新建一个列表
"""


def merge(li, low, mid, high):
    """
    :param li: 列表
    :param low: 列表头部元素
    :param mid: 列表中间元素
    :param high: 列表尾部元素
    :return:
    """
    # 第一段列表头部指针
    i = low
    # 第二段列表头部指针
    j = mid + 1
    # 结果存储列表
    res = []
    # 第一段列表头部不能移动超过mid线，第二段列表头部指针不能移动超过尾部，保证两段指针都有数
    while i <= mid and j <= high:
        # 比较
        if li[i] < li[j]:
            # 拿出大的数，并把指针后移，另一个未取出元素的指针不动
            res.append(li[j])
            i += 1
        else:
            res.append(li[i])
            j += 1
    # while执行后，两部分一定有一部分没有数
    while i <= mid:
        # 第一段i未达到mid终点，表明第一段后面一定有数，第二段空了
        res.append(li[i])
        i += 1
    while j <= high:
        res.append(li[j])
        j += 1
    # 把结果写回li
    li[low: high + 1] = res


def merge_sort(li: list, low, high):
    # low = high时，代表只有一个元素
    if low < high:
        mid = (low + high) // 2
        # 分解左侧
        merge_sort(li, low, mid - 1)
        # 分解右侧
        merge_sort(li, mid + 1, high)
        # 合并，根据递归思想，上方函数最后一次递归跳出来后已经是一个2个只有1个元素的列表，而后执行下方的归并，第一次调用li是被归并元素个数为2的，跳入到上一次递归，再合并
        merge(li, low, mid, high)
