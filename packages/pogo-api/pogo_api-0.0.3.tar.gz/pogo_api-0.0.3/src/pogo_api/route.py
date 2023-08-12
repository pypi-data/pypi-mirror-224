from dataclasses import dataclass
from typing import Callable

from fastapi import APIRouter
from fastapi import FastAPI

from pogo_api.http import Method


@dataclass
class Route:
    path: str
    method: Method
    endpoint: Callable
    tag: str

    def add_to_router(self, router: APIRouter | FastAPI) -> None:
        router.add_api_route(
            path=self.path,
            methods=[self.method.value],
            endpoint=self.endpoint,
            tags=[self.tag],
        )
