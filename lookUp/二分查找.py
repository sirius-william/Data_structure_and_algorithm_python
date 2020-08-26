def looUp(li, val):
    # 如果是降序，则改为升序
    if li[0] > li[-1]:
        li = li[::-1]

    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if val < li[mid]:
            # 如果目标值小于中间元素值，则让right指针指向中间元素左侧的那个元素，即 mid-1
            right = mid - 1
        elif val > li[mid]:
            # 如果目标值大于中间元素值，则让left指针指向中间元素右边1个的那个元素，即 mid+1
            left = mid + 1
        else:
            return mid

    return -1


x = [1, 2, 3, 4]
y = looUp(x, 4)
print(y)
# python中，index()函数是线型查找方式，因为二分查找的前提是要排序，而index()函数传入的列表不一定是排序的
