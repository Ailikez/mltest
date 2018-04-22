from functools import reduce


class MapReduceTest:
    __doc__ =\
        '''
    map()函数接收两个参数，
    一个是函数，一个是Iterable，
    map将传入的函数依次作用到序列的每个元素，
    并把结果作为新的Iterator返回。
    reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
    这个函数必须接收两个参数，
    reduce把结果继续和序列的下一个元素做累积计算.
    '''

    def __init__(self):
        self.seq = [1, 2, 3, 4, 5, 6]
        self.DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def _square(self, x):
        return x * x

    def char2num(self, s):
        return self.DIGITS[s]

    def str2int(self, s):
        return reduce(lambda x, y: x * 10 + y, map(self.char2num, s))

    def _add(self, x, y):
        return x * 10 + y

    def map_test(self):
        print('>>>def my_func(self, x, y):\n\treturn x*y')
        print(">>>type(map(self.my_func, seq))")
        print(type(map(self._square, self.seq)))
        print(">>>seq")
        print(self.seq)
        print(">>>list(map(self.my_func, self.seq))")
        print(list(map(self._square, self.seq)))

    def reduce_test(self):
        print('>>>seq')
        print(self.seq)
        print(">>>def _add(self, x, y):\n\treturn x*10+y")
        print(">>>reduce(_add, self.seq)")
        print(reduce(self._add, self.seq))


if __name__ == '__main__':
    map_reduce_test = MapReduceTest()
    map_reduce_test.map_test()
    map_reduce_test.reduce_test()
    print(">>str2int('123456')")
    print(map_reduce_test.str2int('123456'))
