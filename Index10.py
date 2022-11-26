def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    sum=0
    if s.isdigit():
        sum=sum+int(s[0])
        sum=sum+int(s[1])
        sum=sum+int(s[2])
        sum=sum+int(s[3])
        sum=sum+int(s[4])
    return sum
print(main('12340'))