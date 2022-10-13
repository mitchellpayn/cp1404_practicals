"""
35mins
65mins
"""
text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split(" ")
text_to_count = {}

# iterating through the dictionary to find re-occurrences
for word in words:
    if word in text_to_count:
        text_to_count[word] += 1
    else:
        text_to_count[word] = 1

# convert dictionary to a list to be sorted
words = list(text_to_count.keys())
words.sort()

# formatting output to be aligned
max_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_length}} : {text_to_count[word]}")
