class GeneratorTest:
    __doc__ = '''
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，
它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，
不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的
    '''

    def __init__(self):
        self.mygen = None

    def gen_basic_gen(self):
        self.mygen = (i for i in range(1, 11))
        print(">>>mygen = (i for i in range(1, 11))\n>>>type(mygen)")
        print(type(self.mygen))
        print(">>>for i in mygen:\n\tprint(i)")
        for i in self.mygen:
            print(i)

    def fib_generator(self, maximum):
        n, a, b = 0, 0, 1
        while n < maximum:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done'

    def gen_use_fib_generator(self):
        g = self.fib_generator(6)
        print("def fib_generator(self, maximum):\
        \n\tn, a, b = 0, 0, 1\
        \n\twhile n < maximum:\
            \n\t\tyield b\
            \n\t\ta, b = b, a + b\
            \n\t\tn = n + 1\
        \n\treturn 'done'")
        print("g = fib_generator(6)")
        print(type(g))
        print("for i in g:\n\tprint(i)")
        for i in g:
            print(i)


if __name__ == '__main__':
    generator_test = GeneratorTest()
    print(generator_test.__doc__, '\n')
    # generator_test.gen_basic_gen()
    generator_test.gen_use_fib_generator()