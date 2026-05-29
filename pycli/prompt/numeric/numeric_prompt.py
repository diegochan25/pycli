from pycli.prompt.prompt import Prompt
from pycli.prompt.text.text_prompt_styles import TextPromptStyles


class NumericPrompt(Prompt):
    min: float | None
    max: float | None
    message: str
    validator: str
    required: bool
    styles: TextPromptStyles

    def __init__(
        self,
        message: str = "Write a number below:",
        validator: str | None = None,
        min: float | None = None,
        max: float | None = None,
        required: bool = False,
        styles: TextPromptStyles | None = None,
    ):
        super().__init__()
        self.message = message
        self.validator = (
            validator
            or f"Please write a valid number{f' between {min} and {max}' if min and max else f' higher than {min}' if min else f' lower than {max}' if max else ''}."
        )
        self.min = min
        self.max = max
        self.required = required
        self.styles = styles if styles else TextPromptStyles()

    def is_number(s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False

    def _draw(self):
        print(self.styles.message.line(self.message))

    def render(self):
        while True:
            self._draw()
            ans = self.input.getln().strip()
            if ans:
                if not self.is_number(ans):
                    print(self.styles.validator.line(self.validator))
                    continue
                num = float(ans)
                if (self.max and num > max) or (self.min and num < min):
                    print(self.styles.validator.line(self.validator))
                return num
            else:
                if not self.required:
                    return None
                print(self.styles.validator.line(self.validator))
