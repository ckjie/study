# print('hello python')

# # name = input('please enter your name: ');
# # print('hello', name)

# # '#'用于注释
# # 以 ： 结尾时，缩进的语句视为代码块
# # 使用缩进来组织代码块
# a = 100
# if a > 0:
# 	print('a > 0')
# else:
# 	print('a < 0')

# isinstance：可用于类型的判断：isinstance(x, (int, str, float))

# # 允许使用 r'' 表示 '' 内部的字符串默认不转义
# # \\n\t\\
# print(r'\\n\t\\')

# # 允许使用 '''...''' 的格式标识多行内容
# # line1
# # line2
# # line3
# print('''line1
# line2
# line3''')

# # 布尔值：True False，多个条件可使用 and 、or 、not 连接（相对于js的 && 、|| 、! ）
# # 布尔为false的值有： 0、空字符串、空数组、None
# # 空值：None
# # 使用 // 进行地板除，即除尽或除不尽都取整，
# print('10 / 3 =', 10 / 3)		# 3.3333333333...
# print('10 // 3 =', 10 // 3)		# 3

# # 测试字符串插值
# # %s 替换字符串类型的值，%d 替换整数类型的值，%f 替换浮点数类型的值，%x 替换十六进制整数的值
# # 用 % 进行连接，当只有一个插值时，可以省略括号
# # 格式化整数和浮点数，可以指定是否补0，与小数的位数
# # 当不知使用哪种时，可用 %s ，将永远起作用，它会把任何数据类型转换为字符串
# # 当 % 是普通字符时，可使用 %% 即表示为 %
# print('hello %s' % '插值')
# print('hello %s , 数字为 %d' % ('python', 666))
# print('%2d - %02d' % (3, 1))		# 3 - 01
# print('%.2f' % 3.1415926)		# 3.14
# # %2d 将宽度设为2，即在前面补空格
# # %02d 前面补0
# # %-2d 后面补空格

# # f-string 以 f 开头的字符串，将变量直接替换进去
# b = 3.1415926
# print(f'b is {b:.2f}, a is {a:.1f}')

# 数组
# len(array) 获取长度，arr[-1] 取最后一个，append() 向末尾添加，pop()删除末尾，insert 向指定索引添加
# arr1 = [1, 2, 3, 4, 5]
# arr1.insert(2, 666)		# [1, 2, 666, 3, 4 ,5]
# print('arr1 is', arr1)

# dict	字典，类似js的Object
# 取不存在的值会报错，可采用 key in dict 或 dict.get(key [, default]) (不存在时，可传入自定义返回值)
# 删除键使用 dict.pop(key)
# obj = {
# 	'name': 123
# }
# #	123		True 	123		None 	666
# print(obj['name'], 'name' in obj, obj.get('name'), obj.get('age'), obj.get('age', 666), 'dict')

# set		类似于js的 Set
# 可通过 set1 & set2 取两者的交集，通过 set1 | set2 取并集，set不可添加不可变对象，如：list

# 函数使用 def 来定义，如：def ma_func(x): 在此之后以缩进编写函数体，return返回值
# 函数的返回值其实就是一个 tuple ，在语法上一个 tuple 可以省略括号，多个变量接收一个 tuple ，则按顺序赋予对应位置的值
# 可变参数：函数参数个数的可变性，可在定义时，参数前加 * ，如：def func(*augs)，这样可以传任意个参数，内部接收到的是一个 tuple 类型
# 关键字参数：参数前加 ** ，如：def func(name, sex, **augs)，在函数内会组装成 dict 类型
# 如：func('xiaoming', 'man', age=66, city='jiali') => name: 'xiaoming', sex: 'man', augs: {'age': 66, 'city': 'jiali'}
# def func(name, age, **augs):
# 	print(name, age, agus)
# func('xiaoming', 66, sex='man', city='jiali')
# 命名关键字参数： def func(name, age, *, city, sex) ，* 号后的被视为命名关键字参数，只接收该字段的参数
# 如果函数中已经有了一个可变参数，则后面的命名关键字参数就不需要 * 的特殊符号了，如： def func(name, *age, city, sex)
# def product(*augs):
#   result = 1
#   if len(augs) == 0:
#     raise TypeError('is error')
#   for i in augs:
#     result = result * i
#   return result

# print(product(), 'product()')

# 汉诺塔
# def move(n, a, b, c):
#   if n == 1:	# 终止条件
#     print(a, '-->', c)
#   else:
#   	# 第一步： 把n-1个盘子从a移动到b和把第n个盘子从a移动到c
#     move(n - 1, a, c, b) 
#     print(a, '-->', c)

#   	# 第二步： 把n-1个盘子从b移动到c
#     move(n - 1, b, a, c)
# move(2, 'A', 'B', 'C')

# def trim(s):
# 	while s[:1] == ' ':
# 		s = s[1:]
# 	while s[-1:] == ' ':
# 		s = s[:-2]
# 	return s
# print(trim('    aa    bbb    '))

# 循环
# for ... in ... //  for val in xxx.values()  // for key, val in xxx.items()

# 列表生成式
# 一般可以使用 list(range(star, end)) 生成
# 也可使用 for...in... 生成，可在 for 前加数据处理，for 后加条件筛选，如： [x * x for x in range(1, 11) if x % 2 == 0] => [4, 16, 36, 64, 100]
# 也可使用两层循环：[m + n for m in 'ABC' for n in 'XYZ'] => ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
# 当在 for 前加条件判断时：[x if x % 2 == 0 else -x for x in range(1, 11)] => [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# 斐波拉契数列
# 赋值语句：相当于： t = (b, a + b); a = t[0]; b = t[1]
# a, b = 33, 66
# a, b = b, a + b
# print(a, b, 'aabb')		# 66 99
# def fib(max):
# 	n, a, b = 0, 0, 1
# 	while n < max:
# 		print(b)
# 		a, b = b, a + b
# 		n = n + 1
# 	return 'done'
# fib(6)		# 1, 1, 2, 3, 5, 8

# print([1] + [2, 3, 4] + [1])		# [1, 2, 3, 4, 1]

# from functools import reduce
# def str2float(s):
# 	obj = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
# 	def fn1(x):
# 		return obj[x]
# 	def fn2(x, n):
# 		return x / 10 ** n
# 	def fn3(x, y):
# 		return x * 10 + y
# 	return reduce(fn3, map(fn1, s[:s.index('.')])) + fn2(reduce(fn3, map(fn1, s[s.index('.') + 1:])), len(s[s.index('.') + 1:]))
# aa = str2float('123.456')
# print(aa, 'aaaa')

# strip：用于移除字符串头尾自定的字符或字符序列，默认为空格或换行符
# print('123abcrunoob321'.strip('123'))		# abcrunoob

# 字符串反转
# a = '123456'
# print(a[::-1], '12')		# 654321
# s="hy l ekil ylemertxe ma i"
# y=s[:2:-1]
# print(y)		# i am extremely like l

# 排序：sorted(arr, key = xxx, reverse = True)
# 可传入一个映射条件 key = xxx，将对每项根据 key 处理后的值进行排序，第三个参数传入 reverse 是否倒序

# nonlocal 关键字：修饰变量后，该变量是上级函数中的局部变量（非全局中的变量），一般在嵌套函数内使用
# global 关键字：修饰变量后，对该变量修改，就是修改全局变量，无事先定义该全局变量会报错
# def func():
# 	a = 0
# 	def ff():
# 		nonlocal a
# 		a = a + 1
# 		return a
# 	return ff
# aa = func()
# print(aa(), aa(), 'func')		# 1  2

# lambda：表示匿名函数，如：lambda x: x * x，冒号前表示参数，限制：只能有一个表达式，返回值为表达式的结果