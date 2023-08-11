from typing import Dict, List, Optional, Tuple

from .enums import Error, Flags, NumParts
from .token import (
    Token,
    TokenType,
    add_token,
    div_token,
    mod_token,
    mul_token,
    neg_token,
    pos_token,
    pow_token,
    sub_token,
)

operand_order: List[Optional[TokenType]] = [
    None,
    TokenType.LEFT_PAREN,
    TokenType.COMMA,
    TokenType.BI_OPERATOR,
    TokenType.UN_OPERATOR,
]

unary_operator_order: List[Optional[TokenType]] = [
    None,
    TokenType.LEFT_PAREN,
    TokenType.COMMA,
    TokenType.UN_OPERATOR,
]

binary_operator_order: List[Optional[TokenType]] = [
    TokenType.CONSTANT,
    TokenType.VARIABLE,
    TokenType.RIGHT_PAREN,
]


def evaluate(
    expression: str, flags: Flags, tokens: Dict[str, Token]
) -> Tuple[Optional[float], Optional[Error]]:
    last_token: Optional[TokenType] = None

    ops_stack: List[Token] = []
    out_queue: List[Token] = []
    res_stack: List[float] = []

    arg_count: int = 0
    arg_stack: List[int] = []
    arg_queue: List[int] = []

    i = 0
    while i < len(expression):
        if expression[i] == " ":
            i += 1
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

            state: NumParts = NumParts.INTEGER_PART
            j = i

            while j < len(expression):
                if state == NumParts.INTEGER_PART:
                    if expression[j].isdigit():
                        value = (value * 10) + float(expression[j])
                        j += 1
                        continue

                    if expression[j] == ".":
                        state = NumParts.FRACTION_PART
                        j += 1
                        continue

                    if (
                        expression[j] in ("e", "E")
                        and Flags.SCIENTIFIC_NOTATION in flags
                    ):
                        state = NumParts.EXP_START
                        j += 1
                        continue

                elif state == NumParts.FRACTION_PART:
                    if expression[j] == ".":
                        return None, Error.SYNTAX_ERROR

                    if expression[j].isdigit():
                        value += float(expression[j]) / decimal_place
                        decimal_place *= 10
                        j += 1
                        continue

                    if (
                        expression[j] in ("e", "E")
                        and Flags.SCIENTIFIC_NOTATION in flags
                    ):
                        state = NumParts.EXP_START
                        j += 1
                        continue

                elif state == NumParts.EXP_START:
                    if expression[j] == ".":
                        return None, Error.SYNTAX_ERROR

                    if expression[j].isdigit():
                        exponent = (exponent * 10) + float(expression[j])
                        state = NumParts.EXP_VALUE
                        j += 1
                        continue

                    if expression[j] in ("+", "-"):
                        exponent_sign = expression[j] == "+"
                        state = NumParts.EXP_VALUE
                        j += 1
                        continue

                elif state == NumParts.EXP_VALUE:
                    if expression[j] == ".":
                        return None, Error.SYNTAX_ERROR

                    if expression[j].isdigit():
                        exponent = (exponent * 10) + float(expression[j])
                        state = NumParts.EXP_VALUE
                        j += 1
                        continue

                # If reached here means number literal has ended
                break

            # Cannot have scientific notation separator without specifying exponent
            if state == NumParts.EXP_START:
                j -= 1

            # ".1" => 0.1 and "1." => 1.0 but "." != 0.0
            if j - i == 1 and expression[i] == ".":
                return None, Error.SYNTAX_ERROR

            if exponent != 0:
                value *= pow(10.0 if exponent_sign else 0.1, exponent)

            out_queue.append(Token.from_constant(value))

            last_token = TokenType.CONSTANT
            i = j
            continue

        if expression[i].isalpha() or expression[i] == "_":
            if (
                last_token == TokenType.CONSTANT
                and Flags.IMPLICIT_MULTIPLICATION in flags
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

            j = i + 1

            while j < len(expression):
                if not expression[j].isalnum() and expression[j] != "_":
                    break

                j += 1

            identifier: str = expression[i:j]
            fetched: Optional[Token] = tokens.get(identifier)

            if fetched is None:
                return None, Error.UNDEFINED

            if fetched.type == TokenType.FUNCTION:
                if expression[j] != "(":
                    return None, Error.SYNTAX_ERROR

                ops_stack.append(fetched)

            elif fetched.type in (TokenType.VARIABLE, TokenType.CONSTANT):
                out_queue.append(fetched)

            last_token = fetched.type
            i = j
            continue

        token: Optional[Token] = None

        if expression[i] == "+":
            if Flags.ADDITION in flags and last_token in binary_operator_order:
                # Used as binary operator
                token = add_token

            elif Flags.IDENTITY in flags and last_token in unary_operator_order:
                # Used as unary operator
                token = pos_token

            else:
                return None, Error.SYNTAX_ERROR

        elif expression[i] == "-":
            if Flags.SUBSTRACTION in flags and last_token in binary_operator_order:
                # Used as binary operator
                token = sub_token

            elif Flags.NEGATION in flags and last_token in unary_operator_order:
                # Used as unary operator
                token = neg_token

            else:
                return None, Error.SYNTAX_ERROR

        elif expression[i] == "*" and Flags.MULTIPLICATION in flags:
            # There should always be an operand on the left hand side of the operator
            if last_token not in binary_operator_order:
                return None, Error.SYNTAX_ERROR

            token = mul_token

        elif expression[i] == "/" and Flags.DIVISION in flags:
            # There should always be an operand on the left hand side of the operator
            if last_token not in binary_operator_order:
                return None, Error.SYNTAX_ERROR

            token = div_token

        elif expression[i] == "^" and Flags.EXPONENTIATION in flags:
            # There should always be an operand on the left hand side of the operator
            if last_token not in binary_operator_order:
                return None, Error.SYNTAX_ERROR

            token = pow_token

        elif expression[i] == "%" and Flags.MODULUS in flags:
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
            i += 1
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

            ops_stack.append(Token(TokenType.LEFT_PAREN))
            last_token = TokenType.LEFT_PAREN
            i += 1
            continue

        if expression[i] == ")":
            # Empty expressions are not allowed
            if last_token == None or last_token == TokenType.COMMA:
                return None, Error.SYNTAX_ERROR

            if last_token != TokenType.LEFT_PAREN:
                if not ops_stack:
                    # Mismatched parenthesis (ignore if implicit parentheses are enabled)
                    if Flags.IMPLICIT_PARENTHESES not in flags:
                        return None, Error.SYNTAX_ERROR

                    i += 1
                    continue

                while ops_stack[-1].type != TokenType.LEFT_PAREN:
                    out_queue.append(ops_stack.pop())

                    if not ops_stack:
                        # Mismatched parenthesis (ignore if implicit parentheses are enabled)
                        if Flags.IMPLICIT_PARENTHESES not in flags:
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
            i += 1
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
                if Flags.IMPLICIT_PARENTHESES not in flags:
                    return None, Error.SYNTAX_ERROR

                i += 1
                continue

            while ops_stack[-1].type != TokenType.LEFT_PAREN:
                out_queue.append(ops_stack.pop())

                if not ops_stack:
                    # Mismatched parenthesis (ignore if implicit parentheses are enabled)
                    if Flags.IMPLICIT_PARENTHESES not in flags:
                        return None, Error.SYNTAX_ERROR

                    break

            arg_count += 1
            last_token = TokenType.COMMA
            i += 1
            continue

        # Any character that was not captured by previous checks is considered invalid
        return None, Error.SYNTAX_ERROR

    # Expression cannot end if operand is expected next
    if last_token in operand_order:
        return None, Error.SYNTAX_ERROR

    for token in reversed(ops_stack):
        if token.type == TokenType.LEFT_PAREN:
            # Mismatched parenthesis (ignore if implicit parentheses are enabled)
            if Flags.IMPLICIT_PARENTHESES not in flags:
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
