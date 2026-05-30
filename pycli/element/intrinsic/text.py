from pycli.element.interactive import Interactive
from pycli.styles.style import Style


class Text(Interactive):
    message: str
    validator: str
    required: bool

    def __init__(
        self,
        name: str,
        message: str = "Write your answer below:",
        validator: str = "This field is required. Please write a non-empty answer.",
        required: bool = False,
    ):
        super().__init__(name)
        self.message = message
        self.validator = validator
        self.required = required
        self.elements = {
            "message": Style(text="bright_black"),
            "validator": Style(text="red", weight="bold"),
        }

    def _draw(self) -> None:
        print(self.elements["message"].format(self.message))

    def render(self) -> str:
        while True:
            self._draw()
            ans = self.input.getln().strip()
            if ans or not self.required:
                return ans
            print(self.elements["validator"].format(self.validator))
