def read(fn):
    with open(fn) as f:
        return [line for line in f]


def display(book):
    for line in book:
        print(line, end="")


def count_words(book):
    nwords = 0
    for line in [book] if type(book) is str else book:
        nwords += len(line.split())
    return nwords


def count_characters(book, normalize=True):
    counts = dict()
    for line in [book] if type(book) is str else book:
        for c in line:
            if not c.isalpha():
                continue
            if normalize:
                c = c.lower()
            counts[c] = counts.get(c, 0) + 1
    return counts


def display_report(fn, nwords, char_counts):
    print(f"--- Begin report of {fn} ---")
    print(f"{nwords} words found in the document\n")
    for char, count in char_counts.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def main():
    """Read a book and print it out."""
    fn = "books/frankenstein.txt"
    book = read(fn)
    nwords = count_words(book)
    char_counts = count_characters(book)
    display_report(fn, nwords, char_counts)


if __name__ == "__main__":
    main()
