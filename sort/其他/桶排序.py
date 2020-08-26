"""
桶排序
对计数排序的改进
将列表按照区间（分段函数）分为很多部分，建立很多小列表，分别计数排序

效率：取决于数据的分布
"""


def count_sort(li, minNum, maxNum):
    count = {}
    for i in range(minNum, maxNum + 1):
        count[i] = 0
    for i in li:
        count[i] += 1
    li.clear()
    print(count)
    for i, j in count.items():
        li += [i] * j


def bucket_sort(li: list, n, maxNum):
    """
    :param li: 列表
    :param n: 桶的个数
    :param maxNum: 最大数
    """
    # 一个桶最多放多少个数
    x = maxNum // n
    buckets = [[] for i in range(n)]
    for i in li:
        # 确定桶的编号
        bucket_index = i // x
        if bucket_index > n - 1:
            bucket_index = n - 1
        buckets[bucket_index].append(i)
    li.clear()
    for i in buckets:
        count_sort(i, min(i), max(i))
        li += i
