import pytest
from module.example import example_function, Example
from main import some_helper


@pytest.fixture
def example():
    return Example()


def test_example_function():
    assert example_function() == "example function"


def test_example_class(example):
    assert isinstance(example, Example)
    assert example.example == "example class"


def test_some_fixture(some_fixture):
    assert some_fixture == "example function"


@pytest.mark.parametrize("input_arg", ["hi", "bye"])
def test_some_helper(input_arg):
    assert some_helper(input_arg) == f"I repeat: {input_arg}"