students = [
    ("Charlie", 91),
    ("Alice", 85),
    ("Bob", 72)
]
students.sort(key=lambda student: student[1])
# lambda student: student[1]
means: For each student, return the second element
can do this also:
def get_score(student):
    return student[1]
students.sort(key=get_score)

e.g.
words = ["banana", "kiwi", "apple", "pear"]
words.sort(key=lambda word: len(word))
print(words)
it will extract the length of each word, in ascending order. so the sorted array would be kiwi pear apple banana. Python uses stabel sort so kiwi is always before pear as they remain in the same order if the value is the same.