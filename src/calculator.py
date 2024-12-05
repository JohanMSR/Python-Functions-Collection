def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b 

def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n: A non-negative integer
    Returns:
        The factorial of n (n!)
    Raises:
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1) 

def find_minimum(a: float, b: float) -> float:
    """
    Find the minimum between two numbers.
    
    Args:
        a: First number
        b: Second number
    Returns:
        The smaller of the two numbers
    """
    return a if a < b else b 

def power(base: float, exponent: int) -> float:
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The power to raise the base to
    Returns:
        base raised to the power of exponent
    """
    return base ** exponent

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n: The number to check
    Returns:
        True if the number is prime, False otherwise
    """
    if not isinstance(n, int):
        raise TypeError("Number must be an integer")
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor of two integers.
    
    Args:
        a: First integer
        b: Second integer
    Returns:
        The greatest common divisor
    """
    if not all(isinstance(x, int) for x in [a, b]):
        raise TypeError("Numbers must be integers")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def average(*numbers: float) -> float:
    """
    Calculate the arithmetic mean of a sequence of numbers.
    
    Args:
        *numbers: Variable number of numeric values
    Returns:
        The arithmetic mean
    Raises:
        ValueError: If no numbers are provided
    """
    if not numbers:
        raise ValueError("At least one number is required")
    return sum(numbers) / len(numbers)