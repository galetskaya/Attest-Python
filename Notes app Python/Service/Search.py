from Model.Note import Note

class Search():

    # функция осуществляет поиск заметки по заголовку
    def search_note(list_notes: Note):
        title_for_del = input('Введите заголовок для поиска: \n')
        for obj in list_notes:
            if (obj.title.lower() == title_for_del.lower()):
                return obj
    