def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a = s[0]
    b = s[1]
    c = s[2]
    d = s[3]
    e = s[4]

    n = 0
    if a.isdigit():
        n += 1
    if b.isdigit():
        n += 1
    if c.isdigit():
        n += 1
    if d.isdigit():
        n += 1
    if e.isdigit():
        n += 1

    return n
print(main('32x3z'))
    