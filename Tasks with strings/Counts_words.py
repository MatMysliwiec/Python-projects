def count_words(string):
    words = string.split()
    return len(words)


def from_file(file):
    try:
        with open(file, "r") as file:
            content = file.read()
            word_counts = count_words(content)
            print("Total words in te file: ", word_counts)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred: ", e)


file_path = r"/Inverted_index/Text/file1.txt"
from_file(file_path)