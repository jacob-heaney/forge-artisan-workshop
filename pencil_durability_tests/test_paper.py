from pencil_durability.paper import Paper


def test_new_paper_is_blank():
    paper = Paper()
    assert paper.contents == ""

def test_write_hello_makes_paper_contents_hello():
    # Arrange
    paper = Paper()

    # Act
    paper.write("Hello")

    # Assert
    assert paper.contents == "Hello"

def test_write_hello_then_how_are_you():
    paper = Paper()
    paper.write("Hello")
    paper.write(" how are you")
    assert paper.contents == "Hello how are you"

def test_write_new_line():
    paper = Paper()
    paper.write("Hello")
    paper.write("\n")
    paper.write("how are you")
    assert paper.contents == "Hello\nhow are you"

def test_erase_hello_from_hello():
    # Arrange
    paper = Paper()
    paper.write("Hello")

    # Act
    paper.erase("Hello")

    # Assert
    assert paper.contents == "     "

def test_erase_hello_from_hello_world():
    # Arrange
    paper = Paper()
    paper.write("Hello World")

    # Act
    paper.erase("Hello")

    # Assert
    assert paper.contents == "      World"

def test_erase_chuck_from_woodchuck_tongue_twister():
    paper = Paper()
    paper.write("How much wood would a woodchuck chuck if a woodchuck could chuck wood?")

    paper.erase("chuck")

    assert paper.contents == "How much wood would a woodchuck chuck if a woodchuck could       wood?"
