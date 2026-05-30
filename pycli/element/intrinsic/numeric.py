from pycli.element.interactive import Interactive
from pycli.styles.style import Style


class Numeric(Interactive):
    message: str
    validator: str
    min: float | None
    max: float | None
    required: bool

    def __init__(
        self,
        name: str,
        message: str = "Write a number below:",
        validator: str | None = None,
        min: float | None = None,
        max: float | None = None,
        required: bool = False,
    ):
        super().__init__(name)
        self.message = message
        self.min = min
        self.max = max
        self.required = required
        self.validator = (
            validator
            or f"Please write a valid number{f' between {min} and {max}' if min is not None and max is not None else f' higher than {min}' if min is not None else f' lower than {max}' if max is not None else ''}."
        )
        self.elements = {
            "message": Style(text="bright_black"),
            "validator": Style(text="red", weight="bold"),
        }

    @staticmethod
    def _is_number(s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False

    def _draw(self) -> None:
        print(self.elements["message"].format(self.message))

    def render(self) -> float | None:
        while True:
            self._draw()
            ans = self.input.getln().strip()
            if ans:
                if not self._is_number(ans):
                    print(self.elements["validator"].format(self.validator))
                    continue
                num = float(ans)
                if (self.max is not None and num > self.max) or (self.min is not None and num < self.min):
                    print(self.elements["validator"].format(self.validator))
                    continue
                return num
            if not self.required:
                return None
            print(self.elements["validator"].format(self.validator))
