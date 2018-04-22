class ClosureTest:
    __doc__ = '''
     返回闭包时牢记一点：
     返回函数不要引用任何循环变量，
     或者后续会发生变化的变量。
    '''

    def __int__(self):
        pass

    def counter_bad(self):
        fs = []
        for i in range(1, 4):
            def f():
                return i * i
            fs.append(f)
        return fs

    def counter_good(self):
        def f(i):
            def g():
                return i * i
            return g
        fs = []
        for j in range(1, 4):
            fs.append(f(j))
        return fs

    def counter_self_add(self):
        n = 0

        def f():
            nonlocal n
            n += 1
            return n
        return f


if __name__ == '__main__':
    closure_test = ClosureTest()
    print("闭包错误演示")
    print([i() for i in closure_test.counter_bad()])
    print("闭包正确演示")
    print([i() for i in closure_test.counter_good()])
    print("自增函数演示")
    f = closure_test.counter_self_add()
    print([f() for i in range(1, 11)])
    pass
