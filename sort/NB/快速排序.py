"""
快速排序
思路：
    1、取一个元素p（如第一个元素），使元素p归位
    2、归位后，列表被p分成两部分，左边都比p小，右边都比p大
    3、递归完成排序
框架：
def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)

效率：
    时间复杂度o(nlogn)
partition为归位函数
归位：
    把第一个数a拿出来存在变量里。
    定义剩下的最左边为left，最右边为right。
    从right开始往左遍历找到一个比a小的，然后写到left位置（不是交换，写之前left是个空位），在从left开始往右遍历找到一个比a大的写到right位置，交替进行
    当left=right时，将拿出来的a放到right=left所在位置
"""


# 归位函数
def partition(li, left, right):
    # 可以考虑随机选择应该位置的数与第一个数交换，解决最坏情况
    mid = li[left]
    while left < right:
        # right不断前移一直找到数比mid小的，left<right是为了加入被抽出的数恰好是最小的，此时会一直遍历到left与right重合，重合时应该跳出循环
        while li[right] >= mid and left < right:
            # right左移
            right -= 1
        li[left] = li[right]
        # left不断后移一直找到数比mid大的，假定前面right遍历之后，left=right，则不会进入这个循环
        while li[left] <= mid and left < right:
            # left右移
            left += 1
        li[right] = li[left]
    li[left] = mid
    # 返回mid值的索引，即left=right=mid
    return left


# 主函数
def quick_sort_main(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        # 递归处理mid左边的
        quick_sort_main(li, left, mid - 1)
        # 递归处理mid右边的
        quick_sort_main(li, mid + 1, right)


def quick_sort(li):
    left = 0
    right = len(li) - 1
    quick_sort_main(li, left, right)


l = [0, 7, 9, 4, 2, 3, 8]
quick_sort(l)
print(l)
