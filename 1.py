import fun
'''Main Part Staring from here !!!!'''
library = []
books_set = set()
while True:
    print('\nWelcome to the Static Library Management System')
    print('1. Add a book')
    print('2. Remove a book')
    print('3. Search a book')
    print('4. List all the books')
    print('5. Categorize the books by genre')
    print('6. Exit')

    choice = int(input('Enter the choice from 1 - 6 for the operations :'))

    if choice == 1:
        print('Enter the details about the book to be added!!')
        title = input('Enter the Title of the book :')
        author = input('Enter the Name of Author of the book :')
        genre = input('Enter the Genre of the book :')
        book = fun.Add_Book(title, author, genre)
        fun.Add_to_Library(library, book, books_set)

    elif choice == 2:
        title = input('Enter the title of the book to be removed :')
        fun.Remove_from_Library(title,library,books_set)
    
    elif choice == 3:
        search_term = input('Enter the title or the author of the book to be searched :')
        print(fun.Search_Books(library, search_term))
    
    elif choice == 4:
        print('The list of the books in the library are ')
        print(fun.List_Books(library))
    
    elif choice == 5:
        fun.Categorize_Books(library)
    
    elif choice == 6:
        print('Exit')
    
    else:
        print('Invalid Choice. Enter a correct choice!!')