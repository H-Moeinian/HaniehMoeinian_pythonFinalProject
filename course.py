class Course:
    def __init__(self, name, teacher, major, units, capacity, active=True):
        self.name = name
        self.teacher = teacher
        self.units = int(units)
        self.capacity = int(capacity)
        self.active = active
        self.major = major

    def __str__(self):
        return f"course name: {self.name}, teacher: {self.teacher}, units: {self.units}, " \
               f"capacity: {self.capacity}"

    def decrease_capacity(self,courses):
        for course in courses:
            if self.name == course[0]:
                course[4] = int(course[4]) - 1

    def increase_capacity(self,courses):
        for course in courses:
            if self.name == course[0]:
                course[4] = int(course[4]) + 1