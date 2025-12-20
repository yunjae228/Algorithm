s = input()
a = ""


for i in range(len(s)-1, -1 , -1):
    a += s[i]

if s == a :
    print(1)
else:
    print(0)