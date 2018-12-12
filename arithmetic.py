class Arithmetic:
    '''static methds never talks about reference variables and static variables'''
    @staticmethod
    def add(x, y):
        print("after adding: ", x+y)
    @staticmethod
    def product(x, y):
        print("after multiplication: ",x*y)
    @staticmethod
    def average(x,y):
        print("average is: ",(x+y)/2)

#recommended to call static method using class name
Arithmetic.add(10,20)
Arithmetic.product(10,20)
Arithmetic.average(10,20)

#static method can be call using reference variable
a = Arithmetic()
a.add(100,200)
a.product(100,200)
a.average(100,200)