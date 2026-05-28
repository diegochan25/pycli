from pycli.protocol.supports_execute import SupportsExecute
from pycli.protocol.supports_help import SupportsHelp


class Command(SupportsHelp, SupportsExecute):
    pass