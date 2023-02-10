# Xtics of a string
#        order - sequential
#        immutable
#        heterogenous
#        allows duplication
#        allows to extract subset of a string using index
#        

# s= "fisgosgvuosgvuog"
# print the reverse
# print(s[ :: -1])


# input() - input string value
# print() - output string value
# split() - split string according to delimitors
# strip() - remove space beginning & end
# join() - joins all elements into one string
# lower()
# upper()
# title() - convert string to title case
# replace() - replace old string with new
# len() - no. of characters in a string


# write a program to read some text then test whether its a palindrome

# write a program to prompt the user to enter some string then calculate and display the number of words in that string
text = input("enter some text:  ")
text1 = text.strip()

space = 1
for i in range(len(text1)):
    if text1[i] in [" "]:
        space = space + 1
    else: pass

print("string has",space, "words")

# write a program to prompt the user to enter some strings then calculate and display the no. of vowel and consonants in the strings

string = input("enter some text:  ")
string = string.strip()

vowel = 0
conso = 0
for i in range(len(string)):
    if string[i] in ['a', 'e', 'i', 'o', 'u']:
        vowel = vowel +1
    elif string[i] not in [" "]:
        conso += 1
    else: pass    


print("There are ",vowel, "vowels")
print("There are ",conso, "consonants")

# write a program to prompt user to enter a string, assuming the string has many word, the program should prompt the user to search a word if the word iko it should display it
words = input("enter some texts: ")
words = words.split()

searchWord = input("Enter word to search : ")
if searchWord in words:
    print(f"{searchWord} has been found")
else: print(f"{searchWord} not found")    
