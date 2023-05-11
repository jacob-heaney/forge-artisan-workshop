from fastapi import FastAPI

from pencil_durability.paper import Paper
from pencil_durability.pencil import Pencil

app = FastAPI()


pencils = []
sheets_of_paper = []


@app.get("/pencil/")
def get_pencils():
    return pencils


@app.post("/pencil/")
def create_pencil(pencil: Pencil):
    pencils.append(pencil)
    return pencil


@app.get("/paper/")
def get_paper():
    return sheets_of_paper


@app.post("/paper/")
def create_paper(paper: Paper):
    sheets_of_paper.append(paper)
    return paper


@app.post("/write/")
def write(text_to_write: str):
    stored_pencil().write(text_to_write, stored_paper())


def stored_pencil() -> Pencil:
    return pencils[0]

def stored_paper() -> Paper:
    return sheets_of_paper[0]