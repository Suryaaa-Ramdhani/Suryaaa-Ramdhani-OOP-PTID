class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}"

class Lecturer(Person):
    def _init_(self, name, age, nidn, course):
        super()._init_(name, age)
        self.nidn = nidn
        self.course = course
    
    def teach(self):
        return f"🎓 {self.name} is teaching {self.course}"
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\nNIDN: {self.nidn}\nCourse: {self.course}"

class Student(Person):
    def _init_(self, name, age, nim, major):
        super()._init_(name, age)
        self.nim = nim
        self.major = major
    
    def study(self):
        return f"📚 {self.name} is studying in {self.major} major"
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\nNIM: {self.nim}\nMajor: {self.major}"

class UniversitySystem:
    def _init_(self):
        self.lecturers = []
        self.students = []
    
    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)
    
    def add_student(self, student):
        self.students.append(student)
    
    def display_all_data(self):
        print("=" * 50)
        print("🏫 UNIVERSITY UNDIKMA")
        print("=" * 50)
        
        print("\n👨‍🏫 DATA ")
        print("-" * 30)
        for lecturer in self.lecturers:
            print(lecturer.display_info())
            print(lecturer.teach())
            print("-" * 20)
        
        print("\n👨‍🎓 STUDENT DATA")
        print("-" * 30)
        for student in self.students:
            print(student.display_info())
            print(student.study())
            print("-" * 20)

lecturer1 = Lecturer("Edy", 17, "123456", "Object Oriented Programming")
student1 = Student("Surya Ramdhani", 23, "24241144", "Teknologi Informasi")

university = UniversitySystem()
university.add_lecturer(lecturer1)
university.add_student(student1)

university.display_all_data()