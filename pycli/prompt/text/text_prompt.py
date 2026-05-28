from pycli.prompt.prompt import Prompt
from pycli.prompt.text.text_prompt_styles import TextPromptStyles


class TextPrompt(Prompt):
    message: str
    validator: str
    required: bool
    styles: TextPromptStyles

    def __init__(
        self,
        message: str = "Write your answer below:",
        validator: str = "This field is required. Please write a non-empty answer.",
        required: bool = False,
        styles: TextPromptStyles | None = None,
    ):
        super().__init__()
        self.message = message
        self.validator = (
            validator or "This field is required. Please write a non-empty answer."
        )
        self.required = required
        self.styles = styles if styles else TextPromptStyles()

    def _draw(self):
        print(self.styles.message.line(self.message))

    def render(self):
        while True:
            self._draw()
            ans = self.input.getln().strip()
            if ans or not self.required:
                return ans
            print(self.styles.validator.line(self.validator))


if __name__ == "__main__":
    ans = TextPrompt(message="What's 9 + 10", required=True).render()
    print(ans)
