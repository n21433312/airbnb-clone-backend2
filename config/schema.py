import strawberry
import typing

@strawberry.type
class Movie:
    pk:int
    title:str
    year:int
    rating:int

movies_db = [
    Movie(pk = 1, title="Godfather", year=1990, rating=10),
]

@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> typing.List[Movie]:
        return movies_db
    
    @strawberry.field
    def movie(self, movie_id:int) -> Movie:
        return
    
schema = strawberry.Schema(query=Query)
