
def count_characters(input_string):
    vowels = 0
    consonants = 0
    spaces = 0
    others = 0

    for char in input_string:
        if char.lower() in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Spaces:", spaces)
    print("Other Characters:", others)

def sum_digits(input_string):
    digit_sum = 0
    for char in input_string:
        if char.isdigit():
            digit_sum += int(char)

    print("Sum of Digits:", digit_sum)

def pattern_for():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def pattern_while():
    i = 1
    num = 1
    while i <= 5:
        j = 1
        while j <= i:
            if i % 2 != 0:  
              print(num, end="")
            else: 
              print(i+2, end="")
            j += 1
        if i % 2 != 0: 
          num += 2
        print()
        i += 1


input_string = input("Enter a string: ")

count_characters(input_string)
sum_digits(input_string)

print("\nPattern using for loop:")
pattern_for()

print("\nPattern using while loop:")
pattern_while()
