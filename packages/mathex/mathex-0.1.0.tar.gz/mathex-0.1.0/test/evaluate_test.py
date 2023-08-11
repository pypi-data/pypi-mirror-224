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

from mathex import Mathex, Ref, Error, Flags, default_flags
from pytest import fixture, approx

x: float = 5
y: float = 3
z: float = 6
pi: float = 3.14


def foo_wrapper(args: list[float]) -> tuple[float, Error]:
    if len(args) != 2:
        return None, Error.INCORRECT_ARGS_NUM

    return args[0], None


def bar_wrapper(args: list[float]) -> tuple[float, Error]:
    if len(args) != 0:
        return None, Error.INCORRECT_ARGS_NUM

    return 5.43, None


def f_wrapper(args: list[float]) -> tuple[float, Error]:
    if len(args) != 1:
        return None, Error.INCORRECT_ARGS_NUM

    return args[0] * args[0], None


def g_wrapper(args: list[float]) -> tuple[float, Error]:
    if len(args) != 1:
        return None, Error.INCORRECT_ARGS_NUM

    return 3 * args[0] - 1, None


def h_wrapper(args: list[float]) -> tuple[float, Error]:
    if len(args) != 2:
        return None, Error.INCORRECT_ARGS_NUM

    return args[0] * args[0] + args[1], None


@fixture
def config():
    config = Mathex(default_flags | Flags.EXPONENTIATION)
    config.add_constant("x", x)
    config.add_constant("y", y)
    config.add_constant("z", z)
    config.add_constant("pi", pi)

    config.add_function("foo", foo_wrapper)
    config.add_function("bar", bar_wrapper)
    config.add_function("f", f_wrapper)
    config.add_function("g", g_wrapper)
    config.add_function("h", h_wrapper)
    return config


def test_simple_expressions(config: Mathex):
    result, error = config.evaluate("5 + 3")
    assert not error and result == approx(8)

    result, error = config.evaluate("10 - 4")
    assert not error and result == approx(6)

    result, error = config.evaluate("2 * 6")
    assert not error and result == approx(12)

    result, error = config.evaluate("15 / 3")
    assert not error and result == approx(5)

    result, error = config.evaluate("4 + 6 * 2")
    assert not error and result == approx(16)

    result, error = config.evaluate("(7 + 3) * 4")
    assert not error and result == approx(40)

    result, error = config.evaluate("8 + 12 / 4 - 3 * 2")
    assert not error and result == approx(5)

    result, error = config.evaluate("10 / 3")
    assert not error and result == approx(10.0 / 3)

    result, error = config.evaluate("-5 + 3")
    assert not error and result == approx(-2)

    result, error = config.evaluate("1000000 * 1000000")
    assert not error and result == approx(1000000000000)


def test_erroneous_expressions(config: Mathex):
    _, error = config.evaluate("5 5")
    assert error == Error.SYNTAX_ERROR
    _, error = config.evaluate("() + 3")
    assert error == Error.SYNTAX_ERROR

    _, error = config.evaluate("8 +")
    assert error == Error.SYNTAX_ERROR
    _, error = config.evaluate("/ 5")
    assert error == Error.SYNTAX_ERROR

    _, error = config.evaluate("* 7 + 2")
    assert error == Error.SYNTAX_ERROR
    _, error = config.evaluate("* 7 + 2")
    assert error == Error.SYNTAX_ERROR
    _, error = config.evaluate("4 + 6 -")
    assert error == Error.SYNTAX_ERROR

    _, error = config.evaluate("3 + * 5")
    assert error == Error.SYNTAX_ERROR
    _, error = config.evaluate("4 + 6 + * 2")
    assert error == Error.SYNTAX_ERROR

    _, error = config.evaluate("5 + abc - 3")
    assert error == Error.UNDEFINED
    _, error = config.evaluate("sin(90)")
    assert error == Error.UNDEFINED


def test_number_format(config: Mathex):
    result, error = config.evaluate("30")
    assert not error and result == approx(30)

    result, error = config.evaluate("2.5")
    assert not error and result == approx(2.5)

    result, error = config.evaluate(".1")
    assert not error and result == approx(0.1)

    result, error = config.evaluate("1.")
    assert not error and result == approx(1.0)

    _, error = config.evaluate(".")
    assert error == Error.SYNTAX_ERROR
    _, error = config.evaluate("1..4")
    assert error == Error.SYNTAX_ERROR
    _, error = config.evaluate("2.6.")
    assert error == Error.SYNTAX_ERROR

    result, error = config.evaluate("5e4")
    assert not error and result == approx(50000)

    result, error = config.evaluate("5.3e4")
    assert not error and result == approx(53000)

    result, error = config.evaluate("2.4e-2")
    assert not error and result == approx(0.024)

    result, error = config.evaluate("2.4e+2")
    assert not error and result == approx(240)

    _, error = config.evaluate("2.6e")
    assert error == Error.UNDEFINED
    _, error = config.evaluate("3.4ee6")
    assert error == Error.UNDEFINED
    _, error = config.evaluate("1.6e4.3")
    assert error == Error.SYNTAX_ERROR


def test_variables(config: Mathex):
    result, error = config.evaluate("x + 5")
    assert not error and result == approx(10)

    _, error = config.evaluate("a * 2")
    assert error == Error.UNDEFINED

    result, error = config.evaluate("x + y - z")
    assert not error and result == approx(2)

    result, error = config.evaluate("-x + 7")
    assert not error and result == approx(2)

    result, error = config.evaluate("2 * pi * x")
    assert not error and result == approx(31.4)

    result, error = config.evaluate("x^3")
    assert not error and result == approx(125)

    result, error = config.evaluate("x + x - x / 2")
    assert not error and result == approx(7.5)

    result, error = config.evaluate("x^2 + y * z - z / y")
    assert not error and result == approx(41)

    result, error = config.evaluate("2^x + 3 * x - 5")
    assert not error and result == approx(42)

    _, error = config.evaluate("x + a")
    assert error == Error.UNDEFINED


def test_changing_variables(config: Mathex):
    var: Ref = Ref(0)
    config.add_variable("var", var)

    var.set(3)
    result, error = config.evaluate("var + 3")
    assert not error and result == approx(6)

    var.set(5)
    result, error = config.evaluate("var + 3")
    assert not error and result == approx(8)

    config.remove("var")


def test_functions(config: Mathex):
    result, error = config.evaluate("foo(2, 5)")
    assert not error and result == approx(2)

    result, error = config.evaluate("f(x) + 5")
    assert not error and result == approx(30)

    result, error = config.evaluate("2 * g(y) - f(x)")
    assert not error and result == approx(-9)

    result, error = config.evaluate("h(x, y) + z")
    assert not error and result == approx(34)

    result, error = config.evaluate("bar() + 2")
    assert not error and result == approx(7.43)

    _, error = config.evaluate("f(x) + d(x)")
    assert error == Error.UNDEFINED
    _, error = config.evaluate("f()")
    assert error == Error.INCORRECT_ARGS_NUM
    _, error = config.evaluate("f(3, )")
    assert error == Error.SYNTAX_ERROR

    result, error = config.evaluate("f(x) + f(y) - f(z) / 2")
    assert not error and result == approx(16)

    result, error = config.evaluate("3^2 + f(2x - g(3^1))")
    assert not error and result == approx(13)
