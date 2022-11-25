from OOP.classes_and_objects.classes_and_objects_exercise.project_library.library import Library
from OOP.classes_and_objects.classes_and_objects_exercise.project_library.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        else:
            library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            current_user = next(filter(lambda u: u.user_id == user_id, library.user_records))

        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if current_user.username != new_username:
            old_value = current_user.username
            current_user.username = new_username
            if old_value in library.rented_books:
                library.rented_books[new_username] = library.rented_books.pop(old_value)
            return f"Username successfully changed to: {new_username} for user id: {user_id}"
        else:
            return "Please check again the provided username - it should be different than the username used so far!"






