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

from enum import Flag, Enum, auto


class Flags(Flag):
    IMPLICIT_PARENTHESES = auto()
    IMPLICIT_MULTIPLICATION = auto()
    SCIENTIFIC_NOTATION = auto()
    ADDITION = auto()
    SUBSTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()
    EXPONENTIATION = auto()
    MODULUS = auto()
    IDENTITY = auto()
    NEGATION = auto()


default_flags = (
    Flags.IMPLICIT_PARENTHESES
    | Flags.IMPLICIT_MULTIPLICATION
    | Flags.SCIENTIFIC_NOTATION
    | Flags.ADDITION
    | Flags.SUBSTRACTION
    | Flags.MULTIPLICATION
    | Flags.DIVISION
    | Flags.IDENTITY
    | Flags.NEGATION
)


class Error(Enum):
    DIVISION_BY_ZERO = auto()
    SYNTAX_ERROR = auto()
    UNDEFINED = auto()
    INVALID_ARGS = auto()
    INCORRECT_ARGS_NUM = auto()


class States(Enum):
    INTEGER_PART = auto()
    FRACTION_PART = auto()
    EXP_START = auto()
    EXP_VALUE = auto()
