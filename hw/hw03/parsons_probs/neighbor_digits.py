def neighbor_digits(num, prev_digit=-1):
    # sourcery skip: assign-if-exp, merge-comparisons, merge-else-if-into-elif
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    # num % 10 == (num // 10) % 10 -> first entry,prev_digit = -1
    # num % 10 == prev_digit -> second entry, prev_digit = num % 10
    if num % 10 == prev_digit or num % 10 == (num // 10) % 10:
        if num // 10 == 0:
            return 1
        else:
            return 1 + neighbor_digits(num // 10, num % 10)
    else:
        if num // 10 == 0:
            return 0
        else:
            return neighbor_digits(num // 10, num % 10)
    
