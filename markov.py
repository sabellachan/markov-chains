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
     


def make_chains(text_string):
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

    for i in range(len(words) - 2):
        
        first_word = words[i]
        second_word = words[i+1]
        key = (first_word, second_word)
        if chains.get(key) == None :
            value = []
            chains[key] = value
            value.append(words[i + 2])
        else:
            list_value = chains[key] 
            list_value.append(words[i + 2])
    return chains
 


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    key = choice(chains.keys())

    while True:
        try:
            word = chains[key]
            random_word = choice(word)
            text += " " + random_word
            key = (key[1],random_word)

        except KeyError:
            break

    print text




input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

# print random_text
