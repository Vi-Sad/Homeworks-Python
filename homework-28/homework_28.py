# Задача, связанная с управлением банковским счетом:

# Account (Счет):
# -	Свойства: номер счета, баланс, владелец счета.
# -	Методы: вывод информации о счете, внесение/снятие денег, проверка баланса.

# Transaction (Транзакция):
# -	Свойства: дата, тип (пополнение/снятие), сумма, счет.
# -	Методы: запись транзакции, вывод информации о транзакции.

# Customer (Клиент):
# -	Свойства: имя, адрес, список банковских счетов.
# -	Методы: создание нового счета, удаление счета, вывод информации о клиенте.

# Bank (Банк):
# -	Свойства: список клиентов, список всех транзакций.
# -	Методы: добавление/удаление клиента, вывод общей информации о банке, вывод списка всех транзакций.

# Требования:
# -	Каждый класс должен иметь конструктор для инициализации объектов.
# -	Методы классов должны быть реализованы так, чтобы обеспечивать целостность данных и безопасное выполнение операций.
# -	Классы должны взаимодействовать друг с другом так, чтобы отражать типичные операции с банковским счетом.

# ---------------------------------------------------------------------------------------------------------------------

# Run console.py

# ---------------------------------------------------------------------------------------------------------------------

import random

list_clients_main = []


class Bank:
    def __init__(self, list_clients: list, main_client):
        self.list_clients = list_clients
        self.main_client = main_client

    def new_customer(self, client, address):
        new_number = random.choice(range(1000000))
        new_client = {'client': client, 'address': address, 'list_accounts': [{'number': str(new_number),
                                                                               'balance': 0}], 'list_operations': []}
        self.list_clients.append(new_client)

        len_list = len(list_clients_main) - 1
        counter = 0
        for i in self.list_clients:
            if len_list == counter:
                break
            else:
                counter += 1
                if i["client"] == client:
                    self.list_clients.remove(self.list_clients[-1])
                    return f'Счет Банка на имя "{client}" уже существует!'
        return f'Счет Банка на имя "{client}" был успешно добавлен'

    def delite_customer(self, client):
        if any(client == i['client'] for i in self.list_clients):
            for i in self.list_clients:
                if i['client'] == client:
                    self.list_clients.remove(i)
            return f'Счет Банка на имя "{client}" был успешно удален'
        else:
            return f'Счет Банка на имя "{client}" НЕ найден'

    def information(self):
        for i in self.list_clients:
            if i['client'] == self.main_client:
                print(f'Полная информация о клиенте "{i["client"]}":\n- Проживает в г. {i["address"]}\n'
                      f'Номера счетов и баланс:')
                for j in i['list_accounts']:
                    print(f'- Счет №{j["number"]}: {j["balance"]} руб.')

    def all_information(self):
        print('Полная информация о всех клиентах в словаре:')
        for i in self.list_clients:
            print(i)


class Customer(Bank):
    def __init__(self, list_clients: list, main_client):
        super().__init__(list_clients, main_client)

    def viewing_accounts(self):
        print('Все счета:')
        for i in self.list_clients:
            if i['client'] == self.main_client:
                for j in i['list_accounts']:
                    print(f'- №{j["number"]}')

    def new_account(self):
        new_number = random.choice(range(1000000))
        for i in self.list_clients:
            if i['client'] == self.main_client:
                i['list_accounts'].append({'number': str(new_number), 'balance': 0})
        return f'Счет Банка №{new_number} был успешно создан'

    def delite_account(self, account):
        for i in self.list_clients:
            if i['client'] == self.main_client:
                for j in i['list_accounts']:
                    if j['number'] == account:
                        i['list_accounts'].remove(j)
                        return f'Счет Банка №{account} был успешно удален'
                    else:
                        return f'Счет Банка №{account} НЕ найден'


class Account(Bank):
    def __init__(self, list_clients: list, main_client):
        super().__init__(list_clients, main_client)

    def viewing_balance(self, account):
        for i in self.list_clients:
            if i['client'] == self.main_client:
                if any(j['number'] == account for j in i['list_accounts']):
                    for j in i['list_accounts']:
                        if j['number'] == account:
                            print(f'Баланс счета №{account}: {j["balance"]} руб.')
                else:
                    print(f'Баланс счета №{account} НЕ найден')

    def deposit_money(self, account, money):
        for i in self.list_clients:
            if i['client'] == self.main_client:
                if any(j['number'] == account for j in i['list_accounts']):
                    for j in i['list_accounts']:
                        if j['number'] == account:
                            j["balance"] += abs(money)
                            print(f'На счет №{account} поступило {money} руб.')
                    return money
                else:
                    print(f'Счет №{account} НЕ найден')
                    return None

    def withdraw_money(self, account, money):
        for i in self.list_clients:
            if i['client'] == self.main_client:
                if any(j['number'] == account for j in i['list_accounts']):
                    for j in i['list_accounts']:
                        if j['number'] == account:
                            a = j["balance"]
                            j["balance"] -= abs(money)
                            if j["balance"] < 0:
                                j["balance"] = a
                                print(f'На счете №{account} не хватает средств')
                            else:
                                print(f'С счета №{account} снято {money} руб.')
                    return -money
                else:
                    print(f'Счет №{account} НЕ найден')


class Transaction(Bank):
    def __init__(self, list_clients: list, main_client):
        super().__init__(list_clients, main_client)

    def history_transactions(self, money, account):
        for i in self.list_clients:
            if i['client'] == self.main_client:
                i['list_operations'].append({f'account_{account}': money})

    def account_transactions(self, account):
        for i in self.list_clients:
            if i['client'] == self.main_client:
                if any(account == j['number'] for j in i['list_accounts']):
                    print(f'Транзакции счета №{account}:')
                    for j in i['list_operations']:
                        for n in j:
                            if n == f'account_{account}':
                                print(j[n])
                else:
                    print(f'Счет №{account} НЕ найден')

    def all_transactions(self):
        print('Все транзакции:')
        for i in self.list_clients:
            if i['client'] == self.main_client:
                for j in i['list_operations']:
                    print(j)
                  
