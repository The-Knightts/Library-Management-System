'''Add Book details Function'''
def Add_Book(title, author, genre):
    return (title, author, genre)

'''Adding the book to the library'''
def Add_to_Library(library, book, books_set):
    if book not in books_set:
        library.append(book)
        books_set.add(book)
        print(f'The Book {book[0]} by {book[1]} added to the library.')
    else:
        print(f"The Book '{book[0]}' by {book[1]} already exists in the library.")

'''Removing book from the library'''
def Remove_from_Library(title, library, books_set):
    for book in library:
        if book[0] == title:
            library.remove(book)

            books_set.remove(book)
            print(f"Book '{title}' removed from the library.")
    print(f"Book '{title}' not found in the library.")

'''Searching book from the library'''
def Search_Books(library, search_term):
    results = []
    for book in library:
        if search_term.lower() in book[0].lower() or search_term.lower() in book[1].lower():
            results.append(book)
    return results

'''Showing the list of the books'''
def List_Books(library):
    if library:
        result = ""
        for book in library:
            result += f"\nTitle: {book[0]}, Author: {book[1]}, Genre: {book[2]}"
        return result
    else:
        return "No books in the library."
    
'''Categorizing the books by genre'''
def Categorize_Books(library):
    categorized = {}
    for book in library:
        if book[2] not in categorized:
            categorized[book[2]] = []
        categorized[book[2]].append(book)
    
    print("\nCategorized Books by Genre:")
    for genre, library in categorized.items():
        print(f"\nGenre: {genre}")
        for book in library:
            print(f"  Title: {book[0]}, Author: {book[1]}")