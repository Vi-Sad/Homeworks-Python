import random

print('-' * 100)

print('Task #1')
# Создайте базовый класс "Сотрудник" с общими характеристиками (например, имя, зарплата).
# Затем создайте подклассы для различных типов сотрудников, таких как "Менеджер" и "Разработчик".
# Добавьте уникальные свойства и методы для каждого типа.
# Реализуйте методы для подсчета общей зарплаты и вычисления премии.

list_employees = [
    {
        'name': 'Ben',
        'salary': 40000,
        'post': 'Manager'
    },
    {
        'name': 'Max',
        'salary': 55000,
        'post': 'Manager'
    },
    {
        'name': 'John',
        'salary': 140000,
        'post': 'Developer'
    },
    {
        'name': 'Jessie',
        'salary': 90000,
        'post': 'Developer'
    }
]


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_main(self):
        return f'Name --> {self.name}\nSalary --> {self.salary} RUB'

    def prize_main(self, percent):
        print(f'The bonus is given in the amount of {int(percent * 100)}% of the salary --> ', end='')
        bonus = self.salary * percent
        return f'{int(bonus)} RUB'

    @staticmethod
    def total_salary(list_salary):
        summ = 0
        for salary in list_salary:
            summ += salary['salary']
        return f'Total salary of employees --> {summ} RUB'


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def display(self):
        print(f'\nEmployee with the position of "Manager":')
        return super().display_main()

    def prize(self):
        percent = 0.1
        return super().prize_main(percent)

    @staticmethod
    def feature(list_managers):
        summ = 0
        print('Each manager receives a bonus of 1% of the total amount of all managers --> ', end='')
        for manager in list_managers:
            if manager['post'] == 'Manager':
                summ += manager['salary']
        return f'{int(summ * 0.1)} RUB'


class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def display(self):
        print(f'\nEmployee with the position of "Developer":')
        return super().display_main()

    def prize(self):
        percent = 0.2
        return super().prize_main(percent)

    @staticmethod
    def feature(list_developers):
        summ = 0
        count = 0
        print('Each developer receives a bonus of 3% of the average salary of all developers --> ', end='')
        for developer in list_developers:
            if developer['post'] == 'Developer':
                summ += developer['salary']
                count += 1
        return f'{int(summ / count * 0.3)} RUB'


for emp in list_employees:
    if emp['post'] == 'Manager':
        employee = Manager(emp['name'], emp['salary'])
        print(employee.display())
        print(employee.prize())
    else:
        employee = Developer(emp['name'], emp['salary'])
        print(employee.display())
        print(employee.prize())

print('\n* * *\n')
print(Manager.feature(list_employees))
print(Developer.feature(list_employees))
print(Employee.total_salary(list_employees))

print('-' * 100)

# ---------------------------------------------------------------------------------------------------------------------

print('Task #2')
# Создайте базовый класс "Школьный предмет" с общими характеристиками (например, название, уровень сложности).
# Затем создайте подклассы для различных предметов, таких как "Математика" и "Литература".
# Добавьте уникальные свойства и методы для каждого предмета.
# Реализуйте методы для вычисления средней оценки по предмету.

evaluations_mathematics = []
evaluations_literature = []
evaluations_all = []
estimation_random = range(2, 6)


class SchoolSubject:
    def __init__(self, title, estimation):
        self.title = title
        self.estimation = estimation
        subject = {'subject': self.title, 'estimation': self.estimation}
        evaluations_all.append(subject)

    @staticmethod
    def average_rating():
        average_rating_mathematics = round(sum(evaluations_mathematics) / len(evaluations_mathematics), 2)
        average_rating_literature = round(sum(evaluations_literature) / len(evaluations_literature), 2)
        return f'Average grade in mathematics --> ~{average_rating_mathematics}\n' \
               f'Average grade in literature --> ~{average_rating_literature}'


class Mathematics(SchoolSubject):
    @staticmethod
    def evaluations_mathematics():
        for i in evaluations_all:
            if i['subject'] == 'Mathematics':
                evaluations_mathematics.append(i['estimation'])
        return evaluations_mathematics

    @staticmethod
    def grade():
        average_rating_mathematics = round(sum(evaluations_mathematics) / len(evaluations_mathematics), 2)
        if average_rating_mathematics > 4:
            return 'Good academic performance in mathematics'
        else:
            return 'Poor academic performance in mathematics'


class Literature(SchoolSubject):
    @staticmethod
    def evaluations_literature():
        for i in evaluations_all:
            if i['subject'] == 'Literature':
                evaluations_literature.append(i['estimation'])
        return evaluations_literature

    @staticmethod
    def reading_speed():
        reading_speed = []
        n = 0
        reading = range(100, 401)
        while True:
            if n == len(evaluations_literature):
                break
            else:
                n += 1
                reading_speed.append(random.choice(reading))
        average_reading_speed = round(sum(reading_speed) / len(reading_speed), 2)
        if average_reading_speed < 180:
            return f'Average reading rate --> slow pace reading (~{average_reading_speed})'
        elif 180 < average_reading_speed < 250:
            return f'Average reading rate --> average pace reading (~{average_reading_speed})'
        else:
            return f'Average reading rate --> fast pace reading (~{average_reading_speed})'


student_1 = SchoolSubject('Mathematics', random.choice(estimation_random))
student_2 = SchoolSubject('Mathematics', random.choice(estimation_random))
student_3 = SchoolSubject('Literature', random.choice(estimation_random))
student_4 = SchoolSubject('Literature', random.choice(estimation_random))
student_5 = SchoolSubject('Mathematics', random.choice(estimation_random))
student_6 = SchoolSubject('Literature', random.choice(estimation_random))

Mathematics.evaluations_mathematics()
Literature.evaluations_literature()
print(student_1.average_rating())
print('* * *')
print(Mathematics.grade())
print(Literature.reading_speed())
