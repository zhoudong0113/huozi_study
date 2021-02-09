from Animal import Animal


class Cat(Animal):

# 继承父类属性
    def __init__(self,name,colour,age,gender):
        super().__init__(name,colour,age,gender)
        self.Animal_hair = 'short_hair'

    def catch_mouse(self):
        print(f'{self.name}+会捉老鼠')

    def cry(self):
        print(f'{self.name}+会喵喵叫')


if __name__ == '__main__':
    a = Cat(name='喵喵',colour='black',age=6,gender='male','' )
    a.catch_mouse()