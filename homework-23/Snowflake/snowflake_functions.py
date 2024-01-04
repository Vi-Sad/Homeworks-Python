from snowflake_turtle import *


class Snowflake:
    def __init__(self, size: int, shape: int):
        self.size = size
        self.shape = shape

    def info_snowflake(self):
        return f'* * *\nРазмер снежинки --> {self.size}\nКоличество сегментов снежинки --> {self.shape}'

    def look_snowflake(self):
        print('* * *\nЗагрузка снежинки...')
        snowflake(self.size, self.shape)
        return 'Снежинка готова'

    def change_size(self, new_size):
        self.size = new_size
        return self.size

    def change_shape(self, new_shape):
        self.shape = new_shape
        return self.shape
