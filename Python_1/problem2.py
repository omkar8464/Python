#1.WAP  to check if a number is positive.
'''num=int(input("Enter the number:"))
if num>=0:
    print("Positive")
else:
    print("Negative")
#2.WAP to check whether a number is odd or even.
num=int(input("Enter the number:"))
if num%2==0:
    print("even")
else:
    print("odd")


#3.WAP to create area calculator.
print("******AREA CALCULATOR******")
print("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 3 to get the area of triangle""")
choice=int(input("Enter a number between 1-4:"))
if choice == 1:
    side=float(input("Enter the length of one side:"))
    area=side**2
    print("The area of square is ",area)
elif choice==2:
    length=float(input("Enter the length of the rectangle:"))
    width=float(input("Enter the width of the rectangle:"))
    area=length*width
    print("The area of rectangle is ",area)
elif choice==3:
    radius=float(input("Enter the radius of the circle: "))
    area=3.14*(radius**2)
    print("The area of the circle is",area)
elif choice==4:
    base=float(input("Enter the base of yhe triangle"))
    height=float(input("Enter the heigth of the triangle:"))
    area=0.5*base*height
    print("The area of the triangle is ",area)
else:
    print("invalid")


#4.WAP to check wheter the passed letter is a vowel or not
letter=input("Enter a letter here: ")
if (letter in "aeiou") or (letter in "AEIOU):
    print("it is a vowel")
else:
    print("Not vowel")

'''
#5.WAP to check if a number is single digit number ,2 digit number and so on.., up to 5 digits
num=int(input("Enter a number up to 5 digits:"))
if num>=0 and num<=9:
    print("It is a single digit number")
elif num>=10 and num<=99:
    print("It is a double digit number")
elif num>=100 and num<=999:
    print("It a three digit number")
elif num>=1000 and num<=9999:
    print("It is a four digit number")
elif num>=10000 and num<=99999:
    print("It is five digit number")
else:
    print("Invalid")