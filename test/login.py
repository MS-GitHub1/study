class Person(object):
    def __init__(self):
        self.__age=0
    @property
    def data(self):
        print(self.__age)

    @data.setter
    def data(self,name):
        print('11111')
        self.__age=name
        print(self.__age)




if __name__ == '__main__':
    a=Person().data
    print(a)
    Person().data='小明'



