#!/usr/bin/python

class Compex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Compex(3.0, -4.5)
print(x.r, x.i)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我 %d 岁。"%(self.name,self.age))

p = people('runoob',10,30)
p.speak()

class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g

    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

s = student("ken",10,60,3)
s.speak()

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s ，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
test.speak()

class Parent:
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):
    def myMethod(self):
        print('调用子类方法')

c = Child()
c.myMethod()
super(Child,c).myMethod()

#################################################
class Father(object):
    def __init__(self,name):
        self.name = name
        print("name: %s"%(self.name) )
    def getName(self):
        return 'Father'  + self.name

# class Son(Father):
#     def getName(self):
#         return 'Son '+ self.name

class Son(Father):
    def __init__(self,name):
        super(Son,self).__init__(name)
        print("hi")
        self.name = name
    def getName(self):
        return 'Son ' + self.name
if __name__ == '__main__':
    son = Son('Runoob')
    print(son.getName())

##################################################
class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)

class Site:
    def __init__(self,name,url):
        self.name = name
        self.__url = url

    def who(self):
        print('name : ',self.name)
        print('url: ',self.__url)

    def __foo(self):
        print('这是私有方法')

    def foo(self):
        print('这是公共方法')
        self.__foo()

if __name__ == '__main__':
    x = Site('菜鸟教程','www.runoob.com')
    x.who()
    x.foo()
    # x.__foo()

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d,%d)'% (self.a,self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
if __name__ == '__main__':
    v1 = Vector(2,10)
    v2 = Vector(5,-2)
    print(v1 + v2)