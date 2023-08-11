from mathex import Mathex, default_flags

# Use `Config` class and `DefaultFlags` to get default settings.
# For what settings are available, check out documentation.
config = Mathex(default_flags)

# Config class contains your settings along with custom
# variables and functions you inserted.
x = 1.5
config.add_constant("x", x)

# These variables and functions are then available for users
# to use in expressions.
input = "2x + 5"

# Mathex returns error and result of evaluation as a tuple.
result, error = config.evaluate(input)

# If error is None, evaluation completed without errors
if not error:
    print(f"{input} is {result}")  # Outputs `2x + 5 is 8`
