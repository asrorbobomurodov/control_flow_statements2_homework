def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    max = a
    
    if b>max:
        max = b

    if c>max:
        max = c

    return max
print(main(8,6,9))
print(main(-5,-3,-8))