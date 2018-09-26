#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any

__arthur__ = "张俊鹏"


class Student(object):  # object 表示Student从object继承而来
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s: %s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('bob', 100)
print(bart)
print(Student)

bart.print_score()

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())


# 访问限制

class Student(object):  # object 表示Student从object继承而来
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s: %s" % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', 59)
# print(bart.__name)  # 此时已经无法访问name属性
print(bart._Student__name)  # 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


# 继承和多态
class Animal(object):
    @staticmethod
    def run():
        print("running")


class Dog(Animal):
    def run(self):
        print("dog run")

    @staticmethod
    def eat():
        print("dog eat")


class Cat(Animal):
    def run(self):
        print("cat run")


dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型

print(isinstance(a, list))
print(isinstance(b, Dog))
print(isinstance(c, Animal))


def real_run(animal):
    animal.run()


d = Dog()
c = Cat()
real_run(d)
real_run(c)


# 还可以添加任意子类继承父类
# 只要确保方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
# 对扩展开放：允许新增子类；
# 对修改封闭：不需要修改依赖父类型的real_run()等函数。


class Timer(object):
    @staticmethod
    def run():
        print("tick tuck")


# 动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
real_run(Timer())

# 获取对象信息
print(type(123))
print(type('str'))
print(type(None))

print(type(abs))
print(type(d))

print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(1, 11))) == types.GeneratorType)

a = Animal()
d = Dog()
c = Cat()

print(isinstance(c, Cat))
print(isinstance(a, Dog))
print(isinstance(d, Animal))

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

print(isinstance([1, 2], (list, tuple)))
print(isinstance((1, 23), (list, tuple)))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir("ABC"))

# 在len()函数内部，它自动去调用该对象的__len__()方法
print(len("ABC"))
print("ABC".__len__())


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))

r = "ABC".lower()
print(r)


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
print(setattr(obj, 'y', 19))
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'z', 404))

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())


def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None


# 实例属性和类属性
class Student(object):
    job = 'study'

    def __init__(self, name):
        self.name = name


# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
s = Student("Bob")
s.score = 99

print("s.job:" + s.job)
print("Student.job:" + Student.job)
s.job = 'coding'
print("s.new job:" + s.job)
print("Student.job:" + Student.job)
del s.job
print("after deleted job:" + s.job)


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        self.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')