from pycli.prompt.prompt import Prompt
from pycli.prompt.yn.yn_prompt_styles import YNPromptStyles


class YNPrompt(Prompt):
    message: str
    validator: str
    yes: str
    no: str
    case_sensitive: bool

    def __init__(
        self,
        message: str | None = None,
        validator: str | None = None,
        yes: str = "Y",
        no: str = "n",
        case_sensitive: bool = False,
        styles: YNPromptStyles | None = None,
    ):
        super().__init__()
        self.message = message or f"Write '{yes}' (Yes) / '{no}' (No)."
        self.validator = validator or f"Please use only '{yes}' for Yes or '{no}' for No{' (case sensitive)' if case_sensitive else ''}."
        self.yes = yes
        self.no = no
        self.case_sensitive = case_sensitive
        self.styles = styles or YNPromptStyles()

    def _draw(self):
        print(self.styles.message.line(self.message))

    def render(self):
        while True:
            self._draw()
            ans = self.input.getln().strip()
            is_valid = False
            if self.case_sensitive:
                is_valid = (ans == self.yes or ans == self.no)
            else:
                is_valid = (ans.lower() == self.yes.lower() or ans.lower() == self.no.lower())
            if is_valid:
                return ans.lower() == self.yes.lower()
            print(self.styles.validator.line(self.validator))


if __name__ == "__main__":
    ans = YNPrompt().render()
    print(ans)