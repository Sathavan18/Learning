try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("That is not a valid number")

idea:
try
 ↓
Run code that might cause an error
 ↓
Error occurs?
 ├── No  → continue normally
 └── Yes → run matching except block

 Example:
 def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Cannot divide by zero'

In a try catch block, finally always runs at the end.
def get_list_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return 'Index out of range'