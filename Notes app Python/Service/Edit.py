import sys
sys.path.insert(0, 'Model')
from Model.Note import Note

from datetime import datetime
from Service.Printer import Printer


class Edit():

    # Выводит все заметки и осуществляет выбор той, которую пользователь хочет изменить, в качестве аргументов принимает список заметок
    def enter_note(list_notes: Note):
        p = Printer
        p.print_list_notes(list_notes)
        title_for_del = input('Выбирете заметку (по заголовку): \n')
        for obj in list_notes:
            if (obj.title.lower() == title_for_del.lower()):
                return obj

    # Функция редактирует заголовок заметки. 
    def modify_title(obj: Note):
        try:
            add_title = input("Вветите новый заголовок: \n")
            obj.title = f'{add_title}'
            obj.date_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            print('\nИзменения внесены!')
        except AttributeError:
            print ('Заметка с таким именем не найдена!')

    # Функция редактирует тело заметки
    def modify_message(obj: Note):
        try:
            add_message = input("Вветите текст: \n")
            obj.message = f'{obj.message} {add_message}'
            obj.date_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            print('\nИзменения внесены!')
        except AttributeError:
            print ('Заметка с таким именем не найдена!')