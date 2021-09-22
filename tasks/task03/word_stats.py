import re


texts = [
    "Hello, World!",
    "The world is mine",
    "Hello, how are you?"
]


def get_index(word, data):
    for index, line in enumerate(data):
        if word in line.lower():
            return index
    return 0


def generate_word_stats(data):
    result = {}
    word_list = re.sub(r"[^\w ]", "", ' '.join(data)).lower().split(" ")
    for word in word_list:
        result.update({
            word: dict(count=word_list.count(word), index=get_index(word, data))
        })
    return result


def print_table_cols(word, count, first_line):
    print(f'{word:8}    {count:5}   {first_line:10}')


def print_table(data):
    print_table_cols("word", "count", "first line")
    for key in data:
        item = data[key]
        print_table_cols(key, item["count"], item["index"])


print_table(generate_word_stats(texts))
