from typing import Tuple
import sqlite3

from errors import *
from const import *

class sqlite:
    def __init__(self, name: str):
        #Имя для таблицы
        self.name = name


    def exists(self) -> bool:
        '''Проверка на существовании таблицы'''
        with sqlite3.connect(relative_path) as connect:
            cursor: sqlite3.Cursor = connect.cursor()

            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.name}';")
            result = cursor.fetchone()    

            return True if result else False


    def get_data(self) -> Tuple[int, tuple]:
        '''функция возвращает длинну и параметры таблицы'''
        if self.exists():
            with sqlite3.connect(relative_path) as connect:
                cursor: sqlite3.Cursor = connect.cursor()

                pragma_query = f"PRAGMA table_info({self.name});"

                cursor.execute(pragma_query)
                table_info = cursor.fetchall()

                fields = tuple((field[1], field[2]) for field in table_info)

                return len(table_info), fields

        raise Table_does_not_exist('Таблицы не существует')


    def create_table(self, **kwargs) -> bool:
        '''функция создает таблицу, если её нет'''
        if not len(kwargs):
            raise Parameters_are_empty('Необходимо передать параменты для создания таблицы')
        
        if not self.exists():
            #если таблица не существует
            with sqlite3.connect(relative_path) as connect:
                cursor: sqlite3.Cursor = connect.cursor()

                fields = ',\n'.join(f'{key} {value}' for key, value in kwargs.items())

                create_table_query = f'''
                CREATE TABLE {self.name} (
                    id INTEGER PRIMARY KEY,
                    {fields}
                );
                '''
                cursor.execute(create_table_query)

                connect.commit()

                return True
        
        raise Table_already_exists('Таблица уже создана')

    
    def add_row(self, *args) -> bool:
        '''функция добавляет запись в таблицу и возвроащает True, если всё нормально'''
        if self.exists():
            len_, fields = self.get_data()
            len_ -= 1
            fields = fields[1:]

            len_options = len(args)

            if len_options == len_:
                for i in range(len(fields)):
                    if type(args[i]) == int and fields[i][1] != INT:
                        raise Invalid_parameter_type('Неверный тип аргумента/ов')
                    elif type(args[i]) == str and fields[i][1] != TEXT:
                        raise Invalid_parameter_type('Неверный тип аргумента/ов')

                with sqlite3.connect(relative_path) as connect:
                    cursor: sqlite3.Cursor = connect.cursor()

                    query = f'INSERT INTO {self.name} ({", ".join(field[0] for field in fields)}) VALUES ({("?, " * len_)[:-2]})'
                    cursor.execute(query, args)

                    connect.commit()

                    return True
            elif len_options > len_:
                raise Too_many_parameters(f'Слишком много параметров, лишние {args[len_:]}')
            
            raise Too_few_parameters(f'Не было переданно {len_ - len_options}')
        
        raise Table_does_not_exist('Таблицы не существует')


    def get_rows(self) -> tuple:
        '''функция возвращает кортеж всех записей таблицы'''
        if self.exists():
            with sqlite3.connect(relative_path) as connect:
                cursor: sqlite3.Cursor = connect.cursor()

                query = f'SELECT * FROM {self.name}'

                cursor.execute(query)

                result = tuple(cursor.fetchall())

                return result

        raise Table_does_not_exist('Таблицы не существует')


    def row_exist(self, **kwargs) -> bool:
        '''функция проверяет, если ли запись в таблице по 1 параметру'''
        if len(kwargs) != 1:
            raise Invalid_parameter_lenght('Поиск осуществляется по 1 параметру')

        elif self.exists():
            # Получаем единственный ключ и его значение
            key, value = kwargs.popitem()

            # Получаем данные таблицы и все строки
            _, table_data, all_rows = self.get_data(), self.get_rows()          

            # Поиск соответствующей строки
            for data in table_data:
                if data[0] == key:
                    index = table_data.index(data)
                    for row in all_rows:
                        if row[index] == value:
                            return True
            
            return False
        
        raise Table_does_not_exist('Таблицы не существует')


    def delete_table(self) -> bool:
        '''функция удаляет таблицу, возвращает True, если не было ошибок'''
        if self.exists():
            with sqlite3.connect(relative_path) as connect:
                cursor: sqlite3.Cursor = connect.cursor()
                
                query = f'DROP TABLE {self.name}'

                cursor.execute(query)

                return True

        raise Table_does_not_exist('Таблицы не существует')


    def delete_row(self, pk: int) -> bool:
        '''функция удаляет запись из таблицы по id, возвращает True, если не было ошибок'''
        if self.exists():
            with sqlite3.connect(relative_path) as connect:
                cursor: sqlite3.Cursor = connect.cursor()

                query = f'DELETE FROM {self.name} WHERE id = {pk}'

                cursor.execute(query)
                connect.commit()

            return True

        raise Table_does_not_exist('Таблицы не существует') 
    
    
    def filter_by(self, **kwargs) -> tuple:
        '''функция возвращает отфильтрованные записи в виде кортежа'''
        if len(kwargs) != 1:
            raise Invalid_parameter_lenght('Поиск осуществляется по 1 параметру')

        if self.exists():
            with sqlite3.connect(relative_path) as connect:
                cursor: sqlite3.Cursor = connect.cursor()

                # Получаем единственный ключ и его значение
                key, value = kwargs.popitem()

                _, table_data = self.get_data()
                if key not in [data[0] for data in table_data]:
                    raise Invalid_parameter_arg('Такого параметра не существует')

                query = f"SELECT * FROM {self.name} WHERE {key} = '{value}';"

                cursor.execute(query)

                return tuple(cursor.fetchall())
        
        raise Table_does_not_exist('Таблицы не существует')


    def order(self, arg) -> tuple:
        '''Функция возвращает отсортированный кортеж всех записей'''
        if self.exists():
            with sqlite3.connect(relative_path) as connect:
                cursor: sqlite3.Cursor = connect.cursor()

                _, table_data = self.get_data()
                if arg  not in [data[0] for data in table_data]:
                    raise Invalid_parameter_arg('Такого параметра не существует')

                query = f'SELECT * FROM {self.name} ORDER BY {arg};'

                cursor.execute(query)

                return tuple(cursor.fetchall())
        
        raise Table_does_not_exist('Таблицы не существует')
    

