def replaceVowels(text, char):
    #i see they are telling the terminal to keep an eye out for vowels (is y a vowel? we'll never know)
    vowels = ['a','e','i','o','u']

    newText = ''

    for i in range(0, len(text)):
        #If the letter is a vowel , then we add the char (your chosen symbol) to our newText string.
        if text[i] in vowels:

            newText += char
        #aaand this is what happens if it is a consonant
        else:

            newText += text[i]

    return newText

text = input("Give me a sentence! ")

char = input("Give me a symbol! ")

 
#ok i understand what this is. it replaces all vowels with a symbol of your choice
print(replaceVowels(text, char))