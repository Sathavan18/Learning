'''
# split() splits a string into a set of words in a list
sentence = 'I am happy'
print(sentence.split())

# join() adds wahtever you want to join between the characters
# could also add between items in tuple
sentence = 'I am happy'
print(' '.join(sentence))

# replace() replaces a specified object with another
sentence = 'I like cats'
print(sentence.replace('cats', 'dogs'))

# strip() removes an leading and trailing whitespaces
sentence = '      Hello      '
print(sentence.strip())

# lower() makes everything lowercase
sentence = 'THIS WILL REMAIN UPPERCASE'
print(sentence.lower())
# upper() makes everything uppercase
print(sentence.upper())

# startswith() checks whether string starts with specified value
# return True if true
sentence = 'THIS WILL REMAIN UPPERCASE'
print(sentence.startswith('THIS'))
print(sentence.startswith('THAT'))

# endswith() checks whether string ends with specified value
sentence = 'THIS WILL REMAIN UPPERCASE'
print(sentence.endswith('UPPERCASE'))
print(sentence.endswith('LOWERCASE'))

# isalnum() checks whether a string is alphanumeric
'''