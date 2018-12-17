'''__author__ = "SunChengeng"
__pkuid__  = "1800011825"
__email__  = "1800011825@pku.edu.cn"'''


def judge(list0, o, a, b, m):
    tim = 0
    tim1 = 0
    for y in range(a):
        for x in range(b):
            i = o + x + m*y
            if i in list0:
                tim = tim + 1  # 判断砖块能否横铺

    for y in range(a):
        for x in range(b):
            i = o + y + m*x
            if i in list0:
                tim1 = tim1 + 1  # 判断砖块能否纵铺

    if tim == a*b and tim1 == a*b and o % m + max(a, b) <= m and a != b:
        return 1  # 矩形砖块可以横铺与纵铺返回1
    elif tim == a*b and (tim1 != a*b or o % m + a > m or a == b):
        return 2  # 矩形砖块只能横铺或砖块为正方形，返回2
    elif tim1 == a*b and (tim != a*b or o % m + b > m):
        return 3  # 矩形砖块只能纵铺，返回3
    else:
        return False
'''判断模块
本模块用于对给定的列表（墙面）与初始值，
判断瓷砖在该墙面上是否可以铺开以及可以怎样铺开'''


def getlist(m, n):
    list0 = []
    for i in range(m*n):
        list0.append(i)
    return list0
'''列表生成模块
本模块用于生成墙列表'''


def tile(m, n, a, b, lst):
    import copy
    list_out = []
    if lst == []:
        return []
    fir = min(lst)
    if judge(lst, fir, a, b, m) is False:
        return []  # 墙列表最小值上不能铺砖或墙列表为空，返回空列表，结束递归

    if judge(lst, fir, a, b, m) == 1:
        part = []
        part1 = []
        tem_lst = []
        lstt = copy.copy(lst)
        for y in range(a):
            for x in range(b):
                i = fir + x + m*y
                lstt.remove(i)
                tem_lst.append(i)
        temp = tile(m, n, a, b, lstt)
        if temp == []:
            part = part + [tuple(tem_lst)]
        else:
            for i in temp:
                if type(i) == list:
                    part.append([tuple(tem_lst)] + i)  # 防止返回列表超过二维
                else:
                    part = part + [tuple(tem_lst)] + temp
                    break
        for i in part:
            if type(i) == list:
                list_out.append(i)
            else:
                list_out.append(part)
                break
        tem_lst1 = []
        lstt1 = copy.copy(lst)
        for y in range(a):
            for x in range(b):
                i = fir + y + m*x
                tem_lst1.append(i)
                lstt1.remove(i)
        temp1 = tile(m, n, a, b, lstt1)
        if temp1 == []:
            part1 = part1 + [tuple(tem_lst1)]
        else:
            for ii in temp1:
                if type(ii) == list:
                    part1.append([tuple(tem_lst1)] + ii)  # 防止返回列表超过二维
                else:
                    part1 = part1 + [tuple(tem_lst1)] + temp1
                    break
        for i in part1:
            if type(i) == list:
                list_out.append(i)  # 防止返回列表超过二维
            else:
                list_out.append(part1)
                break
# 对于既能横铺又能纵铺的情况，进行分支处理，分别进行递归并返回结果,
# 并利用临时列表part，part1暂时存储结果并最终加入输出列表

    elif judge(lst, fir, a, b, m) == 2:
        tem_lst = []
        lstt = copy.copy(lst)
        for y in range(a):
            for x in range(b):
                i = fir + x + m*y
                tem_lst.append(i)
                lstt.remove(i)
        temp = tile(m, n, a, b, lstt)
        if temp == []:
            list_out = list_out + [tuple(tem_lst)]
        else:
            for i in temp:
                if type(i) == list:
                    list_out.append([tuple(tem_lst)] + i)  # 防止返回列表超过二维
                else:
                    list_out = list_out + [tuple(tem_lst)] + temp
                    break
# 对于只能横铺或只能纵铺的情况，除无需分支外与第一种情况类似

    elif judge(lst, fir, a, b, m) == 3:
        lstt = copy.copy(lst)
        tem_lst = []
        for y in range(a):
            for x in range(b):
                i = fir + y + m*x
                tem_lst.append(i)
                lstt.remove(i)
        temp = tile(m, n, a, b, lstt)
        if temp == []:
            list_out = list_out + [tuple(tem_lst)]
        else:
            for i in temp:
                if type(i) == list:
                    list_out.append([tuple(tem_lst)] + i)  # 防止返回列表超过二维
                else:
                    list_out = list_out + [tuple(tem_lst)] + temp
                    break
    return list_out
'''铺砖模块
本模块通过递归方法生成铺砖结果，并返回结果列表'''


def wall(m, n):
    import turtle
    t = turtle.Pen()
    t.speed(0)
    for i in range(m*n):
        t.penup()
        t.goto(50*(i//m), 50*(i % m))
        t.pendown()  # 控制乌龟在墙中每一个点绘制一个正方形
        for a in range(4):
            t.forward(50)
            t.left(90)
        t.penup()
        t.goto(50*(i//m) + 25, 50*(i % m) + 25)
        t.pendown()
        t.write(str(i), False, "left", ("Arial", 8, "normal"))  # 在每一个正方形中间绘制数字
'''墙模块
本模块用于墙的可视化'''


def sight(m, a, b, lst):
    import turtle
    t1 = turtle.Pen()
    t1.speed(0)
    t1.pencolor('red')
    t1.pensize(3)
    for i in lst:  # 取输出列表中一项
        x = min(i)
        y = max(i)
        t1.penup()
        t1.goto(50*(x//m), 50*(x % m))
        t1.pendown()
        if y == x + (a - 1) + (b - 1)*m:  # 判断砖块摆放方式
            for i in [1, 2]:
                t1.fd(50*b)
                t1.left(90)
                t1.fd(50*a)
                t1.left(90)  # 绘制砖块
        else:
            for i in [1, 2]:
                t1.fd(50*a)
                t1.left(90)
                t1.fd(50*b)
                t1.left(90)
'''可视化模块
本模块用于对用户选定的铺砖结果进行可视化'''


def main():
    m = int(input('m='))
    n = int(input('n='))
    a = int(input('a='))
    b = int(input('b='))
    lst = getlist(m, n)
    result = tile(m, n, a, b, lst)
    result1 = []
    if type(result[0]) == tuple:
        print('一共有1种答案')
        result1.append(result)
        print('1: ' + str(result))
    else:
        for i in range((len(result))):
            if len(result[i]) == m*n/(a*b):
                result1.append(result[i])  # 筛选输出列表中有效结果
        print('一共有' + str(len(result1)) + '种答案')
        for i in range((len(result1))):
            print(str(i+1) + ': ' + str(result1[i]))  # 输出结果数量与结果
    if len(result1) != 0:  # 如果结果数量大于零，则继续进行可视化
        wall(m, n)
        kind = input('要可视化的种类：')
        lst0 = result1[(int(kind) - 1)]
        sight(m, a, b, lst0)
'''运行模块
本模块具体执行以上函数，输出有效结果并根据需要进行可视化'''


if __name__ == '__main__':
    main()
