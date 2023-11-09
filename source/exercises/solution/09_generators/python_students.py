# python_students.py

class PythonStudents:
    
    def __init__(self):
        self._students = []
        self._populate_students()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        ri = self.index
        self.index += 1
        if self.index > len(self._students):
            raise StopIteration()
        return self._students[ri]
    
    def _populate_students(self):
        names = ["Claus", "Anna", "Ben", "Diana", "Erik", "Fiona", "George", "Hannah", "Ivan", "Julia"]
        numbers = [1234, 5678, 9101, 1121, 3141, 5161, 7181, 9202, 1222, 3242]

        for i in range(10):
            self._students.append(Student(names[i], numbers[i]))





class Student:

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
            return self.__name

    @name.setter
    def name(self, name):
            self.__name = name.capitalize()

    def __add__(self, student):
            return Student('Anna the daugther', 1234)

    def __str__(self):
            return f'{self.name}, {self.cpr}'

    def __repr__(self):
            return f'{self.__dict__}'
