#!/usr/bin/env python
# coding: utf-8

# In[20]:


def judge(list0,o,a,b,m):
    tim = 0
    tim1 = 0
    for y in range(a):
        for x in range(b):
            i = o + x + m*y
            if i in list0:
                tim = tim + 1
    
    for y in range(a):
        for x in range(b):
            i = o + y + m*x
            if i in list0:
                tim1 = tim1 + 1
    if tim == a*b and tim1 == a*b and o%m + max(a,b) <= m and a != b:
        return 1
    elif tim == a*b and (tim1 != a*b or o%m + a > m):
        return 2
    elif tim1 == a*b and (tim != a*b or o%m + b > m):
        return 3
    else:
        return False


def getlist(m,n):
    list0 = []
    for i in range(m*n):
        list0.append(i)
    return list0


def tile(m,n,a,b,lst):
    import copy
    list_out = []
    if lst == []:
        return []
    fir = min(lst)
    if judge(lst,fir,a,b,m) == False:
        return []
    
    if judge(lst,fir,a,b,m) == 1:
        part = []
        part1 = []
        tem_lst = []
        lstt = copy.copy(lst)
        for y in range(a):
            for x in range(b):
                i = fir + x + m*y
                lstt.remove(i)
                tem_lst.append(i)
        temp = tile(m,n,a,b,lstt)
        if temp == []:
            list_out = list_out + [tuple(tem_lst)]
        else:
            for i in temp:
                if type(i) == list:
                    part.append([tuple(tem_lst)] + i)
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
        temp1 = tile(m,n,a,b,lstt1)
        if temp1 == []:
            list_out = list_out + [tuple(tem_lst1)]
        else:
            for ii in temp1:
                if type(ii) == list:
                    part1.append([tuple(tem_lst1)] + ii)
                else:
                    part1 = part1 + [tuple(tem_lst1)] + temp1
                    break
        for i in part1:
            if type(i) == list:
                list_out.append(i)
            else:
                list_out.append(part1)
                break

    elif judge(lst,fir,a,b,m) == 2:
        tem_lst = []
        lstt = copy.copy(lst)
        for y in range(a):
            for x in range(b):
                i = fir + x + m*y
                tem_lst.append(i)
                lstt.remove(i)
        temp = tile(m,n,a,b,lstt)
        if temp == []:
            list_out = list_out + [tuple(tem_lst)]
        else:
            for i in temp:
                if type(i) == list:
                    list_out.append([tuple(tem_lst)] + i)
                else:
                    list_out = list_out + [tuple(tem_lst)] + temp
                    break

    elif judge(lst,fir,a,b,m) == 3:
        lstt = copy.copy(lst)
        tem_lst = []
        for y in range(a):
            for x in range(b):
                i = fir + y + m*x
                tem_lst.append(i)
                lstt.remove(i)
        temp = tile(m,n,a,b,lstt)
        if temp == []:
            list_out = list_out + [tuple(tem_lst)]
        else:
            for i in temp:
                if type(i) == list:
                    list_out.append([tuple(tem_lst)] + i)
                else:
                    list_out = list_out + [tuple(tem_lst)] + temp
                    break
    return list_out

def main():
    m = int(input('m='))
    n = int(input('n='))
    a = int(input('a='))
    b = int(input('b='))
    lst = getlist(m,n)
    result = tile(m,n,a,b,lst)
    for i in range((len(result))):
        if len(result[i]) == m*n/(a*b):
            print(str(i+1) + ': ' + str(result[i]))
    print(len(result))
if __name__ == '__main__':
    main()


# In[ ]:




