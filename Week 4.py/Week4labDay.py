#Question 1
'''
larger_num = int(input("Pick a number: "))
smaller_num = int(input("Pick a number: "))

counter = 0
# larger number until the number is smaller than numbber 

while True:
    if larger_num/2 > smaller_num:
        larger_num /= 2
        counter += 1 
    else:
        break
print(counter)    
'''
#Question 2  
'''
user_word = input("Enter a word: ")

for letter in range (1,len(user_word),2):
    print(user_word[letter])
'''
# question 3 
'''
for number in range (37,1050):
    if number % 2 == 0:
        print(number)
'''
#Question 4

word = ""
user_letter = ""

while user_letter != 'done':
    user_letter = input("Enter a letter (or type done): ")
    if user_letter  != "done":
        word += user_letter
print(word)
   