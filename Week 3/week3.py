#question 3
'''
light_color = input("Enter a light color: ").lower()

if light_color == "green":
    print("Go")
elif light_color == "yellow":
    print("Yeild")
elif light_color == "red":
    print("Stop")
else:
    print("Invalid Color")
'''
#Write a program that prompts the user to enter three integers and displays the integers in increasing
# order (smallest to largest). You may not use the built-in functions max (), min(), sort() or sorted ()

num1 = int(input("Enter a number?: "))
num2 = int(input("Enter another number?: "))
num3 = int(input("Enter a final number?: "))

'''
if num1 <= num2 <= num3:
    print (num1, num2, num3)
'''

#Question 7 

Knuts = int(input("Enter the number of Kunts: "))
# 1 Sickle == 29 kunts
Sickle = int(Knuts / 29)
Kunts = Knuts - (sickle * 29)
 
 if number of sickle > 17: 