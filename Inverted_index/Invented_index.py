import os
import re

def build(files):
    inverted_index = {}

    for file_name in files:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            words = re.findall(r'\b\w+\b', content.lower())

            for word in set(words):
                if word not in inverted_index:
                    inverted_index[word] = [file_name]
                else:
                    inverted_index[word].append(file_name)

    return inverted_index

def search(inverted_index, query):
    query_words = re.findall(r'\b\w+\b', query.lower())
    result = set()

    for word in query_words:
        if word in inverted_index:
            result.update(inverted_index[word])

    return list(result)


directory_path = r'C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\Inverted_index\Text'
files = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith(".txt")]
inverted_index = build(files)

while True:
    search_query = input("Enter search query: ")
    if search_query == "exit":
        break

    search_result = search(inverted_index, search_query)

    if search_result:
        print("Matching files:")
        for file_name in search_result:
            print(f"- {file_name}")
    else:
        print("No matching files")