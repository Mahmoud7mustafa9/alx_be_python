
number = 0
pattern = int(input('Enter the size of the pattern: '))

while number < pattern :
    for item in range(0,pattern):
        print("*", end="")
    number = number + 1    
    print()      