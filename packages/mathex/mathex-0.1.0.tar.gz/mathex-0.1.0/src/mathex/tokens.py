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

from mathex.token import Token, BiOperatorToken, UnOperatorToken
from math import fmod


def add_wrapper(a: float, b: float) -> float:
    return a + b


def sub_wrapper(a: float, b: float) -> float:
    return a - b


def mul_wrapper(a: float, b: float) -> float:
    return a * b


def div_wrapper(a: float, b: float) -> float:
    return a / b


def pos_wrapper(x: float) -> float:
    return x


def neg_wrapper(x: float) -> float:
    return -x


add_token: Token = BiOperatorToken(biop=add_wrapper, prec=2, lassoc=True)
sub_token: Token = BiOperatorToken(biop=sub_wrapper, prec=2, lassoc=True)
mul_token: Token = BiOperatorToken(biop=mul_wrapper, prec=3, lassoc=True)
div_token: Token = BiOperatorToken(biop=div_wrapper, prec=3, lassoc=True)

pow_token: Token = BiOperatorToken(biop=pow, prec=2, lassoc=True)
mod_token: Token = BiOperatorToken(biop=fmod, prec=2, lassoc=True)

pos_token: Token = UnOperatorToken(unop=pos_wrapper)
neg_token: Token = UnOperatorToken(unop=neg_wrapper)
