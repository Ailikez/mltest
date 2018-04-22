class ListGenTest:
    def __init__(self):
        self.mylist = []

    def genlist_use_listfunc(self):
        print(">>>list(range(1, 11))")
        self.mylist = list(range(1, 11))
        print(self.mylist)

    def genlist_use_bracket(self):
        print(">>>[x for x in range(1, 11) if x > 0]")
        self.mylist = [x for x in range(1, 11) if x > 0]
        print(self.mylist)

    def genlist_use_2for(self):
        print(">>>[x + y for x in ('1', '2', '3') for y in ('1', '2', '3')]")
        print([x + y for x in ('1', '2', '3') for y in ('1', '2', '3')])


if __name__ == '__main__':
    listgentest = ListGenTest()
    listgentest.genlist_use_listfunc()
    listgentest.genlist_use_bracket()
    listgentest.genlist_use_2for()