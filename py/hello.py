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
# print(r'\\n\t\\')		# \\n\t\\

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

from functools import reduce
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
# 第一个 : 两端表示取值的开始、结束，第二个 : 表示取值是的跨度，正数从左往右，负数从右往左
# 取值范围会受第二个 : 的正负约束，需有正确的同向取值范围
# a = '123456'
# print(a[::-1], '12')		# 654321
# s="hy l ekil ylemertxe ma i"
# y=s[:2:-1]
# 取 -1 ~ 2 间的值，然后从右往左（-1）取值跨度为1（即取相邻的数）
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

# 在python中，变量名类似 __xxx__ （双下划线开头、双下划线结尾）的，是特殊变量，是可以直接访问的，不是私有变量

# 在python中，如果实例的变量名以 __ 开头，则变成了一个私有变量，只有内部可以访问，外部不能访问
# class Student(object):
# 	def __init__(self, name, score):
# 		self.name = name
# 		self.score = score
# 		self.__name = name
# 		self.__score = score

# 	def print_val(self):
# 		print('%s: %s' % (self.__name, self.__score))

# 	def get_name(self):
# 		return self.__name

# 	def set_name(self, name):
# 		self.__name = name
# xm = Student('xiaoming', 66)
# # print(xm, xm.name, xm.__name, 'xm')		# xm实例		xiaoming		报错（不能访问私有变量）
# print(xm.get_name(), 'get_name')
# xm.set_name('kangkang')
# print(xm.get_name(), 'get_name')

# class SS(object):
# 	count = 0
# 	def __init__(self, name):
# 		SS.count += 1
# 		self.name = name

# if SS.count != 0:
# 	print('not 0')		# is 0
# else:
# 	print('is 0')
# a = SS('xiaoming')
# if SS.count != 1:
# 	print('not 1')
# else:
# 	print('is 1')		# is 1
# b = SS('wangcai')
# print(SS.count, 'count')		# 2

# class Screen(object):
# 	@property
# 	def width(self):
# 		return self._width
# 	@width.setter
# 	def width(self, val):
# 		self._width = val
# 	@property
# 	def height(self):
# 		return self._height
# 	@width.setter
# 	def height(self, val):
# 		self._height = val
# 	@property
# 	def resolution(self):
# 		return self._width * self._height
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)

# 通过 callable() 函数，可以判断一个对象是否是 “可调用” 对象
# callable(max) => True 		callable([1, 2, 3]) => False

# 枚举类，value属性自动赋给成员 int 常量，默认从 1 开始计数
from enum import Enum
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
# 	print(name, '=>', member, '=>', member.value)		# 打印对应月份及其值，值为 1-12
# 如果需要更精确的空置枚举类型，可以从 Enum 派生出自定义类，@unique 装饰器可以检查保证没有重复值
from enum import Enum, unique
# @unique
# class Weekday(Enum):
# 	Sun = 0
# 	Mon = 1
# 	Tue = 2
# 	Wed = 3
# 	Thu = 4
# 	Fri = 5
# 	Sat = 6
# # print(Weekday.Tue, '=>', Weekday.Tue.value)
# for name, member in Weekday.__members__.items():
# 	print(name, '=>', member, '=>', member.value)

# 浮点字符串调用 int() 方法时会报错！！ 如：int('6.6') => 报错

from functools import reduce
# def str2num(s):
# 	return int(float(s))
# def calc(exp):
#   ss = exp.split('+')
#   ns = map(str2num, ss)
#   return reduce(lambda acc, x: acc + x, ns)
# def main():
#   r = calc('100 + 200 + 345')
#   print('100 + 200 + 345 =', r)
#   r = calc('99 + 88 + 7.6')
#   print('99 + 88 + 7.6 =', r)
# main()

# 凡是用 print() 来辅助查看的地方，都可以用断言 assert 来替代
# 如： assert n != 0, 'n is zero'
# assert 的意思是，表达式 n != 0 应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
# 在启动Python解释器的时候，可以用 -O 参数来关闭assert，如：python -O hello.py，此时，assert可以当做pass来看

# logging：不会抛出错误，而且可以输出到文件，等级有debug、info、warning、error等
import logging
# logging.basicConfig(level=logging.INFO)

# s = '0'
# n = int(s)
# logging.info('n = %s' % n)
# print(10 / n)

# pdb.set_trace()：用于设置断点，需先引入 pdb
# 调试时，可以键入 p 变量名 获取此时变量的值，键入 c 执行下一步

# isdigit：用于判断字符串是否只有数字组成
# a = '111'
# b = '1.11'
# print(a.isdigit(), b.isdigit(), 'aabb') # True false

# read()：读取文件，可使用 read(size) 每次最多读取size个字节的内容，使用 readline() 可以每次读取每一行内容，使用 readlines() 一次读取所有内容，并按行返回list
# 标识符 r 表示读（文本文件）
# 二进制文件，用 rb 标识符
# 写文件：标识符使用 w（文本文件） 或 wb（二进制文件），使用 a 表示追加写入（默认为删除后写入）
# 要读取非 UTF-8 编码的文本文件，需要传入 encoding 参数，如：open(xxx, 'r', encoding='gbk')
# 还可以传入一个 errors 参数，表示遇到编码错误后如何处理，最简单的方法是直接忽略：open(xxx, 'r', encoding='gbk', errors='ignore')
# title() 方法：首字符大写，其余小写
# with open('./file.txt', 'r') as f:
# 	ls = f.readlines()
# 	for aa in ls:
# 		aa.replace('\n', '')
# 		print(aa, '\n' in aa, aa.title())
# with open('./file.txt', 'a') as f:
# 	f.write('\nhello py')

# 操作文件和目录
import os
# print(os.name)		# nt（window操作系统）
# # print(os.environ)
# print(os.path.abspath('.'))		# 查看当前目录的绝对路径

# JSON序列化
import json
# json.dumps(dict_obj)		# 把dict序列化为json字符串
# json.loads(json_str)		# 把json字符串反序列化
# print(json.dumps(dict_obj, default=lambda obj: obj.__dict__))		# 把实例序列化为json字符串
# 因为通常class的实例都有一个 __dict__属性，它就是一个dict，用来存储实例变量，也有少数例外，比如定义了 __slots__ 的class

# 获取当前进程的ID
import os
# print('Process (%s) start...' % os.getpid())

# 多进程
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
from multiprocessing import Process
import os
# # 子进程要执行的代码
# def run_proc(name):
# 	print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__ == '__main__':
# 	print('Parent process %s' % os.getpid())
# 	p = Process(target=run_proc, args=('test',))
# 	print('Child process will start,')
# 	p.start()
# 	p.join()
# 	print('Child process end')

# 随机数、时间戳（秒）
# random.random() => 生成 0 - 1 范围内的随机浮点数
# random.uniform(a, b) => 生成 a - b 范围内的随机浮点数
# random.randint(a, b) => 生成 a - b 范围内的随机整数
import random, time
# for _ in range(10):
# 	print(random.randint(0, 10), time.time())

# Pool：如果要启动大量子进程，可以用进程池的方式批量创建子进程
# 代码解析：对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
# Pool(4)限制了最多执行4个进程，所以第5个进程会等待前面某个task完成后才执行，Pool的默认大小是CPU的核数
from multiprocessing import Pool
import os, time, random
# def long_time_task(name):
# 	print('Run task %s (%s)...' % (name, os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds' % (name, end - start))
# if __name__ == '__main__':
# 	print('Parent process %s.' % os.getpid())
# 	p = Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_time_task, args=(i,))
# 	print('Waiting for all subprocesses done...')
# 	p.close()
# 	p.join()
# 	print('ALl subprocesses done.')

from multiprocessing import Process, Queue
import os, time, random
# def write(q):
# 	print('Process to write: %s' % os.getpid())
# 	for value in ['A', 'B', 'C']:
# 		print('Put %s to queue...' % value)
# 		q.put(value)
# 		time.sleep(random.random())
# def read(q):
# 	print('Process to read %s' % os.getpid())
# 	while True:
# 		value = q.get(True)
# 		print('Get %s from queue' % value)
# if __name__ == '__main__':
# 	# 父进程创建Queue，并传给各个子进程
# 	q = Queue()
# 	pw = Process(target=write, args=(q,))
# 	pr = Process(target=read, args=(q,))
# 	# 启动子进程，写入与读取
# 	pw.start()
# 	pr.start()
# 	# 等待pw结束
# 	pw.join()
# 	# pr进程里是死循环，无法等待其结束，只能强行终止
# 	pr.terminate()

# 多线程：一般用threading
# current_thread()函数永远返回当前线程的实例，主线程实例的名字叫 MainThread
# 子线程的名字在创建时指定，这里用的是 LoopThread，名字仅仅在打印时用来显示，完全没有其他意义
import time, threading
# def loop():
# 	print('thread %s is running...' % threading.current_thread().name, 111)
# 	n = 0
# 	while n < 5:
# 		n += 1
# 		print('thread %s >>> %s' % (threading.current_thread().name, n))
# 		time.sleep(1)
# 	print('thread %s ended.' % threading.current_thread().name, 222)
# print('thread %s is running...' % threading.current_thread().name, 333)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name, 444)

# 使用锁，防止多线程同时修改一个变量出现问题
import time, threading
# balance = 0
# lock = threading.Lock()
# def change_it(n):
# 	global balance
# 	balance = balance + n
# 	balance = balance - n
# def run_thread(n):
# 	for i in range(2000000):
# 		# 先要获取锁
# 		lock.acquire()
# 		try:
# 			# 修改数据
# 			change_it(n)
# 		finally:
# 			# 改完数据后，释放锁
# 			lock.release()
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('balance =', balance)

# 时间戳为浮点数，整数部分为秒，小数部分为毫秒
from datetime import datetime, timedelta, timezone
# now = datetime.now()
# print('now：', now)
# tp = now.timestamp()
# print('时间戳：', tp)
# time = datetime.fromtimestamp(tp)
# print('时间：', time)
# # 字符串 转 datetime，使用 datetime.strptime()，需对齐字段长短
# cday = datetime.strptime('2011-11-11 11:11:11', '%Y-%m-%d %H:%M:%S')
# print('cday：', cday)
# # datetime 转 字符串，使用 strftime()
# print(now.strftime('%a, %b %d %H:%M'))
# print(now.strftime('%Y-%m-%d %H:%M:%S'))
# # datetime 加减
# print(now + timedelta(hours = 10))
# print(now - timedelta(days = 1))
# print(now + timedelta(days = 1, hours = 10))

import re
# 设置带时区的时间
# def to_timestamp(dt_str, tz_str):
# 	hh = re.match(r'^UTC([+-]\d{1,2})', tz_str).group(1)
# 	time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
# 	tz_utc_ct = timezone(timedelta(hours=int(hh)))
# 	time = time.replace(tzinfo=tz_utc_ct)
# 	return time.timestamp()
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# print(t1, t2, 'tttt')

# namedtuple
# namedtuple 是一个函数，它用来创建一个自定义的 tuple，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p, p.x, p.y, 'pppp')

# deque
# deque 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低，deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q, 'qqqq')
# q.pop()
# q.popleft()
# print(q, 'q2q2q2')

# defaultdict
# defaultdict，使用dict时，如果引用的key不存在，就会抛出KeyError，如果希望key不存在时，返回一个默认值，就可用defaultdict
# 注意默认值是调用函数返回的，二函数在创建defaultdict对象时传入
from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

# OrderedDict
# OrderedDict，使用dict时，key是无序的，在对dict做迭代时，我们无法确定key的顺序，如果要保持key的顺序，就可用OrderedDict
from collections import OrderedDict
# d = dict([('a', 1), ('c', 3), ('b', 2)])
# # d的key是无序的
# print(d, 'd')
# # dd的key是有序的
# dd = OrderedDict([('x', 11), ('y', 22), ('z', 33)])
# print(dd, 'dd')
# dd['x'] = 'xxx'
# print(dd, 'dd2')
# OrderedDict的key会按照插入的顺序排列，不是key本身排序
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的key

# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

# itertools：提供了非常有用的用于操作迭代对象的函数，返回值是Iterator
import itertools
# 无限的重复下去,根本停不下来：
# 传入 count() 的第一个参数为起始值，第二个参数为步伐
# counts = itertools.count(1, 2)
# for n in counts:
# 	print(n)		# => 1, 3, 5, 7, ...
# cycles = itertools.cycle('ABC')
# for n in cycles:
# 	print(n)
# repeat 可通过传第二个参数，限定重复次数
# repeats = itertools.repeat('AB', 3)
# for n in repeats:
# 	print(n)
# 可通过 takewhile() 等函数根据条件判断来截取出一个有限的序列
# counts = itertools.count(1)
# ll = itertools.takewhile(lambda x: x <= 10, counts)
# print(list(ll), 'll')
# chain()
# 可以把一组迭代对象串联起来，形成一个更大的迭代器
# for n in itertools.chain('ABC', 'XYZ'):
# 	print(n)		# => A B C X Y Z
# groupby()
# 把迭代器中相邻的重复元素挑出来放在一起
# for k, g in itertools.groupby('AAABBCCAAA'):
# 	print(k, list(g))
# ['A', 'A', 'A'] ['B', 'B'] ['C', 'C'] ['A', 'A', 'A']

# def pi(N):
# 	# step 1: 创建一个奇数序列：1, 3, 5, 7, 9, ...
# 	counts = itertools.count(1, 2)
# 	# step 2: 取该序列的前N项
# 	ll = list(itertools.takewhile(lambda x: x <= 2 * N - 1, counts))
# 	# step 3: 隔项添加正负号，并用4除
# 	ll = [-4 / ll[i] if i % 2 else 4 / ll[i] for i in range(0, N)]
# 	# step 4: 求和
# 	return sum(ll)
# print(pi(10))
# print(pi(100))

from PIL import Image
