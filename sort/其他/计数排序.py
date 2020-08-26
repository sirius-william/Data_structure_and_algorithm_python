"""
对列表进行排序，已知列表中的数范围，通过计数的方式统计每个数的个数，然后按个数重写列表
比较取巧，但很有用，可以通过字典这种链表来解决内存连续的问题
时间复杂度：o(n)
"""


def count_sort(li, minNum, maxNum):
    count = {}
    for i in range(minNum, maxNum + 1):
        count[i] = 0
    for i in li:
        count[i] += 1
    li.clear()
    for i, j in count.items():
        li += [i] * j
    del count


l = [2, 3, 4, 5, 2, 3, 1, 9, 8, 3]
count_sort(l, 1, 9)
print(l)
