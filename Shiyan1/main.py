import random
ListA = []
ListB = []
for i in range(0,20):
    n1 = random.randint(0,20)  #从0到20取随机数
    n2 = random.randint(0,20)
    ListA.append(n1)    #将n1添加到列表末尾
    ListB.append(n2)
print('A 列表:',ListA)
print('B 列表:',ListB)
ListC = ListA + ListB     #列表拼接
print('C 列表:',ListC)
print('C 列表中的奇数位置:', ListC[::2])   #list[i:j] 取数组第 i 到 第j 个的内容，list[i:j:2]的这里步长为2。
print('C 列表中的偶数位置:', ListC[1::2])
ListC.reverse()
print('逆序输出:',ListC)


ListC = set(ListA)&set(ListB)  #取交集
ListD = set(ListA)|set(ListB)  #取并集
ListE = set(ListA)-set(ListB)  #取差集
if not ListC:    #如果列表为空，则输出NONE类型
    ListC=None
if len(ListD)==0:
    ListD=None
if len(ListE)==0:
    ListE=None
print('交集新列表C:',list(ListC),"长度:",len(ListC),"类型：",type(ListC))
print('并集新列表D:',list(ListD),"长度:",len(ListD),"类型：",type(ListD))
print('差集新列表E:',list(ListE),"长度:",len(ListE),"类型：",type(ListE))


def TuplePrint(m=20):
    ListA = []
    ListB = []
    for i in range(m):
        temp0 = random.randint(0, 20)
        temp1 = random.randint(0, 20)
        ListA.append(temp0)
        ListB.append(temp1)
    ListC = ListA + ListB
    tup = (ListA,ListB,ListC)
    print("元组输出为：", tup)
TuplePrint()
#实现输出元组功能的函数

F1 = lambda x: x - x % 10   #定义一个函数，功能为将整数的个位数变为0.lambda 函数可接受任意数量的参数，但只能有一个表达式
print('1位整数检验：',F1(9))
print('2位整数检验：',F1(12))
print('3位整数检验：',F1(167))


A1 = list(map(F1, ListA))    #map() 会根据提供的函数对指定序列做映射。map(function函数, iterable序列, ...)
print('A列表函数检验:', A1)
B1 = list(map(F1, ListB))
print('B列表函数检验:', B1)


F2 = lambda x:str(x)[::-1]
print('x=12的逆序输出为：',F2(12))
print('x=1234的逆序输出为：',F2(1234))
print('x=3.14的逆序输出为：',F2(3.14))
