import os
import json
import datetime
import csv
from Notes import  notes_menu
from Finance import finance_menu
from Contacts import contacts_menu
from Tasks import tasks_menu

def load_data(file_path, default_data):
    if not os.path.exists(file_path):
        save_data(file_path, default_data)
        return default_data
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main_menu():
    while True:
        print('\nДобро пожаловать в Персональный помощник!')
        print('Выберите действие:')
        print('1. Управление заметками')
        print('2. Управление задачами')
        print('3. Управление контактами')
        print('4. Управление финансовыми записями')
        print('5. Калькулятор')
        print('6. Выход')
        choice = input('Введите номер действия: ')
        if choice == '1':
            notes_menu()
        elif choice == '2':
            tasks_menu()
        elif choice == '3':
            contacts_menu()
        elif choice == '4':
            finance_menu()
        elif choice == '5':
             calculator_menu()
        elif choice == '6':
            print('До свидания!')
            break
        else:
            print('Некорректный выбор. Попробуйте снова.')

def calculator_menu():
    print('\nКалькулятор')
    while True:
        expression = input('Введите выражение для вычисления или "назад" для возврата: ')
        if expression.lower() == "назад":
            break
        try:
            # Для безопасности можно использовать ast.literal_eval
            import ast
            result = eval(expression, {'__builtins__': None}, {})
            print(f'Результат: {result}')
        except Exception as e:
            print(f'Ошибка: {e}')

if __name__ == '__main__':
    main_menu()