# FIFO
from collections import deque
'''
queue = deque()
queue.append("Alice")  # Add to the back
queue.popleft()        # Remove from the front
queue[0]               # Peek at the front

customers = deque()

def join_queue(name):
    customers.append(name)

def serve_customer():
    if not customers: 
        return None
    else:
        front = customers.popleft()
    return front

documents = deque(["report.pdf", "cv.pdf", "invoice.pdf"])

def add_document(document):
    documents.append(document)

def print_next():
    if not documents:
        return None
    else:
        front = documents.popleft()
        return front

print(print_next())
print(print_next())
print(print_next())
print(print_next())

class RecentCounter:

    def __init__(self):
        # initialise your queue
        self.queue = deque()
    def ping(self, t):
        # add the new ping
        self.queue.append(t)
        # remove pings that are too old
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        # return number of valid pings
        return len(self.queue)

students = deque([1, 1, 0, 0])
sandwiches = [0, 1, 0, 1]
def count_students(students, sandwiches):
    counter = 0
    while students:
        if counter == len(students):
            return len(students)

        if students[0] == sandwiches[0]:
            students.popleft()
            sandwiches.pop(0)
            counter = 0
        else:
            student = students.popleft()
            students.append(student)
            counter += 1
    return 0

print(count_students(students,sandwiches))
'''
def first_unique_stream(stream):
    frequency = {}
    queue = deque()
    results = []
    for character in stream:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1
            queue.append(character)
        while queue and frequency[queue[0]] > 1:
            queue.popleft()
        if queue:
            results.append(queue[0])
        else:
            results.append(None)
    return results
stream = "aabbec"
print(first_unique_stream(stream))