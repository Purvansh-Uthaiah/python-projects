n = int(input("Enter the number of subjects: "))
i = 0
total_marks = []
for i in range(1, n + 1):
    sub_name = input(f"Enter subject {i} name: ")
    sub_marks = int(input(f"Enter your marks in {sub_name} : "))
    total_marks.append(sub_marks)
    percent = sum(total_marks)/n
if (percent >= 90 and percent < 100):
        print(f"Grade A")
elif(percent >= 75 and percent < 90):
        print("Grade B")
elif(percent >= 60 and percent < 75):
        print("Grade C" )
elif(percent >= 50 and percent < 60):
        print("Grade D")
else:
        print("Grade F - Better luck next time! ")




print(total_marks)
print(f"Total score {sum(total_marks)}")
print(f"Congrajulations, you have scored {percent}% in the exam")


