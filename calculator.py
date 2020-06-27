# this program is creating abstract class and its usage.
from abc import ABCMeta, abstractmethod

class calculator(metaclass=ABCMeta):
    @abstractmethod
    def addition(self):
        raise NotImplementedError()     #  it is raise this error when we not write a implete/concrete function this abstract function.

    @abstractmethod
    def substraction(self):
        raise NotImplementedError()

    @abstractmethod
    def multiplication(self):
        raise  NotImplementedError()

    @abstractmethod
    def division(self):
        raise NotImplementedError()

# now writting concreate class for the caluculator abstract class

class myCalculator(calculator):
    def __init__(self, v1, v2):
        self.x = v1
        self.y = v2

    def addition(self):
        return self.x + self.y

    def substraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y



class myCustomCalculator(myCalculator):
    def __init__(self, v1, v2, v3):
        self.z = v3
        super().__init__(v1, v2)

    def multiplication(self):
        print("Invoked parent class(myCalculator) multiplication method")
        return super().multiplication()

    def squareRoot(self):
        return self.z * self.z * self.x


def hello():
    print("in side calculator module")


# here I am creating instance for the concreate class. Always pass the arguments to the class.

# answer = myCalculator(3, 4)
# print("Parent Class My Caluculator Addition Answer : ", answer.addition() )
# print("Parent Class My Caluculator Subtraction Answer : ", answer.substraction() )
# print("Parent Class My Caluculator Multiplication Answer : ", answer.multiplication() )
# print("Parent Class My Caluculator Division Answer : ", answer.division() )

# customAnswer = myCustomCalculator(6, 7, 8)
# print("Child Class Multiplication Result : ", customAnswer.multiplication())
# print("Child Class SquareRoot Result : ", customAnswer.squareRoot())








