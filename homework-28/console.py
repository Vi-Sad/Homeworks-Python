from homework_28 import *

print('-' * 100)

new_name = input('Введите имя нового клиента Банка --> ')
new_address = input('Введите город проживания клиента --> ')
active_client = new_name

BANK = Bank(list_clients_main, active_client)
print(BANK.new_customer(new_name, new_address))

print('-' * 100)
print(f'"Главный" клиент --> {active_client}')

while True:

    print('-' * 100)

    print('Функции Банка:\n1) Добавить нового клиента\n2) Удалить клиента\n3) Посмотреть полную информацию о клиенте\n'
          '4) Посмотреть все счета клиента\n5) Сменить "главного" клинта\n6) Добавить новый счет\n7) Удалить счет\n'
          '8) Посмотреть баланс счета\n9) Вложить деньги\n10) Снять деньги\n11) Посмотреть историю всех транзакций\n'
          '12) Посмотреть транзакции счета\n13) Посмотреть полную информацию всех клиентов\n14) Закрыть программу')
    command = input('Введите номер команды --> ')

    if command == '1':
        print('-' * 100)
        BANK = Bank(list_clients_main, active_client)
        new_name = input('Введите имя нового клиента Банка --> ')
        new_address = input('Введите город проживания клиента --> ')
        print(BANK.new_customer(new_name, new_address))

    elif command == '2':
        print('-' * 100)
        BANK = Bank(list_clients_main, active_client)
        delite_client = input('Введите имя клиента --> ')
        print(BANK.delite_customer(delite_client))

    elif command == '3':
        print('-' * 100)
        BANK = Bank(list_clients_main, active_client)
        BANK.information()

    elif command == '4':
        print('-' * 100)
        CUSTOMER = Customer(list_clients_main, active_client)
        CUSTOMER.viewing_accounts()

    elif command == '5':
        print('-' * 100)
        check_client = input('Введите имя клиента --> ')
        check_list = any(i['client'] == check_client for i in list_clients_main)
        if check_list:
            active_client = check_client
            print(f'"Главный" клиент --> {active_client}')
        else:
            print(f'Клиент с именем "{check_client}" НЕ найден\n"Главный" клиент --> {active_client}')

    elif command == '6':
        print('-' * 100)
        CUSTOMER = Customer(list_clients_main, active_client)
        print(CUSTOMER.new_account())

    elif command == '7':
        print('-' * 100)
        CUSTOMER = Customer(list_clients_main, active_client)
        remove_account = input('Введите номер счета --> ')
        print(CUSTOMER.delite_account(remove_account))

    elif command == '8':
        print('-' * 100)
        ACCOUNT = Account(list_clients_main, active_client)
        active_account = input('Введите номер счета --> ')
        ACCOUNT.viewing_balance(active_account)

    elif command == '9':
        print('-' * 100)
        ACCOUNT = Account(list_clients_main, active_client)
        active_account = input('Введите номер счета --> ')
        deposit_money = float(input('Введите сумму денег --> '))
        TRANSACTION = Transaction(list_clients_main, active_client)
        TRANSACTION.history_transactions(ACCOUNT.deposit_money(active_account, deposit_money), active_account)

    elif command == '10':
        print('-' * 100)
        ACCOUNT = Account(list_clients_main, active_client)
        active_account = input('Введите номер счета --> ')
        withdraw_money = float(input('Введите сумму денег --> '))
        TRANSACTION = Transaction(list_clients_main, active_client)
        TRANSACTION.history_transactions(ACCOUNT.withdraw_money(active_account, withdraw_money), active_account)

    elif command == '11':
        print('-' * 100)
        TRANSACTION = Transaction(list_clients_main, active_client)
        TRANSACTION.all_transactions()

    elif command == '12':
        print('-' * 100)
        TRANSACTION = Transaction(list_clients_main, active_client)
        active_account = input('Введите номер счета --> ')
        TRANSACTION.account_transactions(active_account)

    elif command == '13':
        print('-' * 100)
        BANK = Bank(list_clients_main, active_client)
        BANK.all_information()

    elif command == '14':
        print('-' * 100)
        print('Программа успешно завершена')
        print('-' * 100)
        break

    else:
        print('-' * 100)
        print(f'Команда "{command}" отсутствует')
