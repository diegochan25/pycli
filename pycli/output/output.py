from pycli.output.output_styles import OutputStyles


class Output:
    line: str
    styles: OutputStyles

    def __init__(self, message: str = "", styles: OutputStyles | None = None):
        self.line = message
        self.styles = styles if styles else OutputStyles()

    def render(self) -> str:
        print(self.styles.message.line(self.line))
        return self.line
