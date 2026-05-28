from pycli.input.input_mapper import InputMapper
from pycli.input.key import Key

_SINGLE: dict[str, Key] = {
    "\r": Key.Enter,
    " ": Key.Space,
    "\t": Key.Tab,
    "\x08": Key.Backspace,
    "\x1b": Key.Escape,
    "0": Key.Digit0,
    "1": Key.Digit1,
    "2": Key.Digit2,
    "3": Key.Digit3,
    "4": Key.Digit4,
    "5": Key.Digit5,
    "6": Key.Digit6,
    "7": Key.Digit7,
    "8": Key.Digit8,
    "9": Key.Digit9,
    "`": Key.Backquote,
    "\\": Key.Backslash,
    "[": Key.BracketLeft,
    "]": Key.BracketRight,
    ",": Key.Comma,
    "=": Key.Equal,
    "-": Key.Minus,
    ".": Key.Period,
    "'": Key.Quote,
    ";": Key.Semicolon,
    "/": Key.Slash,
}

_EXTENDED: dict[str, Key] = {
    "\xe0\x48": Key.ArrowUp,
    "\xe0\x50": Key.ArrowDown,
    "\xe0\x4b": Key.ArrowLeft,
    "\xe0\x4d": Key.ArrowRight,
    "\xe0\x47": Key.Home,
    "\xe0\x4f": Key.End,
    "\xe0\x49": Key.PageUp,
    "\xe0\x51": Key.PageDown,
    "\xe0\x52": Key.Insert,
    "\xe0\x53": Key.Delete,
    "\x00\x3b": Key.F1,
    "\x00\x3c": Key.F2,
    "\x00\x3d": Key.F3,
    "\x00\x3e": Key.F4,
    "\x00\x3f": Key.F5,
    "\x00\x40": Key.F6,
    "\x00\x41": Key.F7,
    "\x00\x42": Key.F8,
    "\x00\x43": Key.F9,
    "\x00\x44": Key.F10,
    "\x00\x85": Key.F11,
    "\x00\x86": Key.F12,
}


class Win32Mapper(InputMapper):
    def map(self, seq: str) -> Key:
        if seq in _EXTENDED:
            return _EXTENDED[seq]
        if seq in _SINGLE:
            return _SINGLE[seq]
        if len(seq) == 1 and seq.isalpha():
            return Key["Key" + seq.upper()]
        return Key.Unidentified
