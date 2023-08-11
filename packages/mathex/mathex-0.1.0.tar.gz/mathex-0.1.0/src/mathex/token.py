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

from enum import Enum, auto
from typing import Callable, TypeAlias
from dataclasses import dataclass
from math import fmod
from mathex.enums import Error


Function: TypeAlias = Callable[[list[float]], tuple[float, Error]]
BinaryOperator: TypeAlias = Callable[[float, float], float]
UnaryOperator: TypeAlias = Callable[[float], float]


class Ref:
    def __init__(self, value: float):
        self._value = value

    def set(self, value: float):
        self._value = value

    def get(self) -> float:
        return self._value


class TokenType(Enum):
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    COMMA = auto()
    CONSTANT = auto()
    VARIABLE = auto()
    FUNCTION = auto()
    BI_OPERATOR = auto()
    UN_OPERATOR = auto()


@dataclass(kw_only=True)
class Token:
    type: TokenType


@dataclass(kw_only=True)
class ConstantToken(Token):
    type: TokenType = TokenType.CONSTANT
    value: float


@dataclass(kw_only=True)
class VariableToken(Token):
    type: TokenType = TokenType.VARIABLE
    variable: Ref


@dataclass(kw_only=True)
class FunctionToken(Token):
    type: TokenType = TokenType.FUNCTION
    function: Function


@dataclass(kw_only=True)
class BiOperatorToken(Token):
    type: TokenType = TokenType.BI_OPERATOR
    biop: BinaryOperator
    prec: int
    lassoc: bool


@dataclass(kw_only=True)
class UnOperatorToken(Token):
    type: TokenType = TokenType.UN_OPERATOR
    unop: UnaryOperator
