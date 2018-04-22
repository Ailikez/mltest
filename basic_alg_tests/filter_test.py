class FilterTest:
    __doc__ = '''
    和map()类似，filter()也接收一个函数和一个序列。
    和map()不同的是，filter()把传入的函数依次作用于每个元素，
    然后根据返回值是True还是False决定保留还是丢弃该元素。
    '''

    def __init__(self):
        self.seq = None
        pass

    def oddnums_iter(self):
        n = 1
        while True:
            n = n + 2
            yield n

    def filtered_nums(self):
        yield 2
        self.seq = self.oddnums_iter()
        while True:
            n = next(self.seq)
            yield n
            self.seq = filter(self._not_divisible(n), self.seq)

    def _not_divisible(self, n):
        return lambda x: x % n > 0

    def do_test(self):
        n = 0
        for i in self.filtered_nums():
            if i > 1000:
                break
            else:
                print(i)
            n += 1
        print(">>>", n, "个")


if __name__ == '__main__':
    filter_test = FilterTest()
    filter_test.do_test()
