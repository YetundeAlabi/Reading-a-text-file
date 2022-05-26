# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as file:
        contents = file.read()
        return contents

def count_words():
    text = read_file_content("./story.txt").lower()
    words = text.split()
    stripped_words = [word.strip(', . ?') for word in words]
    unique_words = set(stripped_words)

    new_dict = {}
    for key in unique_words:
        value = stripped_words.count(key)
        new_dict[key] = value
    return new_dict


print(count_words())

