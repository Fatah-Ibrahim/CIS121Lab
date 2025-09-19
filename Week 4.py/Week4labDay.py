
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
    

user_word = input("Enter a word: ")

for letter in range (1,len(user_word),2):
    print(user_word[letter])