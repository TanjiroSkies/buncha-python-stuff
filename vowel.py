#This defines what the function "Chech_Vow" will do

def Check_Vow(string, vowels):

#"Casefold" is basically a funtion to make it so that it doesnt matter if the string is typed either lower or uppercase

    string = string.casefold()

    count = {}.fromkeys(vowels, 0)


    for character in string:

        if character in count:

            count[character] += 1   

    return count

#runner code, which will actually do the stuff, with "vowels" defining what a vowel is

vowels = 'aeiou'

#"string" defines what word/sentence you want to bissect

string = input("Tell me a word and ill tell you how many vowels there are, i can even do full sentences! ") 

#and here the numbers are printed to the terminal, with "Check_Vow" being called from the top part of the code

print (Check_Vow(string, vowels))


