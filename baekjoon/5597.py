import sys

whole_student = [int(i) for i in range(1,31)]

for i in range(28):
    whole_student.remove(int(sys.stdin.readline()))

whole_student.sort()
print(whole_student[0])
print(whole_student[1])