"r" → read
"w" → write (overwrites existing content)
"a" → append (adds to existing content)

with open("example.txt", "r") as file:
    content = file.read()
with automatically closes the file when you're finished

with open("notes.txt","a") as file:
    file.write("Python practice")