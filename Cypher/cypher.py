# The first kind of cipher you are going to build is called a Caesar cipher. 
# Specifically, you will take each letter in your message, 
# find its position in the alphabet, 
# take the letter located after 3 positions in the alphabet, 
# and replace the original letter with the new letter.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
    new_char = alphabet[new_index]
    print(new_char)

