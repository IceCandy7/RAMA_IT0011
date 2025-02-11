def is_palindrome(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def process_file(filename):
    """Read the file and check if the sum of numbers in each line is a palindrome."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        
        for i, line in enumerate(lines, 1):
            numbers = list(map(int, line.strip().split(',')))  
            total = sum(numbers)  
            result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: Invalid data format in file.")


process_file("numbers.txt")
