from OOP.exam_preparation.class_projects.project_movie_app.movie_specification.movie import Movie


class Action(Movie):
    MIN_AGE = 12

    def __init__(self, title, year, owner, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"

