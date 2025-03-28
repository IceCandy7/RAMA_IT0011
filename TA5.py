# Gavin Rama
# TW24
def divide(num1, num2):
    """Divide two numbers."""
    if num2 == 0:
        return None
    return num1 / num2

def exponentiation(base, exponent):
    """Calculate the exponentiation of two numbers."""
    return base ** exponent

def remainder(dividend, divisor):
    """Calculate the remainder of two numbers."""
    if divisor == 0:
        return None
    return dividend % divisor

def summation(lower_limit, upper_limit):
    """Calculate the sum of numbers between two limits (inclusive)."""
    if upper_limit <= lower_limit:
        return None
    return sum(range(lower_limit, upper_limit + 1))

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == "Q":
            break
        
        if choice not in ["D", "E", "R", "F"]:
            print("Invalid choice. Please choose a valid option.")
            continue
        
        try:
            if choice == "D":
                num1 = float(input("Enter the dividend: "))
                num2 = float(input("Enter the divisor: "))
                result = divide(num1, num2)
                if result is None:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"{num1} divided by {num2} is {result}")
                    
            elif choice == "E":
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                result = exponentiation(base, exponent)
                print(f"{base} raised to the power of {exponent} is {result}")
                
            elif choice == "R":
                dividend = float(input("Enter the dividend: "))
                divisor = float(input("Enter the divisor: "))
                result = remainder(dividend, divisor)
                if result is None:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The remainder of {dividend} divided by {divisor} is {result}")
                    
            elif choice == "F":
                lower_limit = int(input("Enter the lower limit: "))
                upper_limit = int(input("Enter the upper limit: "))
                result = summation(lower_limit, upper_limit)
                if result is None:
                    print("Error: The upper limit must be greater than the lower limit.")
                else:
                    print(f"The sum from {lower_limit} to {upper_limit} is {result}")
                    
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
