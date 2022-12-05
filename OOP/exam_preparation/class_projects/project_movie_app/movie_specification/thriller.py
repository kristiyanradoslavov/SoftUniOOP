from OOP.exam_preparation.class_projects.project_movie_app.movie_specification.movie import Movie


class Thriller(Movie):
    MIN_AGE = 16

    def __init__(self, title, year, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"


