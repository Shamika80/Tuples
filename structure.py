def add_book(library, title, author):
  

  if not isinstance(title, str) or not isinstance(author, str):
    print("Error: Title and author must be strings.")
    return library

  new_book = (title.lower(), author.lower())  
  if new_book not in library:
    library.append(new_book)
    print(f"Book '{title}' by {author} added successfully!")
  else:
    print(f"Book '{title}' by {author} already exists in the library.")

  return library

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

add_book(library.copy(), "The Lord of the Rings", "J.R.R. Tolkien")  
add_book(library.copy(), "1984", "george orwell")  


print("\nUpdated Library:")
for book in library:
  title, author = book
  print(f"- {title} by {author}")