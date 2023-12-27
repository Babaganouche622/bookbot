from BookReader import BookReader

def main():
    book_path = "books/frankenstein.txt"

    frankenstein_reader = BookReader(book_path)

    frankenstein_reader.generate_report()

main()