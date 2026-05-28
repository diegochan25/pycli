from pycli.output.output_styles import OutputStyles


class Output:
    line: str
    styles: OutputStyles

    def __init__(self, line: str = "", styles: OutputStyles | None = None):
        self.line = line
        self.styles = styles if styles else OutputStyles()

    def render(self) -> str:
        print(self.styles.line.line(self.line))
        return self.line
