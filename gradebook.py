class Student:
	def __init__(self, name, score):
		self.name = name
		self.score = score

class Gradebook:
	def __init__(self):
		self.students = []

	def add_student(self, student):
		self.students.append(student)

	def get_average(self):
		if not self.students:
			return 0.0

		average = 0
		for student in self.students:
			average += student.score

		return average / len(self.students)

#testing my code

Class7 = Gradebook()
#lets add students now

Class7.add_student(Student("Isihaka" , 90 ))
Class7.add_student(Student("Japhary", 80))
Class7.add_student(Student("Silima", 70))

print(" Class 7 average is:", Class7.get_average())

Class6 = Gradebook()

Class6.add_student(Student("Collins" ,80))
Class6.add_student(Student("Landry", 90))
Class6.add_student(Student("Mwita", 80))

print (f" Class 6 average is: {Class6.get_average():.2f}")

Class5 = Gradebook()

print(f" Class 5 average is :{Class5.get_average():.2f}")
