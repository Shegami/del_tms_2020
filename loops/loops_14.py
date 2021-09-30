"""
Создать список учеников
подобной структуры.
Определить средний балл
каждого студента по всем
предметам, и вывести
сведения о студентах,
средний балл которых
больше 4.

pupils = [
 {
 'firstname': 'Masha',
 'Group': 42,
 'physics': 7,
 'informatics': 6,
 'history': 8,
 },
]
"""


def average_mark(student):
    avg_mark = sum(
        [
            student['physics'],
            student['math'],
            student['history']
        ]) / 3
    return avg_mark


def main():
    students = [
        {
            'firstname': 'Lesha',
            'group': 45,
            'physics': 7,
            'math': 9,
            'history': 7,
        },
        {
            'firstname': 'Lera',
            'group': 45,
            'physics': 6,
            'math': 7,
            'history': 10,
        },
        {
            'firstname': 'Pasha',
            'group': 45,
            'physics': 4,
            'math': 5,
            'history': 4,
        }
    ]

    for student in students:
        avg_mark = average_mark(student)
        if avg_mark > 4:
            for key, value in student.items():
                print(
                    f'{key}: {value}'
                )
        print('\n')


if __name__ == '__main__':
    main()
