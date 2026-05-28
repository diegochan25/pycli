from pycli.styles.styles import Styles


class YNPromptStyles:
    message: Styles = Styles(text="bright_black")
    validator: Styles = Styles(text="red", weight="bold")
