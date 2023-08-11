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

from typing import Dict, Optional, Tuple

from .enums import Error, Flags, default_flags
from .error import IllegalNameError, RedifinitionError, UndefinedError
from .evaluate import evaluate
from .token import Function, Ref, Token


def verify_identifier(name: str) -> bool:
    return bool(
        name
        and not name[0].isdigit()
        and all(char.isascii() and (char.isalnum() or char == "_") for char in name)
    )


class Mathex:
    def __init__(self, flags: Flags = default_flags):
        self._flags: Flags = flags
        self._tokens: Dict[str, Token] = {}

    def add_variable(self, name: str, variable: Ref):
        if not verify_identifier(name):
            raise IllegalNameError(name)

        if name in self._tokens:
            raise RedifinitionError(name, self._tokens[name])

        self._tokens[name] = Token.from_variable(variable)

    def add_constant(self, name: str, value: float):
        if not verify_identifier(name):
            raise IllegalNameError(name)

        if name in self._tokens:
            raise RedifinitionError(name, self._tokens[name])

        self._tokens[name] = Token.from_constant(value)

    def add_function(self, name: str, function: Function):
        if not verify_identifier(name):
            raise IllegalNameError(name)

        if name in self._tokens:
            raise RedifinitionError(name, self._tokens[name])

        self._tokens[name] = Token.from_function(function)

    def remove(self, name: str):
        if name not in self._tokens:
            raise UndefinedError(name)

        del self._tokens[name]

    def evaluate(self, expression: str) -> Tuple[Optional[float], Optional[Error]]:
        return evaluate(expression, self._flags, self._tokens)

    def _read_flag(self, flag: Flags) -> bool:
        return flag in self._flags
