def print_upper_words(words, must_start_with):
    ''' Take an array of words and return uppercased words'''
    for word in words:
        for item in must_start_with:
            if word[0] == item:
            # if word.startswith(item):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
# print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "earth", "Explorer"])
print(print_upper_words.__doc__)