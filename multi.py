def get_input():
    print("Enter a number to see its multiplication table:")
    num = input()
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input. Please enter a positive number.")
        return get_input()

def print_table(n):
    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")

def main():
    number = get_input()
    print_table(number)

if __name__ == "__main__":
    main()
    # i have write this after first commit 
    print("Hello")
    # i have write this after second try 
    print("Second")
    #now we are in branch. what should i do 
    print("it is four?")
    # now we are in branch 
    print("we are in branch")
    # it is after barnching is down 
    print("Done")
    #hello
    print("after cloning")
    # it is someting after ...
    print("netrunner")
    
    # i wanna delete this 
    print("delete")
    
