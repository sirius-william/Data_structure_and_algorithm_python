"""
稀疏数组
"""
import copy


class SparseList(object):
    @staticmethod
    def listToSparse(inputList: list, free):
        head = []
        resPart = []
        try:
            rowCount = len(inputList)
            columnCount = len(inputList[1])
            # 检查各行长度是否相同
            for i in inputList:
                if len(i) != columnCount:
                    return False
            count = 0
            for row in range(0, rowCount):
                for column in range(0, columnCount):
                    num = inputList[row][column]
                    if num != free:
                        count += 1
                        new = [row, column, inputList[row][column]]
                        resPart.append(new)

            head.append([rowCount, columnCount, count])
            res = head + resPart
            return res

        except Exception as e:
            print(e)

    @staticmethod
    def sparseToList(sparse: list, free):
        res = []
        rowCount = sparse[0][0]
        columnCount = sparse[0][1]
        count = sparse[0][2]
        column = [free] * columnCount
        for i in range(0, rowCount):
            # column为引用类型，需要深拷贝，不能res.append(column)，一定要注意，这bug我tm找了好久
            res.append(copy.deepcopy(column))
        for j in range(1, len(sparse)):
            x = sparse[j][0]
            y = sparse[j][1]
            num = sparse[j][2]
            res[x][y] = num
        return res
