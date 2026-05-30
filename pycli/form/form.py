from pycli.protocol.supports_render import SupportsRender
from pycli.form.form_data import FormData
from pycli.form.fork import ForkResult


class Form:
    def __init__(self, **fields: SupportsRender):
        self._fields = fields

    def render(self) -> FormData:
        data = FormData()
        for name, field in self._fields.items():
            result = field.render()
            if isinstance(result, ForkResult):
                if result.value is not None:
                    setattr(data, name, result.value)
                for k, v in result.extra.items():
                    setattr(data, k, v)
            elif result is not None:
                setattr(data, name, result)
        return data
