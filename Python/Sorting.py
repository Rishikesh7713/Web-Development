import numpy as np
data_type=[("name","S"),("class","int"),("height","float")]
student_details=[("James",14,123.4),("Bob",13,125.77),("Fog",16,143.7)]
student=np.array(student_details,data_type)
print("Original Order")
print(student)
print("Sorted by Height")
print(np.sort(student,order="height"))