# This program greets the user, calculates their birth year, and handles basic errors.
# Getting the user's name
name = input("Enter your name: ")           # Getting the user's age and calculating the birth year
print(f"Hello, {name}!")

age = int(input("Enter your age: "))
birth_year = 2024 - age
print(f"You were born in {birth_year}.")
fav_num = int(input("Enter your favorite number: "))        # Asking for the user's favorite number
  
    # Check if the number is even or odd
if fav_num % 2 == 0:
        print("That's an even number!")
else:
        print("That's an odd number!")

if fav_num > 10:
        print("Your favorite number is greater than 10.")
elif fav_num < 10:
        print("Your favorite number is less than 10.")
else:
        print("Your favorite number is exactly 10!")


class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_description(self):
        return f"{self.title} by {self.author}, published in {self.year_published}"

# Creating book instances
book1 = Book("Book Title 1", "Author 1", 2001)
book2 = Book("Book Title 2", "Author 2", 2015)

# Displaying book descriptions
print(book1.get_description())
print(book2.get_description())
def sort_books_by_year(books):
    
    if not books:
        print("No books to sort.")          # Handle empty list
        return []
    return sorted(books, key=lambda book: book.year_published)          # Sort books by year

sorted_books = sort_books_by_year([book1, book2])           # Using the function

# Using a for loop
for book in sorted_books:
    print(book.get_description())

# Using a while loop
i = 0
while i < len(sorted_books):
    print(sorted_books[i].get_description())
    i += 1

while True:
    search_title = input("Enter a book title to search for (or type 'exit' to quit): ")
    if search_title.lower() == "exit":
        break
    # Search for the book
    found = False
    for book in sorted_books:
        if book.title.lower() == search_title.lower():
            print(book.get_description())
            found = True
            break
    if not found:
        print("Book not found.")
