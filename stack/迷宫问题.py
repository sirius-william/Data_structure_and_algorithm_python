"""
栈——深度优先搜索（一条路走到黑，死胡同再回来）
回溯法
思路：从一个节点开始，任意找一个能走的店，当找到不能走的点时，退回到上一个点寻找是否有其他方向的点。
使用栈存储当前路径,走到下一个点为入栈，回退到前一个点为出栈。
1是墙，0是可走的空地
"""
from stack import _stack

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def maze_path(x1, y1, x2, y2):
    """
    :param x1, y1: 起点坐标
    :param x2, y2: 终点坐标
    """
    start = (x1, y1)
    end = (x2, y2)
    # 当前位置，now[0]：x轴；now[1]：y轴
    # 搜索顺序，上下左右，上：y+1；下：y+1；左：x-1；右：x+1
    now: tuple
    stack = _stack.Stack()
    stack.push(start)
    while not stack.is_empty():
        now = stack.get_top()
        if now == end:
            break
        else:
            # 标记当前位置是已经走过的节点
            maze[now[0]][now[1]] = 2
            # 上
            up = (now[0], now[1] - 1)
            # 下
            down = (now[0], now[1] + 1)
            # 左
            left = (now[0] - 1, now[1])
            # 右
            right = (now[0] + 1, now[1])
            directions = [up, down, left, right]
            # 遍历所有4个方向，直到找到第1个能走的方向
            for direction in directions:
                if maze[direction[0]][direction[1]] == 0:
                    # 发现当前查看的方向没走过，则把下一个方向push进栈，然后跳出循环
                    stack.push(direction)
                    break
            # 当发现上面四个方向都不能走时，把当前位置pop出栈，进入下一次循环
            else:
                stack.pop()
    if stack.is_empty():
        print("没有路")
    for i in stack.as_list():
        print(i)


maze_path(1, 1, 6, 8)
