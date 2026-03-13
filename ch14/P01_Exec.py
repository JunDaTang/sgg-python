"""
    该案例讲解晨测题
"""
"""
# 创建一个简单的 Python 模块math_operations.py，其中定义两个函数add和multiply，
# 分别用于实现两个数的加法和乘法运算。在另一个 Python 文件中导入该模块，并调用这两个函数计算3 + 5和3 * 5的结果。
# import P00_math_operation
# print(P00_math_operation.add(2,3))
# print(P00_math_operation.mul(2,3))

# from P00_math_operation import *
# print(add(2,3))
# print(mul(2,3))


# from P00_math_operation import add,mul
# print(add(2,3))
# print(mul(2,3))
"""
"""
# 使用生成器表达式创建一个生成器，生成 1 到 10 的偶数。然后使用for循环遍历该生成器，打印每个偶数
gen = (i for i in range(1,11) if i % 2==0)
for i in gen:
    print(i)


"""
"""
# 创建一个迭代器类MyIterator，用于遍历一个给定列表的元素。实现__iter__和__next__方法。
# 使用该迭代器类遍历列表[10, 20, 30, 40]，并打印每个元素。
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        self.index = self.index + 1
        return self.data[self.index]
"""
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        res = self.data[self.index]
        self.index = self.index + 1
        return res
it = MyIterator([10,20,30,40])
for i in it:
    print(i)

