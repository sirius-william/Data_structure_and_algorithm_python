"""
列表长度为n，分为有序区和无序区
循环走了i=n-1趟，每走一趟，有序区多一个数，每一趟比较n-i-1次，-1是因为无序区最后一个数不需要比较
时间复杂度：o(n^2)
"""

import random


def bubble_sort(li):
    count = 0
    for i in range(len(li) - 1):
        if_sort = True
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j + 1]:
                x = li[j + 1]
                li[j + 1] = li[j]
                li[j] = x
                # 改进：增加一个变量，表示当前循环下是否有冒泡改到
                if_sort = False
                count += 1
        # 如果发现为True，则代表当前趟没发生冒泡，代表已经排序完成，不需要再往下走了，可以结束程序
        if if_sort:
            break


li = [random.randint(0, 100000) for i in range(20)]
li2 = [2, 1, 3, 4, 5]
bubble_sort(li2)
print(li2)
