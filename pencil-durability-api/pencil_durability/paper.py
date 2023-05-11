from pydantic import BaseModel


class Paper(BaseModel):
    contents = ""

    def write(self, new_text):
        self.contents += new_text

    def erase(self, text_to_erase):
        found_index = self.contents.rfind(text_to_erase)
        print(f"FOUND AT INDEX: {found_index}")

        first_part = self.contents[0:found_index]
        second_part = self.contents[found_index:len(self.contents)]
        new_second_part = second_part.replace(text_to_erase, "     ")

        self.contents = first_part + new_second_part
