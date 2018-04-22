from functools import partial


class PartialFuncTest:
    __doc__ = '''
    简单总结functools.partial的作用就是，
    当函数的参数个数太多，需要简化时，
    使用functools.partial可以创建一个新的函数，
    这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
    '''

    def __init__(self):
        self.int2 = partial(int, base=2)
        print(">>>int2 = partial(int, base=2)")


if __name__ == '__main__':
    test = PartialFuncTest()
    print(">>>int2('1010001')")
    print(test.int2('1010001'))
    pass
