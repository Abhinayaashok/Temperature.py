def find_largest_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    print("Enter two numbers to find the largest:")
    
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        largest = find_largest_number(number1, number2)
        print(f"The largest number is: {largest}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
