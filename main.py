from stats import count_words

import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Collect statistics about a book.")
    parser.add_argument("path",
        help="path to the text file containing the contents of a book")
    return parser.parse_args()


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


def old_display_report(fn, nwords, char_counts):
    print(f"--- Begin report of {fn} ---")
    print(f"{nwords} words found in the document\n")
    for char, count in char_counts.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def display_report(fn, nwords, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fn}...")
    print("----------- Word Count ----------")
    print(f"Found {nwords} total words")
    print(f"--------- Character Count -------")
    for char, count in sorted(char_counts.items(), key=lambda t: -int(t[1])):
        print(f"{char}: {count}")
    print("============= END ===============")


def main():
    """Read a book and print it out."""
    args = parse_args()
    fn = args.path
    book = read(fn)
    nwords = count_words(book)
    char_counts = count_characters(book)
    display_report(fn, nwords, char_counts)


if __name__ == "__main__":
    main()
