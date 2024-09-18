import random
import string

# this is simple text generator that allows you to nominate a string length and then generates a random string of that length
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

get_random_string(35)
#get_random_string(6)
#get_random_string(4)