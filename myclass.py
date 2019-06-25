#!/usr/bin/python
class MyClass:
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass()

print("MyClass 类的属性  i 为：",x.i)
print("MyClass 类的方法 f 输出为：",x.f())