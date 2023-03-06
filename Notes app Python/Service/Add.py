from datetime import datetime
from Model.Note import Note

# Создает и заполняет заметку, в результате работы возвращает объект "заметка"
class Add():

    def add(count):  
        id = count
        title = (input('Заголовок: \n'))
        message = (input('Текст: \n'))
        date_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        obj_note = Note(id, title, message, date_time) 
        return obj_note

