# Create a tuple with name courses and initialize it with JAVA, PHP, C#, Android. Insert two items HTML and Python at the 3rd position in tuple.


courses = ("JAVA", "PHP", "C#", "Android")

print("Original Tuple: ", courses)

temp = list(courses)

temp.insert(2, "HTML")
temp.insert(3, "Python")

courses = tuple(temp)

print("Updated Tuple: ", courses)