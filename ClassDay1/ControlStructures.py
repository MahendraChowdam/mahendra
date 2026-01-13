num = 4
if num%2 ==0:
    print("Even")
else:
    print("Odd")

marks =80

if marks>=90:
    print("GRADE A")
elif marks>=80:
    print("GRADE B")
else:
    print("GRADE C")

for i in range(1,11):
    print(i)

j = 1
while j<=10:
    print(j)
    j=j+1
    if j==5:
        break

day = 2
match day :
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
