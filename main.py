from src.calculator import (
    add, subtract, multiply, divide, factorial,
    find_minimum, power, is_prime, gcd, average
)

def demonstrate_calculator():
    """Demonstrate all calculator functions with examples."""
    
    print("Calculator Function Demonstrations\n")
    
    # Basic arithmetic operations
    print("1. Basic Arithmetic:")
    print(f"   Addition (5 + 3) = {add(5, 3)}")
    print(f"   Subtraction (10 - 4) = {subtract(10, 4)}")
    print(f"   Multiplication (6 × 7) = {multiply(6, 7)}")
    print(f"   Division (15 ÷ 3) = {divide(15, 3)}")
    
    # Factorial
    number = 5
    print(f"\n2. Factorial:")
    print(f"   {number}! = {factorial(number)}")
    
    # Find minimum
    a, b = 8, 3
    print(f"\n3. Finding Minimum:")
    print(f"   Minimum between {a} and {b} = {find_minimum(a, b)}")
    
    # Power
    base, exp = 2, 3
    print(f"\n4. Power:")
    print(f"   {base} raised to power {exp} = {power(base, exp)}")
    
    # Prime number check
    numbers_to_check = [2, 7, 10, 17]
    print("\n5. Prime Number Check:")
    for n in numbers_to_check:
        print(f"   Is {n} prime? {is_prime(n)}")
    
    # Greatest Common Divisor
    num1, num2 = 48, 18
    print(f"\n6. Greatest Common Divisor:")
    print(f"   GCD of {num1} and {num2} = {gcd(num1, num2)}")
    
    # Average
    numbers = [1, 2, 3, 4, 5]
    print(f"\n7. Average:")
    print(f"   Average of {numbers} = {average(*numbers)}")

if __name__ == "__main__":
    try:
        demonstrate_calculator()
    except Exception as e:
        print(f"An error occurred: {str(e)}") 