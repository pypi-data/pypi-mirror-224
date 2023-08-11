from abc import ABC
from typing import Any, Generic, TypeVar

from wonda.bot.updates.base import BaseUpdate

_ = Any
T = TypeVar("T", bound=BaseUpdate)


class ABCMiddleware(ABC, Generic[T]):
    async def pre(self, update: T, ctx: dict) -> bool:
        pass

    async def post(self, update: T, ctx: dict, responses: list[_]) -> None:
        pass
