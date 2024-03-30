words = ["hello", "hey", "goodbye", "yo", "yes", "osb", "sam", "123"]

# def print_upper_words(list):
#     for i in range(len(words)):
#         words[i] = words[i].upper()
#     return words

# print(print_upper_words(words))

# def print_upper_words(list, must_start_with={"h", "y"}):
#     res = []
#     for i in range(len(words)):
#         for char in must_start_with:
#             if words[i][0].startswith(char):
#                 res.append(words[i])
#     return res
        
# print(print_upper_words(words))

def print_upper_words(word_list, must_start_with={"o", "y"}):
    res = list(filter(lambda word: any(word.startswith(char) for char in must_start_with), words))
    return res
        
print(print_upper_words(words))