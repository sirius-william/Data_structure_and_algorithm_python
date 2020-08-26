"""
列表长度为 n
一、思路1
    定义一个循环，每次取出一个列表中的最大或最小值，放到新的列表里，把原列表内的元素删除
    缺点：时间复杂度高，o(n^2)；创建了新列表
二、思路2
    分为有序区和无序区，把无序区最小的数与无序区第1个数交换，使其成为有序区中的最后元素
    无序区最后一个数不需要动，故需要跑n-1趟
"""


def select_sort(li: list):
    for i in range(len(li) - 1):
        # 假定无序区第一个数（索引）是最小值
        minNum = i
        # 无序区循环，从无序区第二个数开始循环
        for j in range(i + 1, len(li)):
            # 如果无序区当前数比假定的最小值小，则更新最小的数minNum
            if li[j] < li[minNum]:
                minNum = j
        # 将无序区第一个数和最小值交换位置，使无序区第一个数变为有序区
        temp = li[i]
        li[i] = li[minNum]
        li[minNum] = temp


li = [1, 3, 2, 6, 4, 5]
select_sort(li)
print(li)