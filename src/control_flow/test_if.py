"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_nested_if():
    """nested IF statements"""

    number = 12
    result = ''

    if number > 0:
        if number % 2 == 0:
            result = 'Positive even number'
        else:
            result = 'Positive odd number'
    else:
        result = 'Number is not positive'

    assert result == 'Positive even number'


def test_multiple_elif():
    """multiple ELIF statements"""

    score = 85
    grade = ''

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    elif score >= 50:
        grade = 'E'
    else:
        grade = 'F'

    assert grade == 'B'
       