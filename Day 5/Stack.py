'''
def reverse_string(word):
    character_stack = []
    reversed_word = ''
    for character in word:
        character_stack.append(character)
    while character_stack != []:
        reversed_word += character_stack.pop()
    return reversed_word

word = 'Hello'
print(reverse_string(word))

current_page = "google.com"
history = []

def visit(new_page):
    global current_page
    # save current_page to history
    history.append(current_page)
    # change current_page to new_page
    current_page = new_page

def go_back():
    global current_page
    # check there is some history
    if history != []:
        # pop the most recent page and make it current_page
        current_page = history.pop()

print(current_page)  # google.com

visit("youtube.com")
visit("github.com")

print(current_page)  # github.com
print(history)       # ["google.com", "youtube.com"]

go_back()

print(current_page)  # youtube.com
print(history)       # ["google.com"]

def remove_duplicates(s):
    track_stack = []
    for character in s:
        if track_stack == []:
            track_stack.append(character)
        elif character != track_stack[-1]:
            track_stack.append(character)
        else:
            if track_stack[-1] == character:
                track_stack.pop()
    return ''.join(track_stack)

s = 'azxxzya'
print(remove_duplicates(s))

def backspace_compare(s, t):
    s_stack = []
    t_stack = []
    for character in s:
        if character != '#':
            s_stack.append(character)
        else:
            if s_stack != []:
                s_stack.pop()
    for character in t:
        if character != '#':
            t_stack.append(character)
        else:
            if t_stack != []:
                t_stack.pop()
    string_s = ''.join(s_stack)
    string_t = ''.join(t_stack)
    return string_s == string_t

s = "a#c"
t = "b"
u = "a#c"
v = "c"
print(backspace_compare(s,t))
print(backspace_compare(u,v))
'''
def cal_points(operations):
    points_stack = []
    final_score = 0
    for i in operations:
        if i == "C":
            if points_stack != []:
                points_stack.pop()
        elif i == "D":
            if points_stack != []:
                points_stack.append(points_stack[-1]*2)
        elif i == "+":
            if len(points_stack) >= 2:
                points_stack.append(points_stack[-1] + points_stack[-2])
                
        else:
            points_stack.append(int(i))
    for score in points_stack:
        final_score += int(score)
    return final_score

operations = ["5", "2", "C", "D", "+"]
print(cal_points(operations))