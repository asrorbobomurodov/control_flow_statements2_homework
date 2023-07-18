def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """ #54673
    n1 = n%10 #3
    n = n//10 #5467

    n2 = n%10 #7
    n = n//10 #546

    n3 = n%10 #6
    n = n//10 #54

    n4 = n%10 #4
    n = n//10 #5

    n5 = n

    max = n1
    if n2>max:
        max = n2
    if n3>max:
        max = n3
    if n4>max:
        max = n4
    if n5>max:
        max = n5

    return max
print(main(65489))
print(main(12345))