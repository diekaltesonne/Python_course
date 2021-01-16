# Первое задание у нас для разогрева.
# Ваша задача написать Python-модуль solution.py, внутри которого определен класс FileReader.
# Инициализатор этого класса принимает аргумент - путь до файла на диске.
# У класса должен быть метод read, возвращающий содержимое файла в виде строки.
# Еще один момент - внутри метода read вы должны обрабатывать исключение IOError, возникающее, когда файла, с которым был инициализирован класс,
# на самом деле нет на жестком диске.
# В случае возникновения такой ошибки метод read должен возвращать пустую строку ""
class FileReader(object):
    def __init__(self,Sourse):
        self.Sourse = Sourse

    def read(self):
        try:
            with open(self.Sourse,'r') as f:
                 return f.read()
        except IOError:
            return ""
