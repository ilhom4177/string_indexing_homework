import string
def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    
    if s.count("*")>-1:
        return s.count("*")
    else:
        return False
print(main('2444'))
        