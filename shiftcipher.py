#!/bin/python
import os  
#importing the os module to send commands to the underlying OS for use at the end of the code
def inputMode(): #defining a function to be used later inside another function
        mode = raw_input('Would you like to encrypt "e" or decrypt "d" a message? ') 
        # setting raw input to variable mode
        # offering the option to enter the first letter of the mode they want to uae for convenience
	if mode in 'encrypt e decrypt d'.split(): # storing the value entered in a list
            return mode # returning the set mode for the function inputMode    
	else:# if the entered string is not one of the 2 options displayed, this message and start the loop again 
            print('I am sorry, I did not understand. Please enter either "encrypt" or "decrypt"')
           
def inputMessage(): #defining a function to be used later inside another function
    message = raw_input('Enter your message, containing no numbers or symbols: ') 
    #asking for the message and setting it to a variable
    return message

def cipherMessage(mode, message): #using a modified version of my Caesar codes encryption/decryption process
    key = int(raw_input('Enter your first key: ')) # takes input for 3 encryption keys 
    key1 = int(raw_input('Enter your second key: ')) # sets the input as an int type as they will be
    key2 = int(raw_input('Enter your third key: ')) #used for arithmetic later in the code 
    if mode[0] == 'd': # if the 0th letter of inputted mode is d (as in an array the first letter is 0) 
        key = -key     # then inverse all of the keys for the decryption process
        key1 = -key1
        key2 = -key2
    translated = ''   # defining the variable so it can be used later
    for letter in message:
        if letter.isalpha():  
        # going through the characters in the message leaving out numbers and symbols, using a built in method
            num = ord(letter) 
            # ord returns the ascii value of each character in the message assigning it to the variable num 
            num += key # adds the first key to the ascii value of each letter
            if letter.isupper(): # if the letters are upper case then they have different ascii value to lower case
                if num > ord('Z'): #nested if statement, if the character has an ascii value larger than that of 'Z' 
                    num -= 26  # take 26 away from it to wrap round to the start of the capital letters
                elif num < ord('A'):  # if it is going to go before the ascii value of 'A'
                    num += 26   # add 26 to the value to wrap round to the end of the capital alphabet
            elif letter.islower():
                if num > ord('z'):    # same as above but for lower case letters 
                    num -= 26
                elif num < ord('a'):  #using elif (else if) to extend the if statement
                    num += 26
            num -= key1  # takes the second key away from the ord value of the first encryption stage
            if letter.isupper():  # repeats the code from above to wrap around the alphabet 
                if num > ord('Z'): # after the second key has been taken away from the ascii value
                    num -= 26  
                elif num < ord('A'):  
                    num += 26   
            elif letter.islower():
                if num > ord('z'):   
                    num -= 26
                elif num < ord('a'):  
                    num += 26        
            num += key2  #adds the third key to the ord value of the second encryption stage
            if letter.isupper(): # repeats the wrap around process for a third time to maintain
                if num > ord('Z'): # the encrypted code as letters. As translating to symbols
                    num -= 26  # is easy but translating symbols back to letters is hard 
                elif num < ord('A'):  
                    num += 26   
            elif letter.islower():
                if num > ord('z'):   
                    num -= 26
                elif num < ord('a'):  
                    num += 26 
            translated += chr(num)  
        #translates the 3 time encrypted ord value back to a letter to be added to the translated string
        else:
            translated += letter    # if there is a space, symbol or number then don't translate it 
    return translated        
mode = inputMode()   # calling the functions which have returned their values
message = inputMessage()
print "Your translated text is: " + (cipherMessage(mode, message))
# printing out the ciphermessage function with the arguments from the other 2 functions
# these 2 functions were set to message and mode a few lines above to be inputted into ciphermessage 
exit = raw_input('Would you like to play again? "yes"or "no" : ')  	
if exit == "yes":  # giving the user the chance to replay the code
	os.system('python encrypt.py')

