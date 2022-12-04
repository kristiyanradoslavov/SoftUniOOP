import xml.dom.minidom

from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def get_user_usernames(self):
        usernames = [x.username for x in self.users_collection]
        return usernames

    def get_movie_titles(self):
        titles = [m.title for m in self.movies_collection]
        return titles

    def register_user(self, username: str, age: int):
        all_users_usernames = self.get_user_usernames()
        if username in all_users_usernames:
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie):
        all_users_usernames = self.get_user_usernames()
        if username not in all_users_usernames:
            raise Exception("This user does not exist!")
        current_owner = movie.owner.username
        if current_owner != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        movie.owner.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie, **kwargs):
        all_movies_names = self.get_movie_titles()
        if movie.title not in all_movies_names:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        owner = movie.owner.username
        if username != owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie):
        all_movies_names = self.get_movie_titles()
        if movie.title not in all_movies_names:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        owner = movie.owner.username
        if owner != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        current_movie = list(filter(lambda m: m.title == movie.title, self.movies_collection))[0]
        self.movies_collection.remove(current_movie)
        movie.owner.movies_owned.remove(current_movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie):
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        current_user = list(filter(lambda u: u.username == username, self.users_collection))[0]

        try:
            next(filter(lambda m: m.title == movie.title, current_user.movies_liked))
            raise Exception(f"{username} already liked the movie {movie.title}!")

        except StopIteration:
            current_user.movies_liked.append(movie)
            movie.likes += 1

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie):
        current_user = list(filter(lambda u: u.username == username, self.users_collection))[0]

        liked_movie = list(filter(lambda x: x.title == movie.title, current_user.movies_liked))

        if not liked_movie:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        current_user.movies_liked.remove(liked_movie[0])
        movie.likes -= 1

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_result = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        final_result = []

        if not sorted_result:
            return "No movies found."

        else:
            for movie in sorted_result:
                final_result.append(movie.details())

        return "\n".join(final_result)

    def __str__(self):
        users_result = []
        movies_result = []

        if not self.users_collection:
            users_result.append("All users: No users.")

        else:
            all_usernames = [x.username for x in self.users_collection]
            users_result.append(f"All users: {', '.join(all_usernames)}")

        if not self.movies_collection:
            movies_result.extend("All movies: No movies.")
        else:
            all_titles = [t.title for t in self.movies_collection]
            movies_result.append(f"All movies: {', '.join(all_titles)}")

        return ''.join(users_result) + "\n" + ''.join(movies_result)

