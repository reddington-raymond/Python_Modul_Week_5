'''
Question2: Create a "School" class in Python. This class should have the following features and functionality:

##### Features:
- "name"
- "foundation_year"
- "students"
- "teachers"
-
##### Methods:
- add_new_student(self, student_name, class): A method used to add a new student to the school. It takes the student's name and class and adds it to the "students" list.
- add_new_teacher(self, teacher_name, branch): A method used to add a new teacher to the school. It takes the teacher's name and major and adds it to the "teachers" dictionary.
- view_student_list(self): A method used to display the list of students enrolled in the school. List student names and classes.
- view_teacher_list(self): A method used to display the list of teachers working in the school. List teacher names and majors.
'''
class School:
    
    def __init__(self, name, foundation_year):
        self.name=name
        self.foundation_year=foundation_year
        self.students=[]
        self.teachers={}
    
    def add_new_student(self, student_name, grade):
        self.students.append((student_name, grade))
    
    def add_new_teacher(self, teacher_name, branch):        
        teacher_id = len(self.teachers) + 1
        self.teachers[teacher_id] = {
        'teacher_name': teacher_name,
        'branch': branch
    }
    
    def view_student_list(self):
        print('Ogrenci Listesi :  ')
        print('------------------------------')
        for student_name, grade in self.students:
            print(f"{student_name} - Sınıf: {grade}")
        print()
            
    def view_teacher_list(self):
        print('Ogretmen Listesi :  ')
        print('------------------------------')
        for teacher_id, teacher_info in self.teachers.items():
            print(f"{teacher_id}: {teacher_info['teacher_name']} - {teacher_info['branch']}")
        print()
        
school1=School('Cumhuriyet', 1984)
school2=School('Yeni Levent', 1987)

school1.add_new_student('ilkay arslanoglu', '8C')
school1.add_new_student('vildan arslanoglu', '4B')

school1.add_new_teacher('Yavuz Hoca', 'Matematik')
school1.add_new_teacher('Ihtiyar Hoca', 'Ingilizce')

school1.view_teacher_list()
school1.view_student_list()

    


