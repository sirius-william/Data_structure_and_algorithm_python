"""
按数字的每一位进行分桶，然后进行排序
时间复杂度：o(kn)，k为数最大位数，按照线性时间，o(n)
空间复杂度：o(k+n)
"""


def radix_sort(li: list):
    # 根据最大数的位数决定做几次循环
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        # 多次建桶，装桶，然后排序
        bucket = [[] for i in range(10)]
        for i in li:
            digit = (i // 10 ** it) % 10
            bucket[digit].append(i)
        li.clear()
        for buc in bucket:
            li += buc
        it += 1
