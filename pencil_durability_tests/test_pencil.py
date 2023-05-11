from pencil_durability.paper import Paper
from pencil_durability.pencil import Pencil


def test_new_pencil_starts_with_durability_15():
    pencil = Pencil(15)
    assert pencil.durability == 15

def test_new_pencil_starts_with_durability_100():
    pencil = Pencil(100)
    assert pencil.durability == 100

def test_writing_1_letter_degrades_pencil_by_1():
    pencil = Pencil(100)
    pencil.write("a", Paper())
    assert pencil.durability == 99

def test_writing_3_letters_degrades_pencil_by_3():
    pencil = Pencil(100)
    pencil.write("abc", Paper())
    assert pencil.durability == 97

def test_writing_with_pencil_shows_text_on_paper():
    pencil = Pencil(100)
    paper = Paper()

    pencil.write("bananas", paper)

    assert paper.contents == "bananas"
