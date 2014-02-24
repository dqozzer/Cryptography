#!/bin/python
import collections
#importing a library to count the frequency of letters
var = raw_input('Please enter your ciphered text to be analysed in lower case: ')
# asking for the ciphertext to be analysed using raw input and storing it in a variable 

var2 = list(var) # creating a list of the string so it can analyse each character individually
belly = []  # initialising a list for the values of the for loop occurring more than 5 times in

for letter in var2:   # for loop goes through every character in the list of the inputted string
    if letter.isalpha():  # if statement to ignore spaces and only analyse letters
        var3 = var2.count(letter) # counting the number of times each letter appears
        if var3 > 5:   # if there are more than 5 of a letter in the inputted string of text then
            belly.append(letter) # append (add) the character to the list belly the amount of times it appears
             
counts = collections.Counter(belly) 
mostcommon = counts.most_common()
# using an imported library to count through the list belly and return the most common letters
# as well as how many times it appears
print ""
print mostcommon  #this prints the most common dictionary from the variable created above
print ""
print "Above, each bracket contains a commonly used letter (left side) and the amount of times they are used (right number)"
print "" #prompt explaining what is displayed
# asking for the letters printed above to further analyse
answerone = raw_input('Enter the letter in the first bracket: ')  
answertwo = raw_input('Enter the letter in the second bracket: ')
answerthree = raw_input('Enter the letter in the third bracket: ')
hello = ord(answerone)  # converting the inputted letters to their ascii value 
hellotwo = ord(answertwo)  # so that they can be taken away from the ascii values of 
hellothree = ord(answerthree) #the most frequent letters in the english alphabet leaving a shift value
print ""
print ""    # printing the values analysed followed by the three most common letters in the english language
print answerone + " is the most common letter used in your ciphertext"
print ""
print answertwo + " is the second most common letter used in your cipher text"
print ""
print answerthree + " is the third most common letter used in your cipher text"
print ""
print ""
print "The most common letters in the English alphabet are as follows: "
print "1) e"
print "2) a"
print "3) o"
print ""

# working out each possible values of a key used using the analysed letters and the three most common 
# in the English language by calculating the difference between ascii values of common letters 
# from the ciphertext and the three most common in the English language
key1 = ord('e') - hello    

key2 = ord('e') - hellotwo

key3 = ord('e') - hellothree

key4 = ord('a') - hello

key5 = ord('a') - hellotwo

key6 = ord('a') - hellothree

key7 = ord ('o') - hello

key8 = ord('o') - hellotwo

key9 = ord('o') - hellothree

# making sure that the key doesn't go outside above or below 26 by wrapping it around
# if a key is less than 1 then add 26 to loop it round to the opposite end of the alphabet
#if the key is larger than 26 then take 26 away from it to wrap it round to 
#the beginning of the alphabet, Tried using a for loop but it altered the keys incorrectly
if key1 < 1:
    key1 += 26
elif key1 > 26 :
    key1 -= 26
if key2 < 1:
    key2 += 26
elif key2 > 26 :
    key2 -= 26    
if key3 < 1:
    key3 += 26
elif key3 > 26 :
    key3 -= 26    
if key4 < 1:
    key4 += 26
elif key4 > 26 :
    key4 -= 26
if key5 < 1:
    key5 += 26
elif key5 > 26 :
    key5 -= 26
if key6 < 1:
    key6 += 26
elif key6 > 26 :
    key6 -= 26
if key7 < 1:
    key7 += 26
elif key7 > 26 :
    key7 -= 26
if key8 < 1:
    key8 += 26
elif key8 > 26 :
    key8 -= 26
if key9 < 1:
    key9 += 26
elif key9 > 26 :
    key9 -= 26

key10 = 26 - key1   # taking each key away from 26, as when shifting the alphabet in the encryption process
					# it gives a key different to the one when you take the difference of the ord values
key11 = 26 - key2   # to get it to suggest the correct keys you need to take the key values suggested by this
					# code away from 26 this will then give you the likely keys used to encrypt
key12 = 26 - key3

key13 = 26 - key4

key14 = 26 - key5

key15 = 26 - key6

key16 = 26 - key7

key17 = 26 - key8

key18 = 26 - key9


print "" 
print "Below shows the key thought to have been used to encrypt the message, followed by the decrypted message using said key"
print ""
print ""  #printing a prompt as to what is being printed below

keys = [key10,key11,key12,key13,key14,key15,key16,key17,key18]   


def cipherMessage(var, key):  #this is the same code as used in my Caesar cipher for brute force mode but slightly altered
    translated = ''   # defining the variable so it can be used later
    for letter in var:
        if letter.isalpha():  
        # going through the characters in the message leaving out numbers and symbols, using a built in method
            num = ord(letter) # ord returns the ascii value of each character in the message assigning it to the variable num 
            num -= key # adds the key to the ascii value of each letter
            if letter.isupper(): # if the letters are upper case then they have different ascii value to lower case
                if num > ord('Z'): #nested if statement, if the character has an ascii value larger than that of Z 
                    num -= 26  # take 26 away from it to wrap round to the start of the capital letters
                elif num < ord('A'):  # if it is going to go before the ascii value of A
                    num += 26   # add 26 to the value to wrap round to the end of the capital alphabet
            elif letter.islower():
                if num > ord('z'):    # same as above but for lower case letters 
                    num -= 26
                elif num < ord('a'):  #using elif (else if) to extend the if statement
                    num += 26
            translated += chr(num)
        else:
            translated += letter    # if there is a space, symbol or number then don't translate it 
    return translated

for key in keys:   
# runs a for loop taking key to be each value in the list 'keys' which contains the suggested keys earlier calculated by the code
# it inserts them all into the ciphermessage function 
		print ""									
		print(key, cipherMessage(var, key)) 
	# prints function cipher message using the parameters var and key of which key changes in the for loop







    

    
