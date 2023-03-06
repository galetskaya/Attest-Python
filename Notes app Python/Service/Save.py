import sys
sys.path.insert(0, 'Model')

from Model.Note import Note

class Save():

    # Функция сохраняет состояние приложения (заметки из оперативной памяти) и ID для будущей заметки в файл
    def save_parameters(file, file_count, list_notes: Note, count: int):

        with open(file, 'r', encoding='utf-8'), open(file, 'w', encoding='utf-8') as f:
            for obj in list_notes:
                f.write(
                    f'{obj.id};{obj.title};{obj.message};{obj.date_time}\n')

        with open(file_count, 'r', encoding='utf-8'), open(file_count, 'w', encoding='utf-8') as k:
            k.write(str(count))
