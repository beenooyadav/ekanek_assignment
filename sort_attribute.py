from operator import attrgetter
from random import randrange

from typing import List


class Student:
    """
    Student class
    """

    def __init__(self, name: str, age: int, marks: int, roll_numer: str):
        self.name: str = name
        self.age: int = age
        self.marks: int = marks
        self.roll_number: str = roll_numer

    def __repr__(self):
        return repr((self.name, self.age, self.marks, self.roll_number))


def sort(students: List[Student], criteria: List[str]) -> List[Student]:
    """
    Takes list of students objects and return the list sorted by given attribute list
    :param students: list of students
    :param criteria: list of attribute
    :return: sorted list of students based on criteria list

    Time complexity:
    the sort is O(n log n) both on average and in the worst case.

    Space complexity:
    the sort is Ω(n) since python uses time sort which is similar to merge sort. they use auxillary list to sort.
    """
    students.sort(key=attrgetter(*criteria))
    return students


if __name__ == '__main__':
    #  to test the function you may provide your own list
    number_of_students = 5
    student_list: List[Student] = []
    for i in range(number_of_students):
        student = Student(name=f'student_{99-randrange(10, 20)}', age=randrange(20, 101), marks=randrange(35, 100), roll_numer=f'{randrange(10, 20)}_ekanek')
        student_list.append(student)

    print(f'Original list:\n{student_list}\n')
    print(f"sorted by 'name':\n{sort(students=student_list, criteria=['name'])}\n")
    print(f"sorted by 'name', 'age':\n{sort(students=student_list, criteria=['name', 'age'])}\n")
    print(f"sorted by 'age', 'name':\n{sort(students=student_list, criteria=['age', 'name'])}\n")
    print(f"sorted by 'marks', 'roll_number', 'age':\n{sort(students=student_list, criteria=['marks', 'roll_number', 'age'])}\n")
    print(f"sorted by 'age', 'marks', 'name', 'roll_number':\n{sort(students=student_list, criteria=['age', 'marks', 'name', 'roll_number'])}\n")
