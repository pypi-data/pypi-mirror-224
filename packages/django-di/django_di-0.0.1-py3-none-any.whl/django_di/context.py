from typing import Protocol, Type, TypeVar, Callable, Any

CT = TypeVar("CT")


class Context(Protocol):
    def register_singleton(self, service_type) -> None: ...


class DIContext(Context):
    _services: dict[Type, Any | Callable[[], Any]]

    def __init__(self) -> None:
        self._services = {}

    def register_singleton(self, service_type: Type[CT], service_class: CT) -> None:
        if isinstance(service_class, Type):
            raise TypeError(f"service_class must be an instance, not a type: {service_class}")
        self._services[service_type] = service_class

    def register_transient(
        self,
        service_type: Type[CT],
        service_callable: Callable[[], CT] | None = None
    ) -> None:
        self._services[service_type] = service_callable or (lambda: service_type())

    def get(self, service_type: Type[CT]) -> CT:
        service_or_callable = self._services[service_type]
        service: CT
        if isinstance(service_or_callable, Callable):
            service = service_or_callable()
        else:
            service = service_or_callable
        return service
