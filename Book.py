"""
Object Orintated Program
This is the basics of an object orinated program

'book' is an object and can do a lot of things, This program just
shows the basics of what you can do
"""

# Book class
class book:
    def __init__(self, title, genre, author):
        self.title = title
        self.genre = genre
        self.author = author

if __name__ == '__main__':
    # Make values
    b = book("To kill a mockingbird", "southern gothic", "Harper Lee")
    b2 = book("1984", "dystopian fiction", "George Orwell")
    b3 = book("Load of the rings", "Fantasy", "JR Tolkien")
    b4 = book("Dragon's Green", "Fantasy Fiction", "Scarlett Thomas")
    b5 = book("Murder Most Unladylike", "Mystery fiction", "Robin Stevens")

    # Output
    LOB = [b, b2, b3, b4, b5]
    print(LOB[4].author)
    print(LOB[2].genre)