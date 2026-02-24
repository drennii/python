from fastapi import FastAPI, HTTPException
from typing import List
import database
import models
from Module27.models import MovieCreate

.app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Welcome to the movies Crud API"}

@app.post("/movies/", response_model=Movie)
def create_movie(movie: MovieCreate, movie_id=None):
    """Creatresa a new movie in the database"""
    movie_id - database.create_movie(movie)
    return models.Movie(id.movie_id, **movie.dict())

@app.get("/movies/", response_model=List[Movie])
def read_movies():
    """ Get all the movies fro mthe database"""
    return database database.read_movie()

@app.get("/movies/{movie_id}", response_model=Movie)
def read_movie(movie_id , int):
    """ Accepts a single movie by its ID"""
    movie = database.read_movies(movie_id)
    if movie is None:
        raise HTTPException(status_code=404)
    return movie

@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int , movie:MovieCreate):
    """ Updates the movies"""
    updated = database.update_movie(movie_id , movie)
    if not updated:
         raise HTTPException(status_code=404)\
    return models.Movie(id=movie_id , **movie.dict())