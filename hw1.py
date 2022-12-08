class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecture(self,lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
        else :
            return 'Ошибка'

   

    def __str__(self):
        def average_value(self):
            sum = 0
            count = 0
            for course in self.grades.keys():
                for grade in self.grades[course]:
                    sum += grade
                    count += 1
            result = round(sum / count, 1)
            return result          
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл: {average_value(self)}'
        return res

    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
class Reviewer(Mentor):       
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git'] 

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git'] 

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 9)
cool_mentor.rate_hw(best_student, 'Git', 8)
cool_mentor.rate_hw(best_student, 'Git', 8) 
print(best_student.grades)

best_lecturer = Lecturer('Number', 'One')
best_lecturer.courses_attached += ['Python']

best_student.rate_lecture(best_lecturer, 'Python', 10)

print(best_lecturer.grades)

print(best_student)








