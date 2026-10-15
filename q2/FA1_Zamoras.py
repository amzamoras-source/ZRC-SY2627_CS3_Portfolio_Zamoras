# Coding Assessment: Library Management System
# Goal: Your goal is to demonstrate your understanding of designing classes properly, applying
# encapsulation and inheritance, and creating and testing objects.
# Role: You are a Junior Software Developer assigned to create a simple system for a school
# library.
# Audience: Your program will be used by the school librarian, who needs a clear and organized
# way to display information about library materials.
# Situation: The library has different types of materials. All library materials share common
# information: title and author. However, two specific material types, Book and Magazine, have
# additional attributes.
# ● All library materials have attributes title and author.
# ● Books have attributes: title, author, and number of pages
# ● Magazines have the attributes: title, author, and issue_number.
# Product: You must create a Python program that allows the librarian to display basic
# information about library materials and, for books and magazines, their specific details. Refer
# to the class diagram below for the minimum set of features for the classes to be used in the
# code.
# Create two objects of each class: Publication, Book, and Magazine, and display the objects'
# information as shown in the sample below.
# Other requirements:
# - Add data validation to number_of_pages and issue_number. Display a message such
# as “The number of pages must be positive” if the value is zero or negative.

class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages

    @property
    def number_of_pages(self):
        return self.__number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, value):
        if value <= 0:
            print("Number of pages must be positive.")
        else:
            self.__number_of_pages = value

    def display_info(self):
        super().display_info()
        if self.__number_of_pages is not None and self.__number_of_pages > 0:
            print("Number of pages:", self.__number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    @property
    def issue_number(self):
        return self.__issue_number

    @issue_number.setter
    def issue_number(self, value):
        if value <= 0:
            print("Issue number must be positive.")
        else:
            self.__issue_number = value

    def display_info(self):
        super().display_info()
        if self.__issue_number is not None and self.__issue_number > 0:
            print("Issue number:" + str(self.__issue_number))


pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
pub2 = Publication("The Science Journal", "Various Authors")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 350)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("TIME", "Sam Jacobs", 15)

print("Publication Information:")
pub1.display_info()

print("\nPublication Information:")
pub2.display_info()

print("\nBook Information:")
book1.number_of_pages = -310
book1.display_info()
print(book1.number_of_pages)

print("\nBook Information:")
book2.display_info()

print("\nMagazine Information:")
mag1.display_info()
print(mag1.issue_number)

print("\nMagazine Information:")
mag2.display_info()