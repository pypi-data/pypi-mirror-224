class Ez_sqlite_except(Exception):
    pass


class Table_already_exists(Ez_sqlite_except):
    '''Вызывается, если таблица пытается создаться, когда уже существует'''
    pass


class Parameters_are_empty(Ez_sqlite_except):
    '''Вызывается, когда не передаются никаких параметров для создания таблицы'''
    pass


class Too_many_parameters(Ez_sqlite_except):
    '''Вызывается тогда, когда для создания записи передаются слишком много параметров'''
    pass


class Too_few_parameters(Ez_sqlite_except):
    '''Вызывается тогда, когда для создания записи передаются слишком мало параметров'''
    pass


class Invalid_parameter_type(Ez_sqlite_except):
    '''Вызывается тогда, когда для создания записи передаются неверные типы параметров'''
    pass


class Invalid_parameter_arg(Ez_sqlite_except):
    '''Вызывается тогда, когда для фильтрации записей передаётся аргумент, не находящийся в таблице'''
    pass


class Invalid_parameter_lenght(Ez_sqlite_except):
    '''Вызывается тогда, когда осуществляется поиск по записям таблицы больше, чем по 1 параметру'''
    pass


class Table_does_not_exist(Ez_sqlite_except):
    '''Вызывается тогда, когда несуществующую таблицу пытаются удалить'''
    pass