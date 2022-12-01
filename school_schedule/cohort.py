class Cohort: 
    def __init__(self, name, student_list):
        self.name = name
        self.student_list = student_list

    def get_num_students(self):
        return len(self.student_list)

    def add_student(self, new_student):
        self.student_list.append(new_student)

    def get_student_summaries(self):
        result = f"Students in {self.name}: \n"
        for student in self.student_list:
            result += student.summary() + "\n"
        return result