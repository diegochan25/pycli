from pycli.element import Element
from pycli.styles.style import Style


class Title(Element):
    title: str

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title
        self.elements = {
            "title": Style(bg="cyan", text="bright_white", weight="bold")
        }

    def render(self):
        print(self.elements["title"].format(self.title))
