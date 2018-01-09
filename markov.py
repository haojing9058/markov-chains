"""Generate Markov text from text files."""

from random import choice

import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_data = open(file_path)
    text_data = text_data.read()
    # print text_data
    return text_data


def make_chains(input_text):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    contents = open_and_read_file(sys.argv[1])

    chains = {}

    words = contents.split()

    for i in range(len(words) - 2):
        a = words[i]
        # print "A equals: ",a
        b = words[i + 1]
        # print "B equals: ",b
        pair = (a, b,)
        # chains[pair] = []
        if chains.get(pair, False):
            c = words[i + 2]
            chains[pair].append(c)
            # how can we have an empty list as a value and not reset?
        else:
            c = words[i + 2]
            chains[pair] = []
            chains[pair].append(c)

        # print "C equals: ", c
        # chains[pair].append(c)
        # else add "" to dictionary

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # what word should we start on? "Would you"?
    # dicitonaries are unordered, so what does "first key" mean?
    # from which list you should pull out the random word?

    # key 1st word (a)
    # key 2nd word (b)
    # random word from value ([list]) (c)
    # value of b, c tuple

    key_selection = choice(chains.keys())



    first_word = key_selection[0]
    second_word = key_selection[1]

    third_word = choice(chains[(first_word, second_word,)])
    # print first_word,second_word,third_word




    # random.choice(chains)

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string

input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text