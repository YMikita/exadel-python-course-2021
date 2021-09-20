import re


texts = [
    "Hello, World!",
    "The world is mine",
    "Hello, how are you?"
]


def generate_word_stats(data):
    result = {}
    for index, line in enumerate(data):
        for wordList in line.split(" "):
            word = re.sub(r"\W", "", wordList.lower())
            if word in result:
                result[word]['count'] += 1
            else:
                result[word] = {
                    'count': 1,
                    'index': index
                }
    return result


def print_table_cols(word, count, first_line):
    print(f'{word:8}    {count:5}   {first_line:10}')


def print_table(data):
    print_table_cols("word", "count", "first line")
    for key in data:
        item = data[key]
        print_table_cols(key, item["count"], item["index"])


print_table(generate_word_stats(texts))
