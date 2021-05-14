from user import User


class Administrator(User):
    def __init__(self, username, hashed_password, role, major):
        super().__init__(username,hashed_password,role,major)

    def import_lesson(self, courses, name, teacher, major, units, capacity):
        """
        administrator inserts courses to the system. it returns the list of courses
        """
        courses.append([name, teacher, major, units, capacity,True])

    def accept_reject_unit_selection(self, user_info, stu, my_logger):
        for user in user_info:
            if user[0] == stu:
                for i, course in enumerate(user[5:]):
                    print(f"{i + 1}-{course}")
                break
        while True:
            try:
                result = input("do you accept the unit selection? y/n ")
                assert result in ['y', 'n']
            except AssertionError:
                print("you should enter one of the values y or n")
                my_logger.error("wrong input in line 23 administrator.py")
            else:
                if result == 'n':
                    for user in user_info:
                        if user[0] == stu:
                            del user[4:]
                            user.append(0)
                            return
                my_logger.info(f"{stu}'s unit selection was accepted by administrator")
                break



