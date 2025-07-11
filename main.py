from stats import word_count



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents






       
def main():
    book_text = get_book_text("/home/nemosley17/bookbot/books/frankenstein.txt")
    count_words = word_count(book_text)
    print(f"{count_words} words found in the document")
    
main()