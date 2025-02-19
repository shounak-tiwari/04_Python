# a student who is not a student of java 

group_python_students = {"Nehal","Priyal","Vaishali","Sapna","Sangeeta" ,"Aniket","Ashwin"}
group_java_students =  {"Aniket","Ashwin","Lakhan","Vishal","Nehal","Rishi"}


x = group_python_students-group_java_students
print(x)


# java exist but not python 

# y = group_java_students-group_python_students
y = group_java_students.difference(group_python_students)
print(y)