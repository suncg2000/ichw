def exchange(currency_from, currency_to, amount_from):  # 定义函数 #
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' +
                  currency_from + '&to=' + currency_to + '&amt=' + amount_from)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')  # 从网站获取并解析字符串 #
    list1 = list(jstr.split('"'))  # 在"处切片字符串 #
    message = list1[7]  # 取列表第八项获得兑换货币信息 #
    message = message.split()
    amount_to = message[0]  # 提取兑换货币数值 #
    return amount_to

''' 货币兑换模块
该模块提供了几个字符串解析函数来实现
使用在线货币服务的简单货币兑换例程。
这个模块的主要功能是交换。 '''


def test1():
    assert (exchange('USD', 'EUR', '100') == '86.3569')


def test2():
    assert (exchange('CNY', 'USD', '100') == '14.594066052743')


def test3():
    assert (exchange('JPY', 'CNY', '100') == '6.1509528810851')  # 测试三次货币兑换结果 #


def testAll():
    """test all cases"""
    test1()
    test2()
    test3()
    print("All tests passed")


'''测试模块
该模块创建了3个测试函数来验证exchange函数能否正常运行'''


def main():
    currency_from = input('currency from')
    currency_to = input('currency to')
    amount_from = input('amount of money')  # 输入数据 #
    testAll()
    print(amount_from + ' ' + currency_from + ' is ' +
          exchange(currency_from, currency_to, amount_from) + ' ' + currency_to)

if __name__ == '__main__':
    main()

# 运行模块 #
# 本模块提供了用户向程序输入数据并获得函数执行结果的路径 #
