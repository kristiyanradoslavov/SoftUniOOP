from project.movie_specification.movie import Movie


class Fantasy(Movie):
    MIN_AGE = 6

    def __init__(self, tittle, year, owner, age_restriction=6):
        super().__init__(tittle, year, owner, age_restriction)

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"


