from sys import argv

script, filename = argv

txt = open(filename)
print(">>>> this is argv", repr(argv))
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename agian:")
file_again = input("> ")

txt_again= open(file_again)

print(txt_again.read())



