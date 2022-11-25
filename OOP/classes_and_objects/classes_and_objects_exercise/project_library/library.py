from OOP.classes_and_objects.classes_and_objects_exercise.project_library.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        book_is_available = False
        for key, value in self.books_available.items():
            if key == author:
                for current_book in value:
                    if current_book == book_name:
                        book_is_available = True

        if not book_is_available:
            rented_days_to_return = 0
            for key, value in self.rented_books.items():
                for nested_key, nested_value in value.items():
                    if nested_key == book_name:
                        rented_days_to_return = nested_value
                        break
            return f'The book "{book_name}" is already rented and will be available in {rented_days_to_return} days!'

        else:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        else:
            user.books.remove(book_name)
            del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_name)
