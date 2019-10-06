#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/10/4 0004 16:07 
# @Autohor: Sam
# @File   : Chapter14.py


# 热身例子
# class Foo:
#     pass
# foo = Foo()
# print(isinstance(foo, Foo))
# 结论：判断foo对象是不是这个Foo类


# 反射内置函数 hasattr, getattr, setattr, delattr
# hasattr
# class People:
#     country = "China"
#     def __init__(self, name):
#         self.name = name
#     def tell(self):
#         print('%s is aaa'%self.name)
# obj = People('albert')
# print(hasattr(People, 'country'))
# print(hasattr(obj, 'name'))
# print(hasattr(obj, 'country'))
# print(hasattr(obj, 'tell'))


# getattr
# class People:
#     country = "China"
#     def __init__(self, name):
#         self.name = name
#     def tell(self):
#         print('%s is aaa'%self.name)
# obj = People('albert')
# x = getattr(People, 'country', None)
# print(x)
# 结论：如果没有country1这个属性，就传入None


# getattr 2
# class People:
#     country = "China"
#     def __init__(self, name):
#         self.name = name
#     def tell(self):
#         print('%s is aaa'%self.name)
# obj = People('albert')
# f = getattr(People, 'tell', None)
# print(f == obj.tell)
# f()
# obj.tell()


# setattr,添加一个属性
# class People:
#     country = "China"
#     def __init__(self, name):
#         self.name = name
#     def tell(self):
#         print('%s is aaa'%self.name)
# obj = People('albert')
# setattr(People, 'x', 111)
# print(People.x)
# setattr(obj,'age', 18)
# print(obj.__dict__)


# delattr:删除一个属性
# class People:
#     country = "China"
#     def __init__(self, name):
#         self.name = name
#     def tell(self):
#         print('%s is aaa'%self.name)
# obj = People('albert')
# print(People.__dict__)
# delattr(People, 'country')
# print(People.__dict__)
#
# print(obj.__dict__)
# delattr(obj, 'name')
# print(obj.__dict__)


# 实战例子：
# class Foo:
#     def run(self):
#         while True:
#             cmd = input('cmd>>:').strip()
#             if hasattr(self, cmd):
#                 func = getattr(self, cmd)
#                 func()
#             elif cmd == 'exit':
#                 break
#     def download(self):
#         print('download...')
#     def upload(self):
#         print('upload')
#
# obj = Foo()
# obj.run()
# 结论，可以使用字符来调用函数


# 面向对象的内置方法
# class Foo:
#     pass
# obj = Foo()
# l = [1,2,3,4]
# print(obj.__str__())
# print(l)
# 结论：l打印是值，而obj打印的是内存地址,要使用__str__


# __str__例子
# class People:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def __str__(self):
#         return '<名字：%s 年龄：%s 性别：%s>'%(self.name, self.age, self.sex)
#
# obj = People('ablert', 18, 'male')
# print(obj)
# 结论：__str__打印时自动触发


# __del__方法
# import time
# class People:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def __del__(self):
#         print('__del__')
# obj = People('albert', 18, 'male')
# # del obj
# time.sleep(5)
# 结论：代码运行结束后，自动删除对象obj


# 回收系统资源
# class MyOpen:
#     def __init__(self, file_path, mode='r', encoding='utf-8'):
#         self.file_path = file_path
#         self.mode = mode
#         self.encoding = encoding
#         self.file_obj = open(file_path, mode=mode, encoding=encoding)
#     def __str__(self):
#         msg = """
#         file_path:%s
#         mode:%s
#         encoding:%s
#         """%(self.file_path, self.mode, self.encoding)
#         return msg
#     def __del__(self):
#         self.file_obj.close()
#
# f = MyOpen('setting.py', mode='r', encoding='utf-8')
# print(f.file_path, f.mode, f.encoding)
# print(f)
# print(f.file_obj)
# res = f.file_obj.read()
# print(res)
# 结论：__del__是回收系统资源的，Python自己会回收自己的应用程序的资源


# __call__
# class Foo:
#     def __init__(self):
#         pass
#     def __str__(self):
#         return '123123'
#     def __del__(self):
#         pass
#     def __call__(self, *args, **kwargs):
#         print('__call__', args, kwargs)
# obj = Foo()
# print(obj)
# obj(1,2,3,a=1,b=2,c=3)
# 结论，调用对象时会自动执行__call__的方法


# 热身例子1
# exec用法
# code = """
# x = 1
# y = 2
# """
# global_dic = {}
# local_dic = {}
# exec(code, global_dic, local_dic)
# print(global_dic)
# print(local_dic)
# 结论:这里默认是局部的变量，所以打印local_dic能够看信息


# 热身例子2
# code = """
# global x
# x = 111
# y = 2
# """
# global_dic = {'x':999}
# local_dic = {}
# exec(code, global_dic, local_dic)
# print(global_dic)
# print(local_dic)
# 结论：定义为全局变量后会在global_dic上面显示它的值


# 热身例子3
# code = """
# x = 1
# y = 1
# def f1(self, a, b):
#     pass
# """
# local_dic = {}
# exec(code, {}, local_dic)
# print(local_dic)
# 结论：code里面全部放在local_dic里面


# 元类
# class Chinese:
#     country = "China"
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def speak(self):
#         print('%s speak Chinese'%self.name)
# p = Chinese('albert', 18, 'male')
# print(p)
# print(type(p))
# print(type(Chinese))
# #``````````````````````````````````````````````````
# def abc():
#     pass
# print(type(abc))
# 结论：类的类是type，也就是类的宿主，你在使用class关键字时就开始调了type的实例化了
# 类的类叫作元类


# 使用元类建立一个类
# class_name = 'Chinese'
# class_bases = (object, )
# class_body = """
# country = "China"
# def __init__(self, name, age, gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
# def speak(self):
#     print('%s speak Chinese'%self.name)
# """
# class_dic = {}
# exec(class_body, {}, class_dic)
# # print(class_dic)
#
# Chinese = type(class_name, class_bases, class_dic)
# albert = Chinese('albert', 18, 'male')
# print(albert)

# obj = type(class_name, class_bases, class_dic)
# print(obj)
# 这是定义类的另一种写法，使用的是元类，类的宿主，当然实际不能这么写


# 默认与以下的写法一致
# class Foo(metaclass=type):
#     pass
# 结论：类的默认写法与这个一样，type是关键字class的宿主


# 自定义类1
# class MyType(type):
#     def __init__(self):
#         pass
#
# class Foo(metaclass=MyType):
#     pass
# 改进：
# class MyType(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         if not class_name.istitle():
#             raise TypeError("类名的首字母必须大写")
#         super(MyType, self).__init__(class_name, class_bases, class_dic)
#
# class Foo(object, metaclass=MyType):
#     pass
# 结论，我们可以控制类名不用大写的小伙伴


# __doc__：显示注释的方法
# class Student:
#     """
#     学生类
#     """
#     pass
#
# print(Student.__doc__)
# print(Student.__dict__)
# 结论，如果不写注释就会返回None


# 继续控制类
# class MyType(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         if not class_name.istitle():
#             raise TypeError('类名的首字母大写')
#         if not class_dic.get('__doc__'):
#             raise TypeError('居然不写注释，找打啊')
#         super(MyType, self).__init__(class_name, class_bases, class_dic)
#
# class Foo(object, metaclass=MyType):
#     pass
# 结论：我们再一次自定义了类


# 自定义类的调用
# class MyType(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         super(MyType, self).__init__(class_name, class_bases, class_dic)
#
#     def __call__(self, *args, **kwargs):
#         print('============>')
#
# class Foo(object, metaclass=MyType):
#     pass
#
# obj = Foo()
# print(obj)
# 结论，返回值中有一个None，那是因为使用了call函数，没有返回值


# __call__：调用类时执行call函数
# class MyType(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         super(MyType, self).__init__(class_name, class_bases, class_dic)
#
#     def __call__(self, *args, **kwargs):
#         print('============>')
#         print(*args)
#         print(**kwargs)
#
# class Foo(object, metaclass=MyType):
#     def __init__(self):
#         self.Y = y
#
#     def f1(self):
#         print('from f1')
#
# Foo(123)
# 结论：这下返回值没有出现空了


# 继续改进自定义类1
# class MyType(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         super(MyType, self).__init__(class_name, class_bases, class_dic)
#     def __call__(self, *args, **kwargs):
#         obj = object.__new__(self)
#         self.__init__(obj, *args, **kwargs)
#         return obj
# class Foo(object, metaclass=MyType):
#     def __init__(self, y):
#         self.y = y
# Foo(123)
# 继续改进2
# class MyType(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         super(MyType, self).__init__(class_name, class_bases, class_dic)
#     def __call__(self, *args, **kwargs):
#         obj = object.__new__(self)
#         self.__init__(obj, *args, **kwargs)
#         return obj
# class Foo(object, metaclass=MyType):
#     def __init__(self, y):
#         self.y = y
#     def f1(self):
#         print('from f1')
# obj = Foo(123)
# print(obj)
# print(obj.y)
# print(obj.f1)
# 结论，我们可以返回一个空对象，并且像我们以前一样操作都可以


# 单例模式
# class MySQL:
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#
# obj1 = MySQL('1.1.1.2', 3306)
# obj2 = MySQL('1.1.1.3', 3307)
# obj3 = MySQL('1.1.1.4', 3308)
# print(obj1)
# print(obj2)
# print(obj3)
# 结论，这是手输入的值，但实际工作我们都是文件配置的


# 实际：单例模式
# import setting
# class MySQL:
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#     @classmethod
#     def read_from_conf(cls):
#         obj = cls(setting.IP, setting.PORT)
#         return obj
#
# obj4 = MySQL.read_from_conf()
# obj5 = MySQL.read_from_conf()
# obj6 = MySQL.read_from_conf()
# print(obj4)
# print(obj5)
# print(obj5)
# 结论：这里三个对象的内存地址不同，取的时候都一样，所以浪费


# 改进单例
# import setting
# class MySQL:
#     __instance = None
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#     @classmethod
#     def create_singleton(cls):
#         if not cls.__instance:
#             obj = cls(setting.IP, setting.PORT)
#             cls.__instance = obj
#         return cls.__instance
#
# obj1 = MySQL.create_singleton()
# obj2 = MySQL.create_singleton()
# obj3 = MySQL.create_singleton()
# print(obj1)
# print(obj2)
# print(obj3)
# 结论：经过调整现在对象的内存地址都一样