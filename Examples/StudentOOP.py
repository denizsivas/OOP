class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        return f'Student ID: {self.student_id} | Student Name: {self.student_name} | Class: {self.student_class}'
    
wilson_medina = Student('S122', 'Wilson Medina', 'VI')
print(wilson_medina.display())