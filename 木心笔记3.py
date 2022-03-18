# 算术运算符
print(1+1)  # 加法运算
print(2-1)  # 减法运算
print(2*4)  # 乘法运算
print(1/2)  # 除法运算
print(11//2)  # 整除运算
print(11 % 2)  # 取余运算
print(2**2)  # 表示2的2次方
print(2**3)  # 表示2的3次方
# 数字为一正一负时的整除、取余
print(9//4)  # 2
print(-9//-4)  # 2
print(9//-4)  # -3
print(-9//4)  # -3
print(9 % -4)  # -3
print(-9 % 4)  # 3   取余的公式为 余数=被除数-除数*商
# python中遵循的原则是使两个数的商尽可能的小
# 赋值运算符，运算顺序是从右往左
i = 3+4
# 1、支持链式赋值,多个变量所用的id是一样的
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))
# 2、支持参数赋值
print('支持参数赋值')
a = 20
a += 30  # 相当于a=a+30
print(a)
a -= 10  # 相当于a=a-10
print(a)
a *= 2  # 相当于a=a*2
print(a, type(a))
a /= 8  # 相当于a=a/8
print(a, type(a))
a //= 2  # 相当于求2的整除
print(a)
# 3、支持系列解包赋值
a, b, c = 20, 30, 40
print(a, b, c, id(a), id(b), id(c))  # 依次赋值，变量数要和数字数量相同
# 实现变量值互换
a, b = 10, 20
print('交换之前', a, b)
a, b = b, a
print('交换之后', a, b)
# 比较运算符
a, b = 10, 20
print('a>b吗？', a > b)  # False
print('a<b吗?', a < b)  # True
print('a<=b吗？', a <= b)  # True
print('a>=b吗？', a >= b)  # False
print('a==b吗?', a == b)  # False
print('a!=b吗？', a != b)  # True
'''一个=是赋值运算符，两个==是比较运算符
两个变量比较的是值
比较对象的标识使用 is
即比较对象的id'''
a = 10
b = 10
print(a == b)  # True 说明a与b的value相等
print(a is b)  # True 说明a与b的id标识相等
# 当代数赋值时如果b的值与a的值相等，则b会直接与a相同，地址与值均相同
# 以下代码没有学过
lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # True
print(lst1 is lst2)  # False
print(id(lst1))
print(id(lst2))
print(a is not b)  # False a的id与b的id是相等的
print(lst1 is not lst2)  # True lst1与lst2的id是不相等的
# 布尔运算符
# 1、and
a, b = 1, 2
print(a == 1 and b == 2)  # True and True  True
print(a == 1 and b < 2)  # True and False  False
print(a != 1 and b == 2)  # False and True  False
print(a != 1 and b != 2)  # False and False  False
# 结果实际上相当于与的关系
# 2、or
print(a == 1 or b == 2)  # True or True  True
print(a == 1 or b < 2)  # True or False  True
print(a != 1 or b == 2)  # False or True  True
print(a != 1 or b != 2)  # False or False  False
# 实际上结果相当于或的关系
# 3、not
f1 = True
f2 = False
print(not f1)  # False
print(not f2)  # True
# 4、in，not in
s = 'hello world'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
# 位运算
# 1、按位与运算,符号为&
# 例   00000100   4
#      00001000   8      对上面这两个数按位进行与运算结果为00000000
print(4 & 8)
# 2、按位或运算，符号为|
# 还是以上面的为例，其结果应该为00001100，转换成二进制结果为12
print(4 | 8)
# 3、左移位运算符
# 向左移动一个位置
# 高位溢出，低位补0.即高位直接删掉，低位补上0
# 向左移动一位相当于乘以2
print(4 << 1)
print(4 << 2)
print(4 << 3)
# 4、右移位运算符
# 低位截断，高位补0
# 向右移动一位相当于除以2
print(4 >> 1)
print(4 >> 2)
print(4 >> 3)
# 运算符的优先级
# 算术运算符>位运算>比较运算符>布尔运算符>赋值运算符
# 1、算术运算符：幂运算>乘除运算>加减运算
# 2、位运算：
# 3、比较运算符：
# 4、布尔运算符：
# 5、赋值运算符：
# 有括号则应该优先计算括号内部


