from datetime import datetime
from typing import List, Generic, TypeVar

class Person:
    id = 0

class Student(Person):
    name = ''

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.addr = '无家可归'
    
    def intro(self):
        print(f'my name is {self.id} and my id is {self.name}')

    def encode(self):
        return self.__dict__


class xDateTime():
    def __init__(self, tm = datetime.now()) -> None:
        self.Time = tm
        self.Standard = self.Time.strftime("%Y-%m-%d %H:%M:%S")
        self.Timestamp10 = int(self.Time.timestamp())
        self.Timestamp13 = int(self.Time.timestamp() * 1000)
        pass


T = TypeVar('T')

class xQueue(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop(0)




# T = TypeVar("T")
# def xMax2(num0: T, num1: T) -> T:
#     if type(num0) != type(num1):
#         raise ValueError(f"The two number {num0} and {num1} must have the same type!")

#     return num0 if num0 > num1 else num1

# print(xMax2(6, 4))