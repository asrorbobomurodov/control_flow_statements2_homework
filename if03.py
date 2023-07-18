def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    # between = a
    if b<=a<=c:
        return a
    if c<=a<=b:
        return a
    
    if a<=b<=c:
        return b
    if c<=b<=a:
        return b
    
    if a<=c<=b:
        return c
    else:
        return c
    
print(main(3,7,1))
print(main(6,4,1))
print(main(5,1,4))
print(main(5,5,-1))