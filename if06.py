def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1 = n%10
    n //= 10

    n2 = n%10
    n //= 10

    n3 = n%10
    n //= 10

    n4 = n%10 
    n //=10

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
    
    if n1==max:
        return 1
    if n2==max:
        return 2
    if n3==max:
        return 3
    if n4==max:
        return 4
    if n5==max:
        return 5
print(main(28561))
print(main(85648))