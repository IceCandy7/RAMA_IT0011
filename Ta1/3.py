# ... (Character and digit counting functions remain the same) ...

# 3.a. Nested for loop (Input-based)

rows = int(input("Enter the number of rows for the nested for loop: "))
print("Nested For Loop Output:")
for i in range(1, rows + 1):
    print(" " * (2 * (rows - i)), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print("")

# 3.b. Nested while loop (Input-based)

rows = int(input("Enter the number of rows for the nested while loop: "))
print("\nNested While Loop Output:")
num = 1
i = 1
while i <= rows:
    print(" " * (2 * (rows - i)), end="")

    j = 1
    while j <= i:
        print(str(num) * (2*i-1) , end="")
        j += 1
    
    num += 2
    print("")
    i += 15