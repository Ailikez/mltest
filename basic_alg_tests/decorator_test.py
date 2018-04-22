import functools
class DecoratorTest:
    __doc__ = '''
        在代码运行期间动态增加功能的方式，
        称之为“装饰器”（Decorator）。
        本质上，decorator就是一个返回函数的高阶函数。
    '''

    def __int__(self):
        pass

    def log(self, text):
        def decorator(func):
            # 注意下面这一句，相当wrapper.__name__ = func.__name__
            @functools.wraps(func)
            def wrapper(*args, **kw):
                '''456456'''
                print('%s %s():' % (text, func.__name__), func.__doc__)
                return func(*args, **kw)
            return wrapper
        return decorator

    def test(self, text):
        from datetime import date

        @self.log(text)
        def now():
            '''123123'''
            print(date.today())
        return now


if __name__ == '__main__':
    decorator_test = DecoratorTest()
    decorator_test.test("call")()
    # 下面这句验证@functools.wrapper的作用
    print(decorator_test.test("call").__name__)
    pass
