"""Bora Eskicioğlu-Global AI HUB- ODEV 3"""

students= {"names": [(input("Name of the first student")), (input("Name of the second student")),
                     (input("Name of the third student")),(input("Name of the fourth student")),
                     (input("Name of the fifth student")),],

           "midterms": [(input("Midterm grade of the first student")), (input("Midterm grade of the second student")),
                     (input("Midterm grade of the third student")),(input("Midterm grade of the fourth student")),
                     (input("Midterm grade of the fifth student")),],

           "projects": [(input("Project grade of the first student")), (input("Project grade of the second student")),
                     (input("Project grade of the third student")),(input("Project grade of the fourth student")),
                     (input("Project grade of the fifth student")),],

           "finals": [(input("Final grade of the first student")), (input("Final grade of the second student")),
                     (input("Final grade of the third student")),(input("Final grade of the fourth student")),
                     (input("Final grade of the fifth student")),]
           }

average=[1,2,3,4,5]
student=["","","","",""]
tmp=0
tmp1=""
for i in range(5):
    average[i]=(int(students["midterms"][i])*0.3)+(int(students["projects"][i])*0.3)+(int(students["finals"][i])*0.4)
    student[i]=students["names"][i]

for i in range(5):
    for j in range(5):
        if average[i]<=average[j]:
            continue
        else:
            tmp=average[i]
            average[i]=average[j]
            average[j]=tmp
            tmp1 = student[i]
            student[i] = student[j]
            student[j] = tmp1
print(average)
print("Student",student[0],"has highest grade in the class with grade",average[0],"\n")
print("Student",student[4],"has lowest grade in the class with grade",average[4],"\n")