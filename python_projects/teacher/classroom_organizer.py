import roster
import itertools

sr = roster.student_roster
qq = []

for student in sr:
    qq.append(student['name'])

class ClassroomOrganizer:
    def __init__(self):
        self.sorted_class = self._sort_students()

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        return self

    def _sort_students(self):
        morning_call = []
        for stud in sr:
            morning_call.append(stud['name'])
        return morning_call

    def five_by_two(self):
        itertools.combinations(qq, 2)


x = itertools.combinations(qq, 2)
print(x)
