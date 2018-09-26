#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__arthur__ = "张俊鹏"


# 使用__slots__
class Student(object):
    pass


s = Student()
s.name = "Michael"
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)
print(s.age)
# 但是，给实例绑定的方法，对另一个实例是不起作用的
s2 = Student()


# s2.set_age(25) # 尝试调用方法

# 可以给class绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)


class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = "kiven"
s.age = 25


# s.score=100

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GranduatedStudent(Student):
    pass


g = GranduatedStudent()
g.score = 100


# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
class UngraduatedStudent(Student):
    __slots__ = ()
    pass


u = UngraduatedStudent()


# u.score=59


# @property
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


s = Student()
s.score = 89
print(s.score)


# s.score=-1

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self.birth = value

    @property
    def age(self):
        return 2018 - self._birth


# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


# 多重继承
class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print("Running...")


class Flyable(object):
    def fly(self):
        print("Flying...")


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。


# MixIn
# class MyTCPServer(TCPServer, ForkingMixIn):  # 多进程模式的TCP服务
#     pass
#
#
# class MyUDPServer(UDPServer, TreadingMixIn):  # 多线程模式的UDP服务
#     pass


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 改变用户得到的结果
        return "Student object (name:%s)" % self.name

    __pepr__ = __str__  # 改变程序员看到的结果


print(Student("Michael"))


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):  # 用于实现for循环
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):  # 用于实现获取具体的值
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for n in Fib():
    print(n)

f = Fib()
print(f[0])
print(f[1])
print(f[2])

f = Fib()
print(f[0:5])


class Student(object):
    def __init__(self):
        self.name = "Michael"

    def __getattr__(self, item):  # 找不到的变量会从该函数寻找
        if item == "score":
            return 99
        if item == "age":
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)


s = Student()
print(s.name)
print(s.score)
print(s.age)
print(s.age())


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s' % self.name)


s = Student("Michael")
s()

print(callable(Student))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

# 枚举类
from enum import Enum

Month = Enum('Mon', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
from enum import Enum, unique


@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Mon)
print(Weekday['Tue'])
print(Weekday(3))
print(Weekday.Sat.value)


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if type(gender) == Gender:
            self.gender = gender
        else:
            raise ValueError("gender type error")

    def __str__(self):
        return '学生的姓名为：%s,性别为：%s' % (self.name, self.gender)

    __repr__ = __str__


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

# type
from hello import Hello

h = Hello()
h.hello()
print(type(Hello))
print(type(h))


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))


# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass

# metaclass是类的模板，所以必须从`type`类型派生
class ListMetaclass(type):
    # __new__()方法接收到的参数依次是：
    # 当前准备创建的类的对象；
    # 类的名字；
    # 类继承的父类集合；
    # 类的方法集合。
    def __new__(cls, name, bases, methods):
        methods['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, methods)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)


# 自定义ORM Object Relational Mapping
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "%s:%s" % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar(100)")


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")


class ModelMetaclass(type):
    def __new__(cls, name, bases, methods):
        if name == 'Model':  # 这里是为了防止创建model类型
            return type.__new__(cls, name, bases, methods)
        print('Found model: %s' % name)  # 从这里开始是创建了model的子类
        mappings = dict()
        for k, v in methods.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            methods.pop(k)
        methods['__mapping__'] = mappings
        methods['__table__'] = name
        return type.__new__(cls, name, bases, methods)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mapping__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'replace into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print("SQL: %s" % sql)
        print("ARGS: %s" % str(args))


class User(Model):
    # 注意这里都是方法
    id = IntegerField("id")
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，如果没有找到，就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。
#
# 在ModelMetaclass中，一共做了几件事情：
#
# 排除掉对Model类的修改；
#
# 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
#
# 把表名保存到__table__中，这里简化为表名默认为类名。
#
# 在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。
#
# 我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。
