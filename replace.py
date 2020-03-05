# declared a string and assigned a value to it, removed all exclamations and printed in capital letters
replace_function = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
print(replace_function.replace("!", " ").upper())

# printed sentence in reverse
replace_function = (replace_function.replace("!", " ").upper())[::-1]
print(replace_function)


