def count_words(book):
    nwords = 0
    for line in [book] if type(book) is str else book:
        nwords += len(line.split())
    return nwords
