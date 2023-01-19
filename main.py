from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
app = FastAPI();


movies = [
    {
        "id":1,
        "title":"Back to the future",
        "overview":"Volver al futuro",
        "year":1991,
        "rating": 9.7,
        "category":"Ciencia Ficcion"
    },
      {
        "id":2,
        "title":"Back to the future",
        "overview":"Volver al futuro",
        "year":1991,
        "rating": 9.7,
        "category":"Ciencia Ficcion"
    }
]

@app.get('/')
def inicio():
    return HTMLResponse('Hola Mundo')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies;



@app.get('/movies/{id}', tags=['movies'])
#le pasamos el id a nuestra funcion 
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if ["item"] == category ]


@app.post('/movies', tags=['movies'])
def create_movie(id:int = Body(), title: str = Body() , overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        "id":id,
        "title":title,
        "overview":overview,
        "year":year,
        "rating":rating,
        "category":category
    })
    return title   


@app.put("/movies/{id}", tags=['movies'])
def update_movie(id: int, title: str = Body() , overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies:
        if item["id"] == id:
            item["title"]=title,
            item["overview"]= overview,
            item["year"]=year,
            item["rating"]=rating,
            item["category"]=category
    return movies;


@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
    return movies;
