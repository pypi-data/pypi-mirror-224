# Copyright (c) 2023 Caps Lock

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from mathex import (
    Mathex,
    Ref,
    Error,
    IllegalNameError,
    RedifinitionError,
    UndefinedError,
)
from pytest import fixture, approx, raises


@fixture
def config() -> Mathex:
    config = Mathex()
    return config


def test_add_variable(config):
    x: Ref = Ref(5)
    y: Ref = Ref(3)

    config.add_variable("x", x)
    config.add_variable("y", y)

    with raises(RedifinitionError):
        config.add_variable("y", None)

    with raises(IllegalNameError):
        config.add_variable("رطانة", None)

    result, error = config.evaluate("x + y")
    assert not error and result == approx(8)

    x.set(3)
    y.set(10)

    result, error = config.evaluate("x + y")
    assert not error and result == approx(13)

    config.remove("x")
    config.remove("y")

    with raises(UndefinedError):
        config.remove("رطانة")

    _, error = config.evaluate("x + y")
    assert error == Error.UNDEFINED


def test_add_constant(config):
    config.add_constant("e", 2.71)
    config.add_constant("pi", 3.14)

    with raises(RedifinitionError):
        config.add_constant("pi", None)

    with raises(IllegalNameError):
        config.add_constant("رطانة", None)

    result, error = config.evaluate("e + pi")
    assert not error and result == approx(5.85)

    config.remove("e")
    config.remove("pi")

    with raises(UndefinedError):
        config.remove("رطانة")

    _, error = config.evaluate("e + pi")
    assert error == Error.UNDEFINED


def test_add_function(config):
    def foo_wrapper(args: list[float]) -> tuple[float, Error]:
        if len(args) != 0:
            return Error.INCORRECT_ARGS_NUM

        return -1.25, None

    def abs_wrapper(args: list[float]) -> tuple[float, Error]:
        if len(args) != 1:
            return Error.INCORRECT_ARGS_NUM

        return abs(args[0]), None

    config.add_function("foo", foo_wrapper)
    config.add_function("abs", abs_wrapper)

    with raises(RedifinitionError):
        config.add_function("abs", None)

    with raises(IllegalNameError):
        config.add_function("رطانة", None)

    result, error = config.evaluate("abs(foo()) + 1.12")
    assert not error and result == approx(2.37)

    config.remove("foo")
    config.remove("abs")

    with raises(UndefinedError):
        config.remove("رطانة")

    _, error = config.evaluate("abs(foo()) + 1.12")
    assert error == Error.UNDEFINED
