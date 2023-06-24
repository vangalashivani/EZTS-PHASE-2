student_grade=[]
student_grade.append((1, "shivani"))
student_grade.append((4, "shirisha"))
student_grade.sort(reverse=True)
print("yes")
print(student_grade)
student_grade.append((3, "sid"))
student_grade.sort(reverse=True)
student_grade.append((2,"sathwik"))
student_grade.sort(reverse=True)
print("priority wise sorted\n",student_grade)
print("original queue")
while student_grade:
    print(student_grade.pop())
