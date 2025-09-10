score = int(input())
grade = ''

if score >= 90 :
    grade = "A"
elif ( 80 <= score ) and ( score < 90 ):
    grade = "B"
elif ( 70 <= score ) and ( score < 80):
    grade = "C"
elif ( 60 <= score ) and ( score < 70):
    grade = "D"
else:
    grade = "F"

print(grade)


