from typing import Callable, Coroutine

from pogo_api.http import Method
from pogo_api.pascal_converter import pascal_to_kebab
from pogo_api.pascal_converter import pascal_to_name
from pogo_api.route import Route


class Endpoint:
    method = Method.GET
    endpoint: Callable[..., Coroutine]

    @property
    def name(self) -> str:
        return pascal_to_name(self.__class__.__name__)

    @property
    def path(self) -> str:
        kebab_case = pascal_to_kebab(pascal=self.__class__.__name__)
        return f"/{kebab_case}"

    @property
    def route(self) -> Route:
        return Route(
            path=self.path,
            method=self.method,
            endpoint=self.endpoint,
            tag=self.name,
        )


class DeleteEndpoint(Endpoint):
    method = Method.DELETE


class GetEndpoint(Endpoint):
    method = Method.GET


class PatchEndpoint(Endpoint):
    method = Method.PATCH


class PostEndpoint(Endpoint):
    method = Method.POST


class PutEndpoint(Endpoint):
    method = Method.PUT


class UpdateEndpoint(Endpoint):
    method = Method.UPDATE
