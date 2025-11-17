import matplotlib.pyplot as plt
student_names=["Rahul","Sanjay","John","Andrew","Vaibhav"]
student_marks=[47,37,49,50,48]

mark_per=[]
for x in student_marks:
    per=(x/50)*100
    mark_per.append(per)
print(mark_per)

def line_chart():
    plt.plot(student_names,student_marks,marker="o",ms=20,mec="r")
    plt.title("Student Marks")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.show()
line_chart()

def bar_chart():
    plt.bar(student_names,student_marks)
    plt.title("Student Marks")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.show()
bar_chart()