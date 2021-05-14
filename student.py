from course import Course
from user import User


class Student(User):
    def __init__(self, username, hashed_password, role, major):
        super().__init__(username, hashed_password, role, major)

    def take_lessons(self,user_info, courses, my_logger):
        print("------------------------------------------")
        print("this is the list of courses you are allowed to take:")
        major_courses = []
        major_no_courses = []
        for i, course in enumerate(courses):
            if self.major == course[2]:
                major_courses.append(course)
                major_no_courses.append(i)
        for i, course in enumerate(major_courses):
            print(f"{i + 1}-name: {course[0]}, teacher: {course[1]},"
                  f" units: {course[3]}, capacity: {course[4]}")
        for j, student in enumerate(user_info):
            if student[0] == self.username:
                while True:
                    if student[2] == 'student':
                        if int(student[4]) < 20:
                            try:
                                course_no = int(input("which course do you want to choose? ")) - 1
                            except ValueError:
                                print("you should enter a number")
                                my_logger.error("wrong input in line 27 student.py")
                            else:
                                if f"{courses[major_no_courses[course_no]][0]}" not in student:
                                    if courses[major_no_courses[course_no]][5]:
                                        if int(courses[major_no_courses[course_no]][3]) +\
                                                int(student[4]) < 20:
                                            student.append(courses[major_no_courses[course_no]][0])
                                            student[4] = int(courses[major_no_courses[course_no]][3]) + \
                                                             int(student[4])
                                            my_logger.info(f"{student[0]} selected course {courses[major_no_courses[course_no]][0]}")
                                            corse = Course(*courses[major_no_courses[course_no]])
                                            corse.decrease_capacity(courses)
                                        else:
                                            print("you can not take more than 20 units in"
                                                  " a semester!")
                                            return False
                                    else:
                                        print("this lesson's capacity is full!")
                                else:
                                    print("you can not take a lesson two times in a semester!")
                        if int(student[4]) < 10:
                            print("you need to take at least 10 units")
                            continue
                        else:
                            break

    def see_selected_courses(self, user_info):
        for user in user_info:
            if user[2] == 'student':
                if user[0] == self.username:
                    if user[4] == '0':
                        print("you haven't selected any courses yet!")
                        return
                    print("these are the courses you have selected: ")
                    for i, course in enumerate(user[5:]):
                        print(f"{i+1}-{course}")

    def omit_course(self, user_info, course_no, courses):
        for user in user_info:
            if user[0] == self.username:
                course_name = user[5 + course_no]
                user.remove(user[5+course_no])
                for course in courses:
                    if course[0] == course_name:
                        crs = Course(*course)
                        crs.increase_capacity(courses)
                        no_units = crs.units
                        user[4] = int(user[4])-int(no_units)






