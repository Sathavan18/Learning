'''
def recursive_sum(n):
    if n == 0:
        return 0 # base case has to return same type as recursive function
    return n + recursive_sum(n - 1)

print(recursive_sum(5))

def recursive_length(text):
    if text == '':
        return 0
    return 1 + recursive_length(text[:-1])

print(recursive_length(text='Hello'))

def recursive_reverse(text):
    if text == '':
        return ''
    return recursive_reverse(text[1:]) + text[0]

def recursive_reverse_optimal(text, index):
    if index < 0:
        return ""

    return text[index] + recursive_reverse_optimal(text, index - 1)
text = "hello"
print(recursive_reverse_optimal(text, len(text) - 1))

def power(x, n):
    if n == 0:
        return 1
    return x * power(x,n-1)

print(power(2,5))
print(power(2,3))
print(power(5,3))

def power_optimised(x,n):
    if n == 0:
        return 1
    half = power_optimised(x,n//2)
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half
'''
