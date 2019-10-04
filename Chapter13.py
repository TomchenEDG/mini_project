#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/10/2 0002 17:38 
# @Autohor: Sam
# @File   : Chapter13.py

# 继承的实现
# class DeepsharePeople:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# class DeepshareTeacher(DeepsharePeople):
#     def modify_score(self):
#         print('teacher %s is modifying score'%self.name)
#
# class DeepshareStudent(DeepsharePeople):
#     def choose(self):
#         print('student %s is choosing course'%self.name)
#
# tea1 = DeepshareTeacher('albert', 18, 'male')
# stu1 = DeepshareStudent('张二狗', 18, 'female')
#
# print(tea1.name)
# print(stu1.name)



# 继承的实现2
# class DeepsharePeople:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# class DeepshareTeacher(DeepsharePeople):
#     def modify_score(self):
#         print('teacher %s is modifying score'%self.name)
#
# tea1 = DeepshareTeacher('albert', 18, 'male')
# print(tea1.__dict__)
# print(tea1.name)
# print(DeepsharePeople.__dict__)
# print(DeepshareTeacher.__dict__)
# print(tea1.school)
# print(tea1.modify_score)



# 技巧题
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#     def f2(self):
#         print('Foo.f2')
#         self.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj = Bar()
# obj.f2()
#
# print(obj.__dict__)
# 结论：self.f1是obj对象的，所以打印Bar下面的属性


# 派生，在原来继承基础上增加新的属性
# class DeepsharePeople:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def f1(self):
#         print('爹的f1')
# class DeepshareTeacher(DeepsharePeople):
#     def modify_score(self):
#         print('teacher %s is modifying score'%self.name)
#     def f1(self):
#         print('儿子的f1')
# tea1 = DeepshareTeacher('albert', 18, 'male')
# tea1.f1()
# 父类和子类有相同的属性，则子类先调用自己的属性


# 派生第二个例子
# class DeepsharePeople:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def f1(self):
#         print('爹的f1')
# class DeepshareTeacher(DeepsharePeople):
#     def __init__(self, name, age, gender, level, salary):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.level = level
#         self.salary = salary
#     def modify_score(self):
#         print('teacher %s is modifying score'%self.name)
#     def f1(self):
#         print('儿子的f1')
#
# tea1 = DeepshareTeacher('albert', 18, 'male', '10', '3.1')
# print(tea1.name, tea1.age, tea1.gender, tea1.level, tea1.salary)
# 实验结果：父类和子类都有初始函数，这时先调用子类里的属性


# 派生中解决以上冗余代码
# class DeepsharePeople:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def f1(self):
#         print('爹的f1')
# class DeepshareTeacher(DeepsharePeople):
#     def __init__(self, name, age, gender, level, salary):
#         DeepsharePeople.__init__(self, name, age, gender)
#         self.level = level
#         self.salary = salary
#     def modify_score(self):
#         print('teacher %s is modifying score'%self.name)
#     def f1(self):
#         print('儿子的f1')
#
# tea1 = DeepshareTeacher('albert', 18, 'male', '10', '3.1')
# print(tea1.name, tea1.age, tea1.gender, tea1.level, tea1.salary)
# 实验：出现冗余代码，需要使用以上方式来解决


# 派生例子的改进
# class DeepsharePeople:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def info(self):
#         print("""
#         ===个人信息===
#         姓名：%s
#         年龄：%s
#         性别：%s
#         """%(self.name, self.age, self.gender))
# class DeepshareTeacher(DeepsharePeople):
#     def __init__(self, name, age, gender, level, salary):
#         DeepsharePeople.__init__(self, name, age, gender)
#         self.level = level
#         self.salary = salary
#     def modify_score(self):
#         print('teacher %s is modifying score'%self.name)
#     def f1(self):
#         print('儿子的f1')
#
# tea1 = DeepshareTeacher('albert', 18, 'male', '10', '3.1')
# tea1.info()
# 实验：调用子类中没有的属性，会自动在继承的父类查找


# 派生例子的改进
# class DeepsharePeople:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def info(self):
#         print("""
#         ===个人信息===
#         姓名：%s
#         年龄：%s
#         性别：%s
#         """%(self.name, self.age, self.gender))
# class DeepshareTeacher(DeepsharePeople):
#     def __init__(self, name, age, gender, level, salary):
#         DeepsharePeople.__init__(self, name, age, gender)
#         self.level = level
#         self.salary = salary
#     def modify_score(self):
#         print('teacher %s is modifying score'%self.name)
#     def info(self):
#         print("""
#         ===个人信息===
#         姓名：%s
#         年龄：%s
#         性别：%s
#         """%(self.name, self.age, self.gender))
#         print("""
#         等级：%s
#         薪资:%s
#         """%(self.level, self.salary))
#
# tea1 = DeepshareTeacher('albert', 18, 'male', '10', '3.1')
# tea1.info()
# 结论：调用子类已有的属性会直接调用自己


# 派生例子：改进冗余代码
# class DeepsharePeople:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def info(self):
#         print("""
#         ===个人信息===
#         姓名：%s
#         年龄：%s
#         性别：%s
#         """%(self.name, self.age, self.gender))
# class DeepshareTeacher(DeepsharePeople):
#     def __init__(self, name, age, gender, level, salary):
#         DeepsharePeople.__init__(self, name, age, gender)
#         self.level = level
#         self.salary = salary
#     def modify_score(self):
#         print('teacher %s is modifying score'%self.name)
#         DeepsharePeople.info(self)
#         print("""
#         等级：%s
#         薪资:%s
#         """%(self.level, self.salary))
#
# tea1 = DeepshareTeacher('albert', 18, 'male', '10', '3.1')
# tea1.info()
# 结论：类中出现冗余代码，要积极改进，避免冗余


# 派生第二种方案（用super（）调用）
# class DeepsharePeople:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def info(self):
#         print("""
#         ===个人信息===
#         姓名：%s
#         年龄：%s
#         性别：%s
#         """%(self.name, self.age, self.gender))
# class DeepshareTeacher(DeepsharePeople):
#     def __init__(self, name, age, gender, level, salary):
#         super().__init__(name, age, gender)
#         self.level = level
#         self.salary = salary
#     def modify_score(self):
#         print('teacher %s is modifying score'%self.name)
#     def info(self):
#         super().info()
#         print("""
#         等级：%s
#         薪资:%s
#         """%(self.level, self.salary))
#
# tea1 = DeepshareTeacher('albert', 18, 'male', '10', '3.1')
# tea1.info()
# 结论，使用super()返回父类，无需加self


# 什么是object
# print(object)
# 所有类的老祖宗


# 类
# class Foo:
#     pass
# print(Foo.__bases__)
# 结论，类没有指定的父类，默认继承object类


# 多继承的查找方式
# class A(object):
#     def test(self):
#         print('from A')
# class B(A):
#     def test(self):
#         print('from B')
# class C(A):
#     def  test(self):
#         print('from C')
# class D(B):
#     def test(self):
#         print('from D')
# class E(C):
#     def test(self):
#         print('from E')
# class F(D, E):
#     # def test(self):
#     #     print('from F')
#     pass
#
# f1 = F()
# f1.test()
# 结论：新式类为广度优先搜索，旧式类为深度优先搜索
# print(F.__mro__)
# print(F.mro())
# 结论，这是新式类提供的查找属性的方法


# super()继承查找
# class X:
#     def test(self):
#         print('x')
#     def f1(self):
#         print('XF')
# class A(X):
#     def test(self):
#         print('1 打印一下，代码先经过这里')
#         super().f1()
#         print('3 再打印一下，代码最后经过这里')
# class B:
#     def f1(self):
#         print('2 再经过这里from B')
# class C(A, B):
#     pass
#
# c = C()
# c.test()
# print(C.mro())
# 结论：A会把B类认为爹


# 加入super()的查找顺序
# class X:
#     def test(self):
#         print('x')
#     # def f1(self):
#     #     print('XF')
# class A(X):
#     def test(self):
#         print('1 打印一下，代码先经过这里')
#         super().f1()
#         print('3 再打印一下，代码最后经过这里')
# class B:
#     def f1(self):
#         print('2 再经过这里from B')
# class C(A, B):
#     pass
#
# c = C()
# c.test()
# print(C.mro())
# 结论，mro会按照C3算法来查找属性，但遇到super()的情况，也会出现改变


# 组合
# class Date:
#     def __init__(self, year, mon, day):
#         self.year = year
#         self.mon = mon
#         self.day = day
#     def tell_birth(self):
#         print('出生年月<%s-%s-%s>'%(self.year, self.mon, self.day))
# class DeepsharePeople:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# class DeepshareTeacher(DeepsharePeople):
#     def __init__(self, name, age, gender, level, salary):
#         super().__init__(name, age, gender)
#         self.level = level
#         self.salary = salary
#     def change_score(self):
#         print('teacher %s is changing score'%self.name)
# class DeepshareStudent(DeepsharePeople):
#     def __init__(self, name, age, gender, course):
#         super().__init__(name, age, gender)
#         self.course = course
#     def choose(self):
#         print('student %s choose course'%self.name)
#
# tea1 = DeepshareTeacher('albert', 18, 'male', 10, 3.1)
# date_obj = Date(2000,1,1)
# date_obj.tell_birth()

# 赋予给老师类新的属性birth
# tea1.birth = date_obj
# print(tea1.birth)
# tea1.birth.tell_birth()
# tea1.change_score()

# stu1 = DeepshareStudent('张三', 16, 'male', 'AI')
# stu1.birth = Date(2002, 3, 3)
# stu1.birth.tell_birth()


# 封装的例子
# class Foo:
#     x = 111
#     def f1(self):
#         print('Foo.f1')
# obj = Foo()
# print(obj.x)
# 把以上x隐藏起来
# class Foo:
#     __x = 111
#     def f1(self):
#         print('Foo.f1')
# obj = Foo()
# print(obj.x)
# print(obj._x)
# print(obj.__x)
# 结论：访问不了x


# 封装例子2
# class Foo:
#     __x = 111
#     def __init__(self, y):
#         self.__y = y
#     def __f1(self):
#         print('Foo.f1')
#
# obj = Foo(222)

# print(obj.x)
# print(obj.__x)
#
# print(obj.f1)
# print(obj.__f1)
#
# print(obj.y)
# print(obj.__y)
# 结论：找不到相关属性
# print(obj._Foo__x)
# print(obj._Foo__f1)
# print(obj._Foo__y)
# 结论：修改调用方式，即可访问


# 封装例子3
# class Foo:
#     __x = 111
#     def __init__(self, y):
#         self.__y = y
#     def __f1(self):
#         print('Foo.f1')
#     def get__y(self):
#         print(self.__y)
#
# obj = Foo(222)
# obj.get__y()
# 结论：可以访问到y，因为是内部访问
# obj.__aa = 1
# obj.__bb = 2
# print(Foo.__dict__)
# print(obj.__dict__)
# 结论：obj.__aa这样的写法不会再有变形的效果


# 封装
# class Foo:
#     def __f1(self):
#         print('Foo.f1')
#     def f2(self):
#         print('Foo.f2')
#         self.__f1()
# class Bar(Foo):
#     def __f1(self):
#         print('Bar.f1')
# obj = Bar()
# obj.f2()
# 结论：因为__f1函数在两个类中发生了不同的形变


# 封装
# class People:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def tell_info(self):
#         print(self.__name, self.__age)
#
# p = People('albert', 18)
# p.tell_info()
# 结论：封装一个按钮给大家用


# 封装2
# class People:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def tell_info(self):
#         u = input('user>>:').strip()
#         p = input('pwd>>:').strip()
#         if u == 'albert' and p == 'abc':
#             print(self.__name, self.__age)
#
# p = People('albert', 18)
# p.tell_info()
# 结论：可以封装起来，隔离复杂度


# 封装3
# class ATM:
#     def put_your_card(self):
#         print('1 插卡')
#     def input_password(self):
#         print('2 输密码')
#     def input_money(self):
#         print('3 输入取款金额')
#     def __sent_request(self):
#         print('向银行系统发出请求（不让你看到的代码）')
#     def __dedcut_money(self):
#         print('扣钱（不让你看）')
#     def __update_user_balance(self):
#         print('更新用户余额（不让你看）')
#     def withdraw(self):
#         self.__sent_request()
#         self.__dedcut_money()
#         self.__update_user_balance()
#
# obj = ATM()
# obj.put_your_card()
# obj.input_password()
# obj.input_money()
# obj.withdraw()


# 没有Property方法
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     def bmi(self):
#         return self.weight / (self.height * self.height)
# albert = People('albert', 75, 1.80)
# print(albert.bmi())
# 结论：可以直接调用对象点属性方法计算bmi,但这并不规范


# 有Propert方法
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#     @property
#     def bmi(self):
#         return self.weight / (self.height * self.height)
# albert = People('albert', 75, 1.80)
# print(albert.bmi)
# albert.weight = 70
# print(albert.bmi)
# 结论：使用property可以对象点属性来计算bmi,可以随意变化


# 伪装属性的修改与删除
# class People:
#     def __init__(self, name):
#         self.__name = name
#     @property
#     def name(self):
#         print('访问'.center(50, '='))
#         return self.__name
#
# p = People('albert')
# print(p.name)
# del p.name
# print(p.name)
# 结论：不能修改，也不能删除


# 伪装属性的修改和删除
# class People:
#     def __init__(self, name):
#         self.__name = name
#     @property
#     def name(self):
#         print('访问'.center(50, '='))
#         return self.__name
#     @name.setter
#     def name(self, x):
#         print('修改'.center(50, '='))
#         self.__name = x
#     @name.deleter
#     def name(self):
#         print('删除'.center(50, '='))
#         del self.__name
#
# p = People('albert')
# print(p.name)
# p.name = 'ALBERT'
# print(p.name)
# del p.name
# print(p.name)


# 多态1
# class Animal:
#     def eat(self):
#         print('eat')
#         pass
#     def drink(self):
#         pass
#     def run(self):
#         pass
#     def bark(self):
#         pass
#
# class Cat(Animal):
#     pass
# class Dog(Animal):
#     pass
# class Pig(Animal):
#     pass
# c = Cat()
# d = Dog()
# p = Pig()
# c.eat()
# d.eat()
# p.eat()


# 多态2
class Animal:
    def eat(self):
        print('eat')
        pass
    def drink(self):
        pass
    def run(self):
        pass
    def bark(self):
        pass

class Cat(Animal):
    def bark(self):
        print('喵喵叫')
    pass

class Dog(Animal):
    def bark(self):
        print('汪汪叫')
    pass
class Pig(Animal):
    def bark(self):
        print('哼哼叫')
    pass
c = Cat()
d = Dog()
p = Pig()
c.bark()
d.bark()
p.bark()
# 结论，每个对象都自己的特别，那就在自己类修改。
