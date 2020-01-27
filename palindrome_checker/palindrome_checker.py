##This code asks for a user input of a word or sentence and then calls a fuctnion
##called palichecker to see if the input is a palindrome.

def palichecker (your_word,reverse_word):
    if your_word == reverse_word:
        print ("This word is a palindrome")
    else:
        print("This word is not a palindrome")


print("Let me tell you if a word or sentence is a palindrome")
your_word = input("Give me a word or sentence ")

your_word = str(your_word)
reverse_word =your_word[::-1]
palichecker (your_word,reverse_word)
