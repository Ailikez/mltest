class EnumTest:
    def __init__(self):
        self.list_a = ['a', 'b', 'c']

    def do_test(self):
        print("list_a: ", self.list_a)
        print("after do enumerate:\n")
        print("for i, val in enumerate(self.list_a):\n\tprint(i,val,\\n)")
        for i, val in enumerate(self.list_a):
            print(i, val)
            print("\n")

    def do_another_test(self):
        print("for x, y in [(1, 1), (2, 4), (3, 9)]:\n\tprint(x,y,\\n)\n")
        for x, y in [(1, 1), (2, 4), (3, 9)]:
            print(x, y, '\n')


if __name__ == '__main__':
    test = EnumTest()
    test.do_test()
    test.do_another_test()