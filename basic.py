a  = int(input("Enter a number: "))
b = int(input("Enter second number: "))
c = a + b
print("The sum of", a, "and", b, "is:", c) 

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
# print("The average of", n1, "and", n2, "is:", (n1+n2)/2)
print(n1>=n2)

name = str(input("Enter your name: "))
print("Hello", name, "!")
print(name,"Your name has", len(name), "characters.")

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")   
print("grade of student is:", )

frist  = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third  = int(input("Enter third number: "))
if frist > second and frist > third:
    print("The largest number is the first:", frist)
elif second > frist and second > third:
    print("The largest number is the second:", second)
else:
    print("The largest number is the third:", third)



