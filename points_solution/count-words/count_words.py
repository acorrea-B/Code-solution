import os


def count_words(file_name):
    try:
        file = open(os.path.dirname(__file__) + f"/{file_name}", "r")
    except:
        raise FileNotFoundError("Try again with existent file")
    else:
        words = file.readlines()

    # Validate if number of words is correct
    if int(words[0]) == len(words) - 1:
        unique_words = list(set(words[1:]))
        counter = ""
        # Count the number of times each word is repeated
        for unique_word in sorted(unique_words):
            counter += str(words.count(unique_word)) + " "
        # Create output file
        new_file = open(os.path.dirname(__file__) + "/words_counted.txt", "w")
        # Add result on output file
        new_file.write(f"{len(unique_words)} \n")
        new_file.write(counter)
        return

    raise ValueError("The number of words does not match the one indicated in the file")
