from msgspec import Struct, json, to_builtins

omit_defaults = True
rename = lambda n: n.rstrip("_") if n.endswith("_") else None


class Model(Struct, rename=rename, omit_defaults=omit_defaults):
    def dict(self) -> dict:
        return {k: getattr(self, k) for k in self.__struct_fields__}


def to_json(v):
    return bytes.decode(json.encode(v))


def translate(v):
    return (
        v
        if isinstance(v, tuple)
        else (str(v) if type(v) in (int, str) else to_json(to_builtins(v)))
    )


def get_params(loc: dict):
    n = {k: v for k, v in loc.items() if k not in ("self", "kwargs") and v is not None}
    n.update(loc["kwargs"])
    return n


__all__ = ("Model", "get_params", "json")
