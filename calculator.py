def parse_expression(expression):
    """
    Parse a calculation containing two numbers and one operator.

    Supported operators:
    +  Addition
    -  Subtraction
    *  Multiplication
    /  Division
    """

    parts = expression.split()

    if len(parts) != 3:
        return None

    first_number, operator, second_number = parts

    try:
        first_number = float(first_number)
        second_number = float(second_number)
    except ValueError:
        return None

    if operator not in ["+", "-", "*", "/"]:
        return None

    return first_number, operator, second_number


def calculate(expression):
    """Perform a basic arithmetic calculation."""

    parsed_expression = parse_expression(expression)

    if parsed_expression is None:
        return "I could not understand that calculation."

    first_number, operator, second_number = parsed_expression

    if operator == "+":
        result = first_number + second_number

    elif operator == "-":
        result = first_number - second_number

    elif operator == "*":
        result = first_number * second_number

    elif operator == "/":
        if second_number == 0:
            return "You cannot divide by zero."

        result = first_number / second_number

    # Display whole-number results without .0
    if isinstance(result, float) and result.is_integer():
        return int(result)

    return result