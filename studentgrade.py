
import sys


if len(sys.argv) == 6:
    script_name = sys.argv[0]
    m1 = float(sys.argv[1])
    m2 = float(sys.argv[2])
    m3 = float(sys.argv[3])
    m4 = float(sys.argv[4])
    m5 = float(sys.argv[5])
    print("User provided input marks:")
else:
    script_name = sys.argv[0]
    
    m1 = 75
    m2 = 80
    m3 = 70
    m4 = 85
    m5 = 90
    print("No input given — using default marks:")


average = (m1 + m2 + m3 + m4 + m5) / 5


if average >= 85:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 55:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"


print("Script Name:", script_name)
print("Marks:", m1, m2, m3, m4, m5)
print("Average Marks:", average)
print("Grade:", grade)
