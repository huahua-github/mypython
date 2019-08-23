#新建一个动物类
class Animal(object):
    def eat(self):
        print("动物在吃东西")
class Dog(Animal):
    __name="小黄"
    def eat(self):
        print("狗在吃东西")
    def __wang(self):
        print("狗再叫")
    def jiao(self):
        self.__wang()
    def get_name(self):
        return self.__name
class Xiaotian(Dog):
    def eat(self,temp):
        temp.eat()

xiaotian=Xiaotian()
print(xiaotian.get_name())
xiaotian.jiao()
xiaotian.eat(Dog())
xiaotian.eat(Animal())