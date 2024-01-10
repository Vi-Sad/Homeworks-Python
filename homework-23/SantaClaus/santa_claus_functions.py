from santa_claus_turtle import *


class SantaClaus:
    def __init__(self, name: str, age: int, count_gifts: int):
        self.name = name
        self.age = age
        self.count_gifts = count_gifts

    def give_gifts(self):
        return main(self.name, self.count_gifts)

    def update_age(self, new_age):
        self.age = new_age
        return self.age
