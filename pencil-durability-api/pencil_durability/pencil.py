from pydantic import BaseModel

from pencil_durability.paper import Paper


class Pencil(BaseModel):

    durability = 0

    # def __init__(self, durability, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.durability = durability

    def write(self, text, paper: Paper):
        paper.write(text)
        self.durability -= len(text)
