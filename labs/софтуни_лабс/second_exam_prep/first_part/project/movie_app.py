import os


from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        new_user = User(username, age)
        curr_user = self.__find_user_by_name(username)
        if curr_user is not None:
            raise Exception("User already exists!")

        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        curr_user = self.__find_user_by_name(username)
        if curr_user is None:
            raise Exception("This user does not exist!")
        if curr_user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        curr_user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        curr_user = self.__find_user_by_name(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if curr_user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        movie.title = kwargs.get("title", movie.title)
        movie.age_restriction = kwargs.get("age_restriction", movie.age_restriction)
        movie.year = kwargs.get("year", movie.year)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        curr_user = self.__find_user_by_name(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if curr_user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        curr_user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        curr_user = self.__find_user_by_name(username)
        if curr_user == movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in curr_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        curr_user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        curr_user = self.__find_user_by_name(username)
        if movie not in curr_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        curr_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        ordered_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        result = os.linesep.join([m.details() for m in ordered_movies])
        return result

    def __str__(self):
        result = "All users: "
        if not self.movies_collection:
            result += "No users."
        else:
            users = ", ".join([u.username for u in self.users_collection])
            result += users

        result += "\nAll movies: "

        if not self.users_collection:
            result += "No movies."
        else:
            movies = ", ".join([m.title for m in self.movies_collection])
            result += movies

        return result

    def __find_user_by_name(self, user_name):
        for user in self.users_collection:
            if user.username == user_name:
                return user
