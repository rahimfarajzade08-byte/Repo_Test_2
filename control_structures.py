mark = int(input("What is your exam mark? "))

if mark > 89:
    print("A")
elif mark > 74:
    print("B")
elif mark>49:
    print("C")
else:
    print("F")

number = int(input("Input a number "))
for i in range(1,11):
    print(number,"x",i,"=",number*i)
password = "ilovecoding123"
attempt = 3
while attempt > 0:
    pass_2 = input("Enter your password: ")
    if pass_2 == password:
        print("You have logged in!")
        break
    attempt -= 1
    print("Your password is incorrect, try again!")
