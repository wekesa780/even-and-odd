def check_even_odd(n):
    """
    This function takes an integer as input and returns 'Even' if the number is even, 'Odd' if the number is odd.
    """
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


num = int(input("Enter a number: "))
result = check_even_odd(num)
print(f"The number {num} is {result}.")