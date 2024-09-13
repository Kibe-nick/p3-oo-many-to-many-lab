class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        # Return all contracts related to this author
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        # Return all books related to this author through contracts
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Sign a new contract for the author with the given book, date, and royalties
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Calculate total royalties from all contracts
        return sum([contract.royalties for contract in self.contracts()])

    def __repr__(self):
        return f"Author(name={self.name})"


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        # Return all contracts related to this book
        return [contract for contract in Contract.all_contracts if contract.book == self]
    
    def authors(self):
        # Return all authors related to this book through contracts
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f"Book(title={self.title})"


import re
from datetime import datetime
class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        # Validate and parse the date 
        try:
            self.date = datetime.strptime(date, "%m/%d/%Y")
        except ValueError:
            raise ValueError("date must be in MM/DD/YYYY format")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("royalties must be a non-negative integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date_str):
        """Returns a list of contracts that match the specified date, sorted by royalties."""
        try:
            target_date = datetime.strptime(date_str, "%m/%d/%Y")
        except ValueError:
            raise ValueError("Date must be in MM/DD/YYYY format")

        # Filter contracts by the target date
        contracts_on_date = [contract for contract in cls.all_contracts if contract.date.date() == target_date.date()]
        # Sort contracts by royalties in ascending order
        return sorted(contracts_on_date, key=lambda contract: contract.royalties)
       
    def __repr__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date={self.date.strftime('%m/%d/%Y')}, royalties={self.royalties})"
