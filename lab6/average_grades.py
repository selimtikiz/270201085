grade_lst=[]
number_of_students=int(input("enter the number of students"))
i = 0
while i < number_of_students:
    print("Student :",str(i+1))
    mid_1 = int(input("midterm1"))
    mid_2 = int(input("midterm2"))
    final = int(input("final"))
    i += 1
    grade_lst.append([mid_1,mid_2,final])
print(grade_lst)
average_grade_lst = []
for sub_grades in grade_lst:
    average_grade_lst.append(sub_grades[0]*0.3+sub_grades[1]*0.3+sub_grades[2]*0.4)
print(average_grade_lst)