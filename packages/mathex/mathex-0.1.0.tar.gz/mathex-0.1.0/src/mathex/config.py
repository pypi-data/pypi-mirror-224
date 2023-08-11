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

from mathex.token import (
    Ref,
    Function,
    TokenType,
    Token,
    ConstantToken,
    VariableToken,
    FunctionToken,
)
from mathex.tokens import (
    add_token,
    sub_token,
    mul_token,
    div_token,
    pow_token,
    mod_token,
    pos_token,
    neg_token,
)
from mathex.error import IllegalNameError, RedifinitionError, UndefinedError
from mathex.enums import Error, Flags, default_flags, States


operand_order: list[TokenType | None] = [
    None,
    TokenType.LEFT_PAREN,
    TokenType.COMMA,
    TokenType.BI_OPERATOR,
    TokenType.UN_OPERATOR,
]
unary_operator_order: list[TokenType | None] = [
    None,
    TokenType.LEFT_PAREN,
    TokenType.COMMA,
    TokenType.UN_OPERATOR,
]
binary_operator_order: list[TokenType | None] = [
    TokenType.CONSTANT,
    TokenType.VARIABLE,
    TokenType.RIGHT_PAREN,
]


def verify_identifier(name: str) -> bool:
    return bool(
        name
        and not name[0].isdigit()
        and all(char.isascii() and (char.isalnum() or char == "_") for char in name)
    )


class Mathex:
    def __init__(self, flags: Flags = default_flags):
        self._flags: Flags = flags
        self._tokens: dict[str, Token] = {}

    def add_variable(self, name: str, variable: Ref):
        if not verify_identifier(name):
            raise IllegalNameError(name)

        if name in self._tokens:
            raise RedifinitionError(name, self._tokens[name])

        self._tokens[name] = VariableToken(variable=variable)

    def add_constant(self, name: str, value: float):
        if not verify_identifier(name):
            raise IllegalNameError(name)

        if name in self._tokens:
            raise RedifinitionError(name, self._tokens[name])

        self._tokens[name] = ConstantToken(value=value)

    def add_function(self, name: str, function: Function):
        if not verify_identifier(name):
            raise IllegalNameError(name)

        if name in self._tokens:
            raise RedifinitionError(name, self._tokens[name])

        self._tokens[name] = FunctionToken(function=function)

    def remove(self, name: str):
        if name not in self._tokens:
            raise UndefinedError(name)

        del self._tokens[name]

    def evaluate(self, expression: str) -> tuple[float | None, Error | None]:
        last_token: TokenType | None = None

        ops_stack: list[Token] = []
        out_queue: list[Token] = []
        res_stack: list[float] = []

        arg_count: int = 0
        arg_stack: list[int] = []
        arg_queue: list[int] = []

        i = -1
        while (i := i + 1) < len(expression):
            if expression[i] == " ":
                continue

            if expression[i].isdigit() or expression[i] == ".":
                if last_token not in operand_order:
                    return None, Error.SYNTAX_ERROR

                if arg_count == 0:
                    arg_count += 1

                value: float = 0
                decimal_place: float = 10
                exponent: float = 0
                exponent_sign: bool = True

                state: States = States.INTEGER_PART
                j = i - 1

                while (j := j + 1) < len(expression):
                    if state == States.INTEGER_PART:
                        if expression[j].isdigit():
                            value = (value * 10) + float(expression[j])
                            continue

                        if expression[j] == ".":
                            state = States.FRACTION_PART
                            continue

                        if (
                            expression[j] in ("e", "E")
                            and Flags.SCIENTIFIC_NOTATION in self._flags
                        ):
                            state = States.EXP_START
                            continue

                    elif state == States.FRACTION_PART:
                        if expression[j] == ".":
                            return None, Error.SYNTAX_ERROR

                        if expression[j].isdigit():
                            value += float(expression[j]) / decimal_place
                            decimal_place *= 10
                            continue

                        if (
                            expression[j] in ("e", "E")
                            and Flags.SCIENTIFIC_NOTATION in self._flags
                        ):
                            state = States.EXP_START
                            continue

                    elif state == States.EXP_START:
                        if expression[j] == ".":
                            return None, Error.SYNTAX_ERROR

                        if expression[j].isdigit():
                            exponent = (exponent * 10) + float(expression[j])
                            state = States.EXP_VALUE
                            continue

                        if expression[j] in ("+", "-"):
                            exponent_sign = expression[j] == "+"
                            state = States.EXP_VALUE
                            continue

                    elif state == States.EXP_VALUE:
                        if expression[j] == ".":
                            return None, Error.SYNTAX_ERROR

                        if expression[j].isdigit():
                            exponent = (exponent * 10) + float(expression[j])
                            state = States.EXP_VALUE
                            continue

                    # If reached here means number literal has ended
                    break

                # Cannot have scientific notation separator without specifying exponent
                if state == States.EXP_START:
                    j -= 1

                # ".1" => 0.1 and "1." => 1.0 but "." != 0.0
                if j - i == 1 and expression[i] == ".":
                    return None, Error.SYNTAX_ERROR

                if exponent != 0:
                    value *= pow(10.0 if exponent_sign else 0.1, exponent)

                out_queue.append(ConstantToken(value=value))

                last_token = TokenType.CONSTANT
                i = j - 1
                continue

            if expression[i].isalpha() or expression[i] == "_":
                if (
                    last_token == TokenType.CONSTANT
                    and Flags.IMPLICIT_MULTIPLICATION in self._flags
                ):
                    # Implicit multiplication
                    while ops_stack:
                        if ops_stack[-1].type == TokenType.BI_OPERATOR:
                            if not (
                                ops_stack[-1].prec > mul_token.prec
                                or (
                                    ops_stack[-1].prec == mul_token.prec
                                    and mul_token.lassoc
                                )
                            ):
                                break
                        elif ops_stack[-1].type != TokenType.UN_OPERATOR:
                            # Precedence of unary operator is always greater than of any binary operator
                            break

                        out_queue.append(ops_stack.pop())

                    ops_stack.append(mul_token)
                else:
                    # Two operands in a row are not allowed
                    # Operand should only either be first in expression or right after operator
                    if last_token not in operand_order:
                        return None, Error.SYNTAX_ERROR

                if arg_count == 0:
                    arg_count += 1

                j = i

                while (j := j + 1) < len(expression):
                    if not expression[j].isalnum() and expression[j] != "_":
                        break

                identifier: str = expression[i:j]
                fetched: Token | None = self._tokens.get(identifier)

                if fetched is None:
                    return None, Error.UNDEFINED

                if fetched.type == TokenType.FUNCTION:
                    if expression[j] != "(":
                        return None, Error.SYNTAX_ERROR

                    ops_stack.append(fetched)

                elif fetched.type in (TokenType.VARIABLE, TokenType.CONSTANT):
                    out_queue.append(fetched)

                last_token = fetched.type
                i = j - 1
                continue

            token: Token | None = None

            if expression[i] == "+":
                if (
                    Flags.ADDITION in self._flags
                    and last_token in binary_operator_order
                ):
                    # Used as binary operator
                    token = add_token

                elif (
                    Flags.IDENTITY in self._flags and last_token in unary_operator_order
                ):
                    # Used as unary operator
                    token = pos_token

                else:
                    return None, Error.SYNTAX_ERROR

            elif expression[i] == "-":
                if (
                    Flags.SUBSTRACTION in self._flags
                    and last_token in binary_operator_order
                ):
                    # Used as binary operator
                    token = sub_token

                elif (
                    Flags.NEGATION in self._flags and last_token in unary_operator_order
                ):
                    # Used as unary operator
                    token = neg_token

                else:
                    return None, Error.SYNTAX_ERROR

            elif expression[i] == "*" and Flags.MULTIPLICATION in self._flags:
                # There should always be an operand on the left hand side of the operator
                if last_token not in binary_operator_order:
                    return None, Error.SYNTAX_ERROR

                token = mul_token

            elif expression[i] == "/" and Flags.DIVISION in self._flags:
                # There should always be an operand on the left hand side of the operator
                if last_token not in binary_operator_order:
                    return None, Error.SYNTAX_ERROR

                token = div_token

            elif expression[i] == "^" and Flags.EXPONENTIATION in self._flags:
                # There should always be an operand on the left hand side of the operator
                if last_token not in binary_operator_order:
                    return None, Error.SYNTAX_ERROR

                token = pow_token

            elif expression[i] == "%" and Flags.MODULUS in self._flags:
                # There should always be an operand on the left hand side of the operator
                if last_token not in binary_operator_order:
                    return None, Error.SYNTAX_ERROR

                token = mod_token

            if token is not None:
                if token.type == TokenType.BI_OPERATOR:
                    while ops_stack:
                        if ops_stack[-1].type == TokenType.BI_OPERATOR:
                            if not (
                                ops_stack[-1].prec > token.prec
                                or (ops_stack[-1].prec == token.prec and token.lassoc)
                            ):
                                break

                        elif ops_stack[-1].type != TokenType.UN_OPERATOR:
                            # Precedence of unary operator is always greater than of any binary operator
                            break

                        out_queue.append(ops_stack.pop())

                ops_stack.append(token)
                last_token = token.type
                continue

            if expression[i] == "(":
                if last_token == TokenType.FUNCTION:
                    arg_stack.append(arg_count)
                    arg_count = 0

                else:
                    # Two operands in a row are not allowed
                    # Operand should only either be first in expression or right after operator
                    if last_token not in operand_order:
                        return None, Error.SYNTAX_ERROR

                    if arg_count == 0:
                        arg_count += 1

                ops_stack.append(Token(type=TokenType.LEFT_PAREN))
                last_token = TokenType.LEFT_PAREN
                continue

            if expression[i] == ")":
                # Empty expressions are not allowed
                if last_token == None or last_token == TokenType.COMMA:
                    return None, Error.SYNTAX_ERROR

                if last_token != TokenType.LEFT_PAREN:
                    if not ops_stack:
                        # Mismatched parenthesis (ignore if implicit parentheses are enabled)
                        if Flags.IMPLICIT_PARENTHESES not in self._flags:
                            return None, Error.SYNTAX_ERROR

                        continue

                    while ops_stack[-1].type != TokenType.LEFT_PAREN:
                        out_queue.append(ops_stack.pop())

                        if not ops_stack:
                            # Mismatched parenthesis (ignore if implicit parentheses are enabled)
                            if Flags.IMPLICIT_PARENTHESES not in self._flags:
                                return None, Error.SYNTAX_ERROR

                            break

                if ops_stack:
                    ops_stack.pop()  # Discard left parenthesis

                    if ops_stack and ops_stack[-1].type == TokenType.FUNCTION:
                        out_queue.append(ops_stack.pop())
                        arg_queue.append(arg_count)
                        arg_count = arg_stack.pop()

                    elif last_token == TokenType.LEFT_PAREN:
                        # Empty parentheses are not allowed, unless for zero-argument functions
                        return None, Error.SYNTAX_ERROR

                last_token = TokenType.RIGHT_PAREN
                continue

            if expression[i] == ",":
                # Previous argument has to be non-empty
                if last_token not in binary_operator_order:
                    return None, Error.SYNTAX_ERROR

                # Comma is only valid inside function parentheses
                if not arg_stack:
                    return None, Error.SYNTAX_ERROR

                if not ops_stack:
                    # Mismatched parenthesis (ignore if implicit parentheses are enabled)
                    if Flags.IMPLICIT_PARENTHESES not in self._flags:
                        return None, Error.SYNTAX_ERROR

                    continue

                while ops_stack[-1].type != TokenType.LEFT_PAREN:
                    out_queue.append(ops_stack.pop())

                    if not ops_stack:
                        # Mismatched parenthesis (ignore if implicit parentheses are enabled)
                        if Flags.IMPLICIT_PARENTHESES not in self._flags:
                            return None, Error.SYNTAX_ERROR

                        break

                arg_count += 1
                last_token = TokenType.COMMA
                continue

            # Any character that was not captured by previous checks is considered invalid
            return None, Error.SYNTAX_ERROR

        # Expression cannot end if operand is expected next
        if last_token in operand_order:
            return None, Error.SYNTAX_ERROR

        for token in reversed(ops_stack):
            if token.type == TokenType.LEFT_PAREN:
                # Mismatched parenthesis (ignore if implicit parentheses are enabled)
                if Flags.IMPLICIT_PARENTHESES not in self._flags:
                    return None, Error.SYNTAX_ERROR

                continue

            if token.type == TokenType.FUNCTION:
                # Implicit parentheses for zero argument functions are not allowed
                if arg_count == 0:
                    return None, Error.SYNTAX_ERROR

                arg_queue.append(arg_count)
                arg_count = arg_stack.pop()

            out_queue.append(token)

        for token in out_queue:
            if token.type == TokenType.CONSTANT:
                res_stack.append(token.value)

            elif token.type == TokenType.VARIABLE:
                res_stack.append(token.variable.get())

            elif token.type == TokenType.BI_OPERATOR:
                b: float = res_stack.pop()
                a: float = res_stack.pop()
                res_stack.append(token.biop(a, b))

            elif token.type == TokenType.UN_OPERATOR:
                x: float = res_stack.pop()
                res_stack.append(token.unop(x))

            elif token.type == TokenType.FUNCTION:
                args_num: int = arg_queue.pop(0)
                args = list(reversed([res_stack.pop() for _ in range(args_num)]))
                func_result, error = token.function(args)

                if error != None:
                    return None, error

                res_stack.append(func_result)

        result = res_stack.pop()

        # Exactly one value has to be left in results stack
        return result, Error.SYNTAX_ERROR if res_stack else None

    def _read_flag(self, flag: Flags) -> bool:
        return flag in self._flags
