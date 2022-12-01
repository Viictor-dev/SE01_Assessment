numbers = ["4", "0", "2", "1", "6", "5", "3", "8", "7"]
x = 0 
zero = numbers.index("0")

for nums in numbers:
    print(numbers[x])
    x += 1

user_input = input()

def move(user_input):
    x = 0

    if user_input != "0":
        index = numbers.index(user_input)

        numbers[zero], numbers[index] = numbers[index], numbers[zero]
        print("------------------------------------")
        
        for nums in numbers:
            print(numbers[x])
            x += 1

move(user_input)
