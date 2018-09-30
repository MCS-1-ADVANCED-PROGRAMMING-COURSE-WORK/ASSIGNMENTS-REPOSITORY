'''
A simple example of creating and using objects in Python.

TUSUBIRA DAVID  2018/HD05/1981U  1800740165
ALLAN MURUNGI   2018/HD05/1970U 
DANIEL ANGOLE   2018/HD05/1947U  1800737067
EUNICE NANZIRI  2017/HD05/1714U  207014800

'''

class Student:
    
    no_of_students = 0
    
    def __init__(self,firstname,lastname,regno,grade_av,reg_year):    #Added "grade_av" and "reg_year" among the arguments of the constructor method
        self.firstname = firstname
        self.lastname = lastname
        self.regno = regno
        self.grade_average = grade_av                                 #Created the grade_average field to store student's grade average
        self.reg_year = reg_year                                      #reg_year field added
        self.no_of_students = no_of_students + 1

    def setgrade(self, grade):                                        #setgrade method for changing the grade average value
        self.grade_average = grade

    def tostring(self):                                               #tostring method adjusted to include the grade average
        description = self.lastname + ', ' + self.firstname + '. \tRegistration number ' + self.regno + '\tGrade Average ' + self.grade_average + 't\Reg_year ' + self.reg_year
        return description

    

class Course:
    def __init__(self,coursetitle):
        self.coursetitle = coursetitle
        self.students = []
        self.lecturers = []

    def addstudent(self,newstudent):
        self.students.append(newstudent)

    def addlecturer(self,newlecturer):                                                   #Add lecturer method added to Course class
        self.lecturers.append(newlecturer)
    
    def tostring(self):                                        
        str = self.coursetitle + '\n'
        str = str + 'Students enrolled:\n'
        for s in self.students:
            str = str + s.tostring() + '\n'
        return str

class MasterStudent(student):                                                            #MasterStudent class inheriting the student class

    def __init__(self,firstname,lastname,regno,grade_av,reg_year,status):
        student.__init__(self,firstname,lastname,regno,grade_av,reg_year)
        self.status = status

    def tostring(self):                                                                  #overriding tostring method with status added
        description = self.lastname + ', ' + self.firstname + '. \tRegistration number ' + self.regno + '\tGrade Average ' + self.grade_average + 't\Reg_year ' + self.reg_year + '\tStatus ' + self.status
        return description

class Lecturer:                                                                          #Lecturer class created
    def __init__(self,first_name,last_name,lecturer_id):
        self.firstname = firstname
        self.lastname = lastname
        self.lecturer_id = lecturer_id

    
   
student1 = Student('Jimi','Hendrix','123456')
student2 = Student('Frank','Zappa','234567')
student3 = Student('Ringo','Starr','345678')

course1 = Course('MSc Computer Science')
course1.addstudent(student1)
course1.addstudent(student2)
course1.addstudent(student3)

print('Name of first student is ' + student1.firstname)

print(course1.tostring())
