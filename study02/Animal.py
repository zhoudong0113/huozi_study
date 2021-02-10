"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""

class Animal:

# 定义类里面的属性
    def __init__(self,name,colour,age,gender):
        # 名称,颜色,年龄,性别
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender

# 定义一个类方法(会叫，会跑)
    def action(self,cry,run):
        self.cry = cry
        self.run = run
        print(f'{self.name}'+f'{self.run}')

