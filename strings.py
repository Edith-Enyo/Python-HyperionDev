# declared a variable called hero and assigned it to the value super man
hero = "Super Man"
# Converts string to uppercase
hero = hero.upper()
# hero = hero.replace(" ", "")  # replace space with nothing
# join each character with a ^
hero_join = "^".join(hero)
# split words to create space between S^U^P^E^R and M^A^N
splice_words = hero_join[:9]
splice_words2 = hero_join[12:]
print(splice_words + " " + splice_words2)

