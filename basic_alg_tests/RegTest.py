import re


class RegTest:
    # 正则表达式测试.

    def __init__(self):
        self.test_str = '()(&%878423hjhdfsjkt提取的文本1231233'

    def do_match(self, test_str="?", match_rule=".*(提.*?本).*"):
        return re.match(match_rule, test_str)


if __name__ == '__main__':
    reg_test = RegTest()
    match_res = reg_test.do_match(test_str=reg_test.test_str)
    try:
        print(match_res.group(1))
    except Exception as err:
        print(err)
