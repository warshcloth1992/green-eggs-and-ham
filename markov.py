"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    
    filename = open(file_path).read() 
    #assigning var to opened txt file and returning a string
    return(filename)
    #returning the string
    #print(filename)


#open_and_read_file("green-eggs.txt")


def make_chains(text_string):
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

    chains = {}
    #make dictionary for tuple and list
    filename = open_and_read_file("green-eggs.txt")
    #assign var to open txt file and returning a string
    words = filename.split()
    #asssign a var to list and split string at all blank space
    for word in range(len(words)-2):
        #creating a loop to iterate through the range through the length of words up until the last two words.

        key = (words[word], words[word + 1])
        #assigning the var key to the first two words in list
        val = words[word+2]
        #assigning the val to the third word in list
        # print(key)
        # print(val)
        if key not in chains: 
            #if the first two words(key) not in the dictionary
            chains[key] = []
            # added it to chains 
        chains[key].append(val)
        #added the content in val to the key in chains to complete the dictionary 
        #with both {key: val}

    return chains
    #print(chains)


    #put key and val into chains
    """by signing key and val to chains somehow: chains = {key: val} this should give us a dictionary"""
       
    #return chains


#ake_chains()


def make_text(chains):
    """Return text from chains."""

    words = []
    

    # your code goes here
    
    chains = make_chains("green-eggs.txt")
    #calling the dictionary we made in make_chains and assigning it to the var
    
    item = choice(list(chains.keys()))
    #iterate through the dictionary. Make that a list. randomly choosing an item
    
    key = [item[0], item[1]]
    #assigning the first two items to key
    value = choice(chains[item])
    #assigning a random item at index 2 of chains to value
    #print(key)

    #print(value)
    # while value != None:
    while True:
        #words.append(key)
        words.append(value)
        key = (key[1], value)
        if chains.get(key, None):
            value = choice(chains[key])
        else:
            break
            # value = None
    
    #print(words)    
    #print()
    # Keep looping until we reach a value of None
    # (which would mean it was the end of our original text)
    # Note that for long texts (like a full book), this might mean
    # it would run for a very long time.

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file("green-eggs.txt")

# Get a Markov chain
chains = make_chains("green-eggs.txt")

# Produce random text
random_text = make_text(chains)

print(random_text)
