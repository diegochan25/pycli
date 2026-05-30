from pycli.element.interactive import Interactive
from pycli.styles.style import Style


class YesNo(Interactive):
    message: str
    validator: str
    yes: str
    no: str
    case_sensitive: bool

    def __init__(
        self,
        name: str,
        message: str | None = None,
        validator: str | None = None,
        yes: str = "Y",
        no: str = "n",
        case_sensitive: bool = False,
    ):
        super().__init__(name)
        self.yes = yes
        self.no = no
        self.case_sensitive = case_sensitive
        self.message = message or f"Write '{yes}' (Yes) / '{no}' (No)."
        self.validator = validator or f"Please use only '{yes}' for Yes or '{no}' for No{' (case sensitive)' if case_sensitive else ''}."
        self.elements = {
            "message": Style(text="bright_black"),
            "validator": Style(text="red", weight="bold"),
        }

    def _draw(self) -> None:
        print(self.elements["message"].format(self.message))

    def render(self) -> bool:
        while True:
            self._draw()
            ans = self.input.getln().strip()
            if self.case_sensitive:
                is_valid = ans == self.yes or ans == self.no
            else:
                is_valid = ans.lower() == self.yes.lower() or ans.lower() == self.no.lower()
            if is_valid:
                return ans.lower() == self.yes.lower()
            print(self.elements["validator"].format(self.validator))
