from random import choice
import sys


def open_and_read_file(argv):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_file = open(sys.argv[1])
    str_file = text_file.read()

    text_file.close()

    return str_file
     


def make_chains(text_string, argv):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split()
    chains = {}

    length = int(argv[2])

    
    for i in range(len(words) - length-1):
        key = []
        for x in range(length):
            word = words[i+x]
            key.append(word)
            #i +=1
        # first_word = words[i]
        # second_word = words[i+1]
        # key = (first_word, second_word)
        
        key = tuple(key)

        if chains.get(key) == None:
            value = []
            chains[key] = value
            value.append(words[i + length])
        else:
            list_value = chains[key]
            list_value.append(words[i + length])
    return chains
 


def make_text(chains, argv):
    """Takes dictionary of markov chains; returns random text."""
    length = int(argv[2])
    text = ""
    key = choice(chains.keys())

    while True:
        try:
            word = chains[key]
            random_word = choice(word)
            text += " " + random_word
            key_list = [key[x] for x in range(1,length)]
            key_list.append(random_word)
            key = tuple(key_list)
        except KeyError:
            break

    print text




input_path = "gettysburg.txt"

key_size = sys.argv
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, key_size)

# # Produce random text
random_text = make_text(chains, key_size)

# print random_text
