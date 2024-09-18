#this has been taken from https://lorem-text.readthedocs.io/en/latest/readme/#features
# comment out the options you don't want to execute for any given output run

from lorem_text import lorem

# For randomly generated sentence of lorem ipsum text where the first word is capitalized, and the sentence ends in either a period or question mark:
print(lorem.sentence())

# Generate multiple paragraphs of lorem ipsum text each paragraph’s consists of 2 to 4 sentences:
paragraph_length = 5
print(lorem.paragraphs(paragraph_length))

# Generate random lorem ipsum words seperated with single space:
words = 10
print(lorem.words(words))