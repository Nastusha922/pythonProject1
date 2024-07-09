class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.course_grades:
                    lecturer.course_grades[course] += [grade]
                else:
                    lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_grade(self, course, grade):
        if course not in self.grades:
            self.grades[course] = []
        self.grades[course].append(grade)

    #def __average_hw_grade(self, course):
        #if course in self.grades.keys() and len(self.grades.values()) > 0:
            #grades = self.grades.values()
            #sum_grades = sum(grades)
            #return round((sum_grades / len(grades)), 1)
        #else:
            #return None

    def __average_hw_grade(self):
        middle_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
            middle_sum += 1
            if middle_sum == 0:
                return f'Студент еще не получал оценки'
            else:
                return f'{middle_sum / len(self.grades.values()):.2f}'

    #def __average_hw_grade(self, course):
        #if not isinstance(course, str):
            #return 'Ошибка'
        #avg_grade = 0
        #for course in self.grades.items():
            #avg_grade += sum(self.grades.get(course, []))/len(self.grades.get(course, []))
        #return round(avg_grade, 1)

        #if len(self.grades) == 0:
            #return None
        #else:
            #for grade in self.grades.values():
                #sumar = sum(self.grades)
                #sumar = sumar + grade
            #return round(sumar/len(self.grades), 1)

    def __str__(self):
        average = best_student.__average_hw_grade()
        some_student = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашние задания: {average}\n' f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return some_student

    #def __lt__(self, other):
        #return (best_student.__average_hw_grade('Python') < best_student1.__average_hw_grade('Python'))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def add_grade(self, course, grade):
        if course not in self.course_grades:
            self.course_grades[course] = []
        self.course_grades[course].append(grade)

    def __average_lecture_grade(self, course):
        if course in self.course_grades and len(self.course_grades.values()) > 0:
            grades = self.course_grades.values()
            sum_grades = sum(grades)
            return round((sum_grades / len(grades)), 1)
        else:
            return None

    def __str__(self):
        mean_grade = cool_lecturer.__average_lecture_grade('Python')
        self.some_lecturer = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {mean_grade}\n'
        return self.some_lecturer

    def __str1__(self):
        mean_grade = cool_lecturer1.average_lecture_grade('Python')
        self.some_lecturer = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {mean_grade}'
        return self.some_lecturer

    def __lt__(self, cool_lecturer_1):
        return (cool_lecturer.__average_lecture_grade() < cool_lecturer_1.__average_lecture_grade())


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
        self.cool_reviewer = f'Имя: {self.name}\n' f'Фамилия: {self.surname}'
        return self.cool_reviewer

best_student = Student('Ruoy', 'Eman', 'M')
best_student.courses_in_progress += ['Python, Git']
best_student.finished_courses += ['Введение в программирование']
print(best_student)


best_student1 = Student('Arnold', 'Schwarzneger', 'M')
best_student1.courses_in_progress += ['Python, Git']
best_student1.finished_courses += ['Введение в программирование']
students_list = [best_student, best_student1]

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
print(cool_lecturer)

cool_lecturer1 = Lecturer('John', 'Uik')
cool_lecturer1.courses_attached += ['Python']
lecturer_list = [cool_lecturer, cool_lecturer1]

best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 9)
best_student.rate_lect(cool_lecturer, 'Python', 8)

best_student.rate_lect(cool_lecturer1, 'Python', 6)
best_student.rate_lect(cool_lecturer1, 'Python', 8)
best_student.rate_lect(cool_lecturer1, 'Python', 9)


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
print(cool_reviewer)

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(best_student1, 'Python', 5)
cool_reviewer.rate_hw(best_student1, 'Python', 8)
cool_reviewer.rate_hw(best_student1, 'Python', 5)

#print(best_student < best_student1)
#print(cool_lecturer < cool_lecturer1)

def grades_students(students_list, course):
    overall_student_rating = 0
    lectors = 0
    for listener in students_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(listener.grades[course])
            average_student_score += overall_student_rating
            lectors += 1
    if overall_student_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'round({overall_student_rating / lectors}, 1)'


def grades_lecturers(lecturer_list, course):
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.course_grades.keys():
            lecturer_average_rates = 0
            for rate in lecturer.course_grades[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.course_grades[course])
            average_rating += overall_lecturer_average_rates
            b += 1
    if average_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'round({average_rating / b}, 1)'

