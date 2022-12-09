class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avarege_grade(self):
        return round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)

    def __str__(self):
        res_1 = ', '.join(self.courses_in_progress)
        res_2 = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avarege_grade()}\nКурсы в процессе изучения: {res_1}\nЗавершенные курсы: {res_2}\n'
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avarege_grade() < other.avarege_grade()
        else:
            return 'Нельзя сравнивать'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avarege_grade(self):
        return round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avarege_grade()}\n'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return  self.avarege_grade() < other.avarege_grade()
        else:
            return 'Нельзя сравнивать'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

def course_grate_hw(students_list, course):
    sum_grate = 0
    number_grate = 0
    for student in students_list:
        if course in student.grades.keys():
            number_grate += len(student.grades[course])
            for grate in student.grades[course]:
                sum_grate += grate
    return print(f'Средняя оценка за д/з по курсу {course}: {round(sum_grate / number_grate, 1)}\n')

def course_grate_lecture(lecturers_list, course):
    sum_grate = 0
    number_grate = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades.keys():
            number_grate += len(lecturer.grades[course])
            for grate in lecturer.grades[course]:
                sum_grate += grate
    return print(f'Средняя оценка за лекции по курсу {course}: {round(sum_grate / number_grate, 1)}\n')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
good_student = Student('Very', 'Good', 'm')
good_student.finished_courses += ['Git']
good_student.courses_in_progress += ['Python']
best_lecturer = Lecturer('Number', 'One')
best_lecturer.courses_attached += ['Python', 'Git']
main_lecturer = Lecturer('Ron', 'Jones')
main_lecturer.courses_attached += ['Python', 'Git']
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']
best_reviewer = Reviewer('Mark','Dark')
best_reviewer.courses_attached += ['Python']

list_of_students = [good_student, best_student,]
list_of_lecturer = [best_lecturer, main_lecturer]

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 9)
cool_mentor.rate_hw(best_student, 'Git', 9)
best_reviewer.rate_hw(good_student, 'Python', 10)
best_reviewer.rate_hw(good_student, 'Python', 9)
best_reviewer.rate_hw(good_student, 'Python', 8)
best_student.rate_lecture(best_lecturer, 'Python', 10)
best_student.rate_lecture(best_lecturer, 'Git', 9)
best_student.rate_lecture(best_lecturer, 'Python', 10)
best_student.rate_lecture(best_lecturer, 'Git', 10)
best_student.rate_lecture(main_lecturer, 'Git', 10)
good_student.rate_lecture(main_lecturer, 'Python', 10)
good_student.rate_lecture(main_lecturer, 'Pithon', 10)
best_student.rate_lecture(main_lecturer, 'Git', 10)

print(best_student)
print(good_student)
print(best_lecturer)
print(main_lecturer)
print(best_reviewer)
print(cool_mentor)

course_grate_hw(list_of_students,'Python')
course_grate_hw(list_of_students,'Git')
course_grate_lecture(list_of_lecturer, 'Python')
course_grate_lecture(list_of_lecturer, 'Git')

print(best_student > good_student )

print(main_lecturer < best_lecturer)

print(good_student < best_lecturer)

print(good_student < best_reviewer)








