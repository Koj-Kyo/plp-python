# Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file.

with open("input.txt", "w") as f:
    f.write("This is the first line.\n")
    f.write("Here is the second line of text.\n")
    f.write("The third line is also here.\n")
    f.write("Fourth lines are fun to write.\n")
    f.write("Finally, this is the fifth line.\n")

with open("input.txt", "r") as f:
    content = f.read()

word_count = len(content.split())

content_upper = content.upper()

with open("output.txt", "w") as f:
    f.write(content_upper)
    f.write(f"\nWORD COUNT: {word_count}\n")

print("output.txt has been created Successfully Success Success.")


