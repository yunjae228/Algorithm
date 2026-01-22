series = int(input())
devil_number = 666
cnt = 0

while True:
    if '666' in str(devil_number):
        cnt += 1
    if cnt == series:
        break
    devil_number += 1

print(devil_number) 