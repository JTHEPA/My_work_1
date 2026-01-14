
while True:
    def main():
        user_operation = input("Choose Arithmatic Operation between (+,-,/,*) or q to quit: ").lower()
        if user_operation == 'q':
            quit()
        else:
            user_num1 = int(input("Enter fist NO: "))
            user_num2 = int(input("Enter Second NO: "))
            if user_operation == '+':
                results = addition(a = user_num1,b = user_num2)
                return f"Your Results: {results}"
                
            elif user_operation == '-':
                results = substraction(a = user_num1,b = user_num2)
                return f"Your Results: {results}"
            elif user_operation == '*':
                results = multiplication(a = user_num1,b = user_num2)
                return f"Your Results: {results}"
            elif user_operation == '/':
                results = division(a = user_num1, b = user_num2)
                return f"Your Results: {results}"
            
            else:
                if user_num1 == 0 or user_num2 == 0:
                    raise ValueError("Enter only numbers higher than 0")
                else:
                    print("choose correct operation ")
        
    def addition(a,b):
        return a + b
        
    def substraction(a,b):
        return a - b
        
    def multiplication(a,b):
        return a * b
        
    def division(a,b):
        return a/b

    if __name__ == "__main__":
        print(main())