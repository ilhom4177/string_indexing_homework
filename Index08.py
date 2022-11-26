import string
def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    
    if s.count("*")!=0:
        return s.index('*')
    else:
        return s.count("*")!=0
print(main('1345'))
        