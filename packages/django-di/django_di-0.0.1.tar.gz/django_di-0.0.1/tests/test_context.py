from typing import Protocol

import pytest

from django_di.context import DIContext


class ServiceProtocol(Protocol):
    pass


class Service:
    pass


def test_register_singleton_with_type_raises_error():
    context = DIContext()
    with pytest.raises(TypeError):
        context.register_singleton(Service, Service)


def test_register_singleton_with_instance():
    context = DIContext()
    context.register_singleton(Service, Service())
    actual = context.get(Service)
    assert isinstance(actual, Service)
    

def test_register_singleton_with_callable():
    context = DIContext()
    context.register_singleton(Service, lambda: Service())
    actual = context.get(Service)
    assert isinstance(actual, Service)


def test_register_singleton_with_protocol():
    context = DIContext()
    context.register_singleton(ServiceProtocol, Service())
    actual = context.get(ServiceProtocol)
    assert isinstance(actual, Service)


def test_register_transient_returns_new_instance():
    context = DIContext()
    context.register_transient(Service)
    first = context.get(Service)
    second = context.get(Service)
    assert id(first) != id(second)


def test_register_transient_without_callable():
    context = DIContext()
    context.register_transient(Service)
    actual = context.get(Service)
    assert isinstance(actual, Service)


def test_register_transient_with_callable():
    called = False
    def create_service() -> Service:
        nonlocal called
        called = True
        return Service()

    context = DIContext()
    context.register_transient(Service, create_service)
    actual = context.get(Service)
    
    assert isinstance(actual, Service)
    assert called
