"""wcount.py: count words from an Internet file.

__author__ = "SunChengeng"
__pkuid__  = "1800011825"
__email__  = "1800011825@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import urllib.error


def wcount(lines, topn=10):
    import copy
    lines1 = copy.copy(lines)  # 对输入进行复制
    for letter in lines:
        if not (65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122):
            lines1 = lines1.replace(letter, ' ', 1)  # 将副本中非字母文本进行替换
    lst = lines1.split()
    counts = {}
    for word in lst:
        counts[word] = counts.get(word, 0) + 1  # 用字典进行统计
    tem_list = list(counts.items())
    sorted_list = sorted(tem_list, key=lambda t: t[1])
    if topn >= len(sorted_list):
        out_list = sorted_list[::-1]
    else:
        out_list = []
        for a in range(1, topn + 1):
            out_list.append(sorted_list[-a])  # 利用列表对结果进行排序
    out_dict = dict(out_list)
    return out_dict  # 返回输出字典
    pass


def main():
    try:
        doc = urlopen(sys.argv[1])
    except urllib.error.HTTPError:
        print('Please input valid URL')  # 网址错误的返回结果
    except urllib.error.URLError:
        print('Please check you Internet connection')
# 断网的返回结果
    else:
        doc = urlopen(sys.argv[1])
        lines = doc.read().decode()
        lines = lines.lower()  # 对URL返回值进行解码并转为小写
        if len(sys.argv) <= 2:
            topn = 10
        else:
            topn = int(sys.argv[2])  # 处理输入的topn
        dic = wcount(lines, topn)
        for i in dic:
            print(i + '    ' + str(dic[i]))  # 输出结果


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('url: URL of the txt file to analyze ')
        print('topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    else:
        main()
