import string
'''
# Return largest without using max()
def return_largest(a):
    largest = 0
    for i in range(len(a)):
        if a[i] >= largest:
            largest = a[i]
    return largest

a = [0,1,2,3,4,5]
print(return_largest(a))

# Reverse a string
def reverse_string(a):
    string_reversed = ''
    for i in range(len(a)-1,-1,-1):
        string_reversed += a[i]
    return string_reversed

a = 'Hello'
print( reverse_string(a))

# Count vowels in a sentence
def count_vowels(a):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for i in range(len(a)):
        for j in range(len(vowels)):
            if a[i] == vowels[j]:
                count += 1
    return count
a = 'Hello, my name is Sathavan'
print(count_vowels(a))

# Fizzbuzz
def fizzbuzz(a):
    answer = []
    for i in range (a):
        if i != 0:
            if i%3 == 0 and i%5 == 0:
                answer.append("FizzBuzz")
            elif i%3 == 0:
                answer.append("Fizz")
            elif i%5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
    return answer
a = 15
print(fizzbuzz(a))

# Palindrome
def palindrome_check(a):
    new_a = a.lower()
    b = ''
    for i in range(len(a)-1,-1,-1):
        b += new_a[i]
    if b == new_a:
        return True
    else:
        return False
a = 'Racecar'
b = 'Hello'
print(palindrome_check(a))
print(palindrome_check(b))

# Return frequency of every word
def word_frequency(a):
    a_list = a.split()
    frequency = {}
    for i in range(len(a_list)):
        if a_list[i] not in frequency:
            frequency[a_list[i]] = 1
        else:
            frequency[a_list[i]] += 1 
    return frequency

a = 'My name is My name'
print(word_frequency(a))
'''