import sys
sys.path.insert(0, 'Model')
from Service.Printer import Printer
from Model.Note import Note


class Download():

    # принимает в качестве аргумента путь к файлу, который содержит ID, который будет присвоен следующей заметке
    def import_count(count):
        with open(count, 'r', encoding='utf-8') as k:
            count = k.readlines()
        return int(count[0])
    
    # принимает в качестве аргумента путь к файлу, который содержит все схраненные заметки,
    # таким образом, программа загружает то состояние, на котором было выполнено последнее сохранение.
    def import_data(file):
        with open(file, 'r', encoding='utf-8') as k:
            lines = k.readlines()
            lst1 = []
            list_notes = []
            for each in lines:
                if each.__contains__(";"):
                    line = each.replace("\n", "")
                    lst1 = line.split(";")
                    list_notes.append(Note(lst1[0], lst1[1], lst1[2], lst1[3]))
                    lst1 = []
            return list_notes
