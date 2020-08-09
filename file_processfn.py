def process(char, path ="book.txt"):
    file = open(path)
    content = file.read()
    return content.count(char)
        