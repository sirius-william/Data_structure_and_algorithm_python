"""
列表长度：n
思路：从无序区拿出第一个数插入到有序区正确的位置里
第一个数不需要执行算法，自动为有序区，故需要执行n-1趟
"""

import time
import random
import copy


# 方式一：被抽出的数介于2个相邻数之间，速度慢
# 时间复杂度：o(n^3)
def insert_sort(li: list):
    # 有序区为[0,i)， 无序区为[i, 最后)，i为趟数，即无序区第一个数
    for i in range(1, len(li)):
        # 抽出被比较的数，
        x = i
        # j 为有序区
        for j in range(0, i):
            if j == 0:
                if li[x] < li[j]:
                    temp = li[j: i]
                    li[j] = li[x]
                    li[j + 1:i + 1] = temp
            else:
                if li[j - 1] <= li[x] < li[j]:
                    # 介于两个相邻数之间时
                    temp = li[j: i]
                    li[j] = li[x]
                    li[j + 1:i + 1] = temp


# 方式二：判断每一个有序区，如果被抽出的数小于被循环的有序区的数，则把这个数往后移动一个位置。
# 时间复杂度：2层循环o(n^2)
def insert_sort2(li: list):
    # i为无序区
    for i in range(1, len(li)):
        # 被从无序区抽出
        x = li[i]
        # j为有序区
        j = i - 1
        # 从后往前查找有序区，一直到查找出第一个不大于被抽出的数的那个位置
        while j >= 0 and x < li[j]:
            # 被抽出元素与有序区每个数比较，小于则把当前遍历的有序区的数往后移动
            li[j + 1] = li[j]
            j -= 1
        # 循环结束后把空余位置填上（当前j后面的位置，画个图想一想就能看出来了）
        li[j + 1] = x


l = [random.randint(0, 100000) for i in range(10000)]
y = copy.deepcopy(l)
time1 = time.time() * 1000
insert_sort2(l)
print(time.time() * 1000 - time1)
time2 = time.time() * 1000
insert_sort(y)
print(float(time.time()) * 1000 - time2)
