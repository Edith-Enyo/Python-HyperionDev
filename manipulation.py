# Prompt user to enter a sentence, calculate and display length or the sentence
str_manip = input("Enter a sentence: ")
print(len(str_manip))
# Find last letter in the sentence and replace every occurrence of letter with @
print("\nFind last letter in the sentence and replace every occurrence of letter with @")
print(str_manip.replace(str_manip[-1], "@"))
# Print last three characters in reverse
print("\nPrint last three characters in reverse")
str_return = (str_manip[-3:])[::-1]
print(str_return)
# Create 5 letter work from first three letters and last 2 letters
print("\nCreate 5 letter work from first three letters and last 2 letters")
print(str_manip[:3]+str_manip[-2:])
# Display each word in the sentence on a new line
print("\nDisplay each word in the sentence on a new line")
splitList = str_manip.split()
# print(splitList[::-1])
print(*splitList, sep="\n")

